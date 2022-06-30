# -*- coding:utf-8 -*-
'''
@Author  : Eric
@Time    : 2020-09-15 17:20
@IDE     : PyCharm
'''

import requests



def ip_search(ip=None):
    assert not isinstance(ip,(int,long)),'ip类型不能为数字'
    if ip is not None:
        if isinstance(ip, (list, set)):
            for i in ip:
                url = 'http://ip-api.com/json/' + i + '?lang=zh-CN'
                response = requests.post(url)
                print response.content

        elif isinstance(ip,basestring):
            url = 'http://ip-api.com/json/' + ip + '?lang=zh-CN'
            response = requests.post(url)
            res = response.json()
            print str({u'国家': res['country'], u'省/直辖市': res['regionName'], u'城市': res['city'],
                       u'运营商': res['isp']}).replace('u\'', '\'') \
                .encode('utf-8').decode('unicode_escape')


    else:
        url = 'http://ip-api.com/json/?lang=zh-CN'
        response = requests.post(url)
        print response.content
