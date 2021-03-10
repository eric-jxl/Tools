# -*- coding:utf-8 -*-
'''
@Author  : Eric
@Time    : 2020-09-10 10:37
@IDE     : PyCharm
'''

import os
import time
import datetime


class RemoveFile(object):
    def __init__(self, filename, timedifference):
        self.filename = filename
        self.timedifference = timedifference

    @staticmethod
    def fileremove(filename, timedifference):
        '''remove file'''

        date = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
        now = datetime.datetime.now()

        if (now - date).seconds > timedifference:
            if os.path.exists(filename):
                os.remove(filename)
                print 'remove file: %s' % filename
            else:
                print 'no such file: %s' % filename


FILE_DIR = '/home'

if __name__ == '__main__':

    print 'Script is running...'

    while True:
        ITEMS = os.listdir(FILE_DIR)
        NEWLIST = []
        for names in ITEMS:
            if names.endswith(".txt"):
                NEWLIST.append(FILE_DIR + names)

        for names in NEWLIST:
            print 'current file: %s' % (names)
            RemoveFile.fileremove(names, 10)

        time.sleep(2)
