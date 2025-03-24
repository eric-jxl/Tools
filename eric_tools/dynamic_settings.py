import os
import yaml
import toml
import csv
import configparser
import logging
from collections.abc import MutableMapping
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__.rsplit("/", 1)[1])

__all__ = ["DynamicConfig"]



class ConfigFileHandler(FileSystemEventHandler):
    """Handles file changes and reloads the configuration."""

    def __init__(self, config, file_path):
        self.config = config
        self.file_path = file_path

    def on_modified(self, event):
        if event.src_path == self.file_path:
            print(f"Configuration file {self.file_path} changed, reloading...")
            self.config.force_reload(self.file_path)


class DynamicConfig(MutableMapping):
    def __init__(self, watch_file=None, **kwargs):
        self.watch_file = watch_file
        self.config = kwargs  # Support setting variables directly

        if watch_file:
            self.load(watch_file)
            self._start_watching()

    def _start_watching(self):
        """Starts a background thread to monitor file changes."""
        observer = Observer()
        observer.schedule(ConfigFileHandler(self, self.watch_file), path=os.path.dirname(
            self.watch_file) or ".", recursive=False)
        observer.start()
        self._observer = observer

    def load(self, file_path=None):
        """Loads configuration from a file and merges with existing values."""
        if file_path:
            self.file_path = file_path

        if not self.file_path or not os.path.exists(self.file_path):
            logger.error(f"Configuration file '{self.file_path}' not found.")
            return

        loaders = {
            ".yml": self._load_yaml, ".yaml": self._load_yaml,
            ".toml": self._load_toml, ".csv": self._load_csv,
            ".conf": self._load_conf, ".ini": self._load_conf
        }

        ext = os.path.splitext(self.file_path)[-1].lower()
        if ext not in loaders:
            raise ValueError(f"Unsupported file format: {ext}")

        file_config = loaders[ext](self.file_path, self.config)

        logger.debug("Updated Config:", self.config)  # Debugging

    def force_reload(self):
        """Manually trigger configuration reload (used in watchdog)."""
        logger.info("Force reloading configuration...")
        if self.watch_file:
            self.load(self.watch_file)

    def _load_yaml(self, file_path, config):
        with open(file_path, 'r', encoding='utf-8') as f:
            config.update(yaml.safe_load(f) or {})

    def _load_toml(self, file_path, config):
        with open(file_path, 'r', encoding='utf-8') as f:
            config.update(toml.load(f))

    def _load_csv(self, file_path, config):
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            config.update({row[0]: row[1] for row in reader if len(row) >= 2})

    def _load_conf(self, file_path, config):
        parser = configparser.ConfigParser()
        parser.read(file_path, encoding='utf-8')
        for section in parser.sections():
            for key, value in parser.items(section):
                config[f"{section}.{key}"] = value

    def set(self, key, value):
        """Sets a configuration variable."""
        self.config[key] = value

    def get(self, key, default=None):
        """支持多层级 `.` 分隔键访问，如 `config.get("database.host")`"""
        if key in self.config:
            return self.config[key]
        keys = key.split(".")  # 按 `.` 分割多级键
        value = self.config  # 从 `self.config` 开始查找

        try:
            for k in keys:
                if isinstance(value, dict):  # 如果是字典，继续查找键
                    value = value[k]
                elif isinstance(value, list) and k.isdigit():  # 如果是列表，并且 k 是索引
                    value = value[int(k)]
                else:
                    return default  # 找不到，返回默认值
            return value
        except (KeyError, IndexError, TypeError):
            return default  # 访问失败，返回默认值

    def __getitem__(self, key):
        return self.config[key]

    def __setitem__(self, key, value):
        self.config[key] = value

    def __delitem__(self, key):
        del self.config[key]

    def __iter__(self):
        return iter(self.config)

    def __len__(self):
        return len(self.config)

    def __repr__(self):
        return f"DynamicConfig({self.config})"

    def stop_watching(self):
        """Stops the file watcher."""
        if hasattr(self, "_observer"):
            self._observer.stop()
            self._observer.join()

if __name__ == "__main__":
    config = DynamicConfig(watch_file="config.yml")
    print(config.get("development.password"))