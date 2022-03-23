# -*- coding:utf-8 -*-
'''
@Author  : Eric
@Time    : 2021-08-02 09:50
@IDE     : PyCharm
'''
import sys
from functools import wraps


class lazy_property(object):
    """
    Decorator for a lazy property of an object, i.e., an object attribute
    that is determined by the result of a method call evaluated once. To
    reevaluate the property, simply delete the attribute on the object, and
    get it again.
    """
    def __init__(self, fget):
        self.fget = fget

    def __get__(self, obj, cls):
        if obj is None:
            return self
        value = self.fget(obj)
        setattr(obj, self.fget.__name__, value)
        return value

    @property
    def __doc__(self):
        return self.fget.__doc__

    @staticmethod
    def reset_all(obj):
        """ Reset all lazy properties on the instance `obj`. """
        cls = type(obj)
        obj_dict = vars(obj)
        for name in obj_dict.keys():
            if isinstance(getattr(cls, name, None), lazy_property):
                obj_dict.pop(name)

def synchronized(lock_attr='_lock'):
    '''
    :param lock_attr: sync lock
    '''
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            lock = getattr(self, lock_attr)
            try:
                lock.acquire()
                return func(self, *args, **kwargs)
            finally:
                lock.release()
        return wrapper
    return decorator


def alias(*aliases):
    """ 
    Decorating a class with @alias('FOO', 'BAR', ..) allows the class to
    be referenced by each of the names provided as arguments.
    """
    def decorator(cls):
        # alias must be set in globals from caller's frame
        caller = sys._getframe(1)
        globals_dict = caller.f_globals
        for alias in aliases:
            globals_dict[alias] = cls 
        return cls 
    return decorator
