class Meta(type):
    """自定义元类，用于动态添加Mixin"""

    def __new__(meta, name, bases, dct):
        if "use_logging" in dct and dct["use_logging"]:
            dct.update(LogMixin.__dict__)  # 动态添加LogMixin的属性和方法
        return super().__new__(meta, name, bases, dct)


class LogMixin:
    def log(self, message):
        print(f"{self.__class__.__name__}: {message}")


class MyClass(metaclass=Meta):
    use_logging = True  # 设置标志位，指示是否使用日志Mixin

    def do_something(self):
        self.log("Doing something...")


class StrategyMeta(type):
    """更智能的元类，根据类属性动态选择Mixin"""

    def __new__(meta, name, bases, dct):
        mixins_to_apply = []
        if "security_required" in dct and dct["security_required"]:
            mixins_to_apply.append(SecurityMixin)
        if "cache_enabled" in dct and dct["cache_enabled"]:
            mixins_to_apply.extend([CacheMixin, CacheControlMixin])

        for mixin in mixins_to_apply:
            dct.update(mixin.__dict__)

        return super().__new__(meta, name, bases, dct)


class MySecureClass(metaclass=StrategyMeta):
    security_required = True
    cache_enabled = True

    def perform_operation(self):
        self.secure_access()
        self.cache_data()
        self.control_cache()


_registry = []


class RegisterMixinMeta(type):
    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)
        if 'register_me' in dct and dct['register_me']:
            _registry.append(new_class)
        return new_class


class IPlugin(metaclass=RegisterMixinMeta):
    """接口类 ，定义了插件应实现的方法"""

    def plugin_action(self):
        raise NotImplementedError("Subclasses must implement plugin_action.")


class PluginA(IPlugin):
    register_me = True

    def plugin_action(self):
        print("Plugin A is active.")


class PluginB(IPlugin):
    def plugin_action(self):
        print("Plugin B is active but not registered explicitly.")


# 使用示例
for plugin_class in _registry:
    plugin_class().plugin_action()


if __name__ == "__main__":
    my_instance = MyClass()
    my_instance.do_something()
