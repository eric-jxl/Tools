# -*- coding:utf-8 -*-
'''
@Author  : Eric
@Time    : 2021-01-27 16:08
@IDE     : PyCharm
'''
import psycopg2


class PostgreSQL(object):
    def __init__(self, database, user, password, host, port=5432):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def __str__(self):
        return '{0},{1},{2}'.format(self.database, self.user, self.host)

    def __repr__(self):
        return "Database:%s User:%s Host:%s" % (self.database, self.user, self.host)

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, item):
        return self.__dict__[item]

    def __call__(self, *args, **kwargs):
        print('%s' % PostgreSQL.__dict__)

    @property
    def info(self):
        return psycopg2.__version__, psycopg2.__doc__

    def operate(self, sql, params):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql, params)
            self.conn.commit()
            self.close()
        except Exception, e:
            print(e.message)
        return count

    def connect(self):
        self.conn = psycopg2.connect(database=self.database, host=self.host, port=self.port, user=self.user,
                                     password=self.password)

        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_one(self, sql, params=()):
        result = None
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
        except Exception, e:
            print(e.message)
        return result

    def get_all(self, sql, params=()):
        tup = ()
        try:
            self.connect()
            self.cursor.execute(sql, params)
            tup = self.cursor.fetchall()
            self.close()
        except Exception, e:
            print(e.message)
        return tup

    def insert(self, sql, params=()):
        return self.operate(sql, params)

    def update(self, sql, params=()):
        return self.operate(sql, params)

    def delete(self, sql, params=()):
        return self.operate(sql, params)
