# -*- coding:utf-8 -*-
'''
@Author  : Eric
@Time    : 2020-11-30 17:31
@IDE     : PyCharm
'''
name = 'Eric-Tools'
__title__ = 'tools'
__description__ = 'Python HTTP for Humans.'
__version__ = "1.1.3.3"
__author__ = 'Eric'
__doc__ = ["Python Daily Development Tools"]
__url__ = "https://github.com/Eric-jxl/Tools"
__license__ = "MIT"

from . import exception_class
from . import resize_image
from . import logger
import ip
from . import encryption_classmethod
from . import pgsql
from . import sftp
import readconfig
import send_email
import jwt_encrypt
