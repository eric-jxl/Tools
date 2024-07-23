# -*- coding:utf-8 -*-
'''
@Author  : Eric
@Time    : 2020-09-15 17:20
@IDE     : PyCharm
'''

import requests


def ip_search(ip=None):
    assert not isinstance(ip, (int, float)), 'ip类型不能为数值'
    if ip is not None:
        if isinstance(ip, (list, set)):
            for i in ip:
                url = 'http://ip-api.com/json/' + i + '?lang=zh-CN'
                response = requests.post(url)
                print(response.json())

        elif isinstance(ip, str):
            url = 'http://ip-api.com/json/' + ip + '?lang=zh-CN'
            response = requests.post(url)
            res = response.json()
            print(str({'国家': res['country'], '省/直辖市': res['regionName'], '城市': res['city'],
                       '运营商': res['isp']}))

    else:
        url = 'http://ip-api.com/json/?lang=zh-CN'
        response = requests.post(url)
        print(response.content)
