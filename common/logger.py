# -*- coding:utf-8 -*-
'''
@Author  : Eric
@Time    : 2020-11-30 11:09
@IDE     : PyCharm
'''
__all__ =['Logger','FuncLog']

import logging
import traceback
from logging import handlers
from logging.handlers import TimedRotatingFileHandler


class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }  # 日志级别关系映射

    def __init__(self, filename, level='info', when='D', backCount=3,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d-%(funcName)s] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
        sh = logging.StreamHandler()  # 往屏幕上输出
        sh.setFormatter(format_str)  # 设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount,
                                               encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒 M 分 H 小时、D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)  # 设置文件里写入的格式
        self.logger.addHandler(sh)  # 把对象加到logger里
        self.logger.addHandler(th)


class FuncLog(object):
    @staticmethod
    def loggerInFile(filename):  # 带参数的装饰器需要2层装饰器实现,第一层传参数，第二层传函数，每层函数在上一层返回
        def decorator(func):
            def inner(*args, **kwargs):  # 1
                logger = logging.getLogger(filename)
                logger.setLevel(logging.INFO)
                handler = TimedRotatingFileHandler(filename,
                                                   when="d",
                                                   interval=1,
                                                   backupCount=5)
                formatter = logging.Formatter(
                    '%(asctime)s - %(pathname)s[line:%(lineno)d-%(funcName)s] - %(levelname)s: %(message)s')
                console =logging.StreamHandler()
                console.setLevel(logging.INFO)
                console.setFormatter(formatter)
                handler.setFormatter(formatter)
                logger.addHandler(handler)
                logger.addHandler(console)
                try:
                    result = func(*args, **kwargs)  # 2
                    logger.info(result)
                except:
                    logger.error(traceback.format_exc())

            return inner
        return decorator
