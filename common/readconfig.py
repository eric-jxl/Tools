# -*- coding:utf-8 -*-
'''
@Author  : Eric
@Time    : 2021-02-07 14:01
@IDE     : PyCharm
'''
import sys

import configparser

# proDir = os.path.split(os.path.realpath(__file__))[0]
# configPath = os.path.join(proDir, "config.ini")


class ReadConfig(object):
    def __init__(self, configPath,title, name):
        self.conf = configparser.ConfigParser()
        self.title = title
        self.name = name
        self.conf.read(configPath, encoding='utf-8')
        self.conf.get(title, name)
        print self.conf.get(title, name)


    def __repr__(self):
        if sys.version_info < 3:
            print '%s' % self.conf.get(self.title, self.name)
        else:
            print('%s' % self.conf.get(self.title, self.name))

