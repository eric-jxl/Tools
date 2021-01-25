# -*- coding:utf-8 -*-
'''
@Author  : Eric
@Time    : 2020-11-30 14:55
@IDE     : PyCharm
'''
import re
import datetime
import pandas as pd
import xlwt

obj = re.compile(
    r'(?P<ip>.*?)- - \[(?P<time>.*?)\] "(?P<request>.*?)" (?P<status>.*?) (?P<bytes>.*?) "(?P<referer>.*?)" "(?P<ua>.*?)"')


def load_log(path):
    lst = []
    error_lst = []
    i = 0
    with open(name=path, mode="r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            dic = parse(line)
            if dic:  # 正确的数据添加到lst列表中
                lst.append(dic)
            else:
                error_lst.append(line)  # 脏数据添加到error_lst列表中
            i += 1

    return lst, error_lst

def parse(line):
    # 解析单行nginx日志
    dic = {}
    try:
        result = obj.match(line)
        # ip处理
        ip = result.group("ip")
        if ip.strip() == '-' or ip.strip() == "":  # 如果是匹配到没有ip就把这条数据丢弃
            return False
        dic['ip'] = ip.split(",")[0]  # 如果有两个ip，取第一个ip

        # 状态码处理
        status = result.group("status")  # 状态码
        dic['status'] = status

        # 时间处理
        time = result.group("time")  # 21/Dec/2019:21:45:31 +0800
        time = time.replace(" +0800", "")  # 替换+0800为空
        t = datetime.datetime.strptime(time, "%d/%b/%Y:%H:%M:%S")  # 将时间格式化成友好的格式
        dic['time'] = t

        # request处理
        request = result.group(
            "request")  # GET /post/pou-xi-he-jie-jue-python-zhong-wang-luo-nian-bao-de-zheng-que-zi-shi/ HTTP/1.1
        a = request.split()[1].split("?")[0]  # 往往url后面会有一些参数，url和参数之间用?分隔，取出不带参数的url
        dic['request'] = a

        # user_agent处理
        ua = result.group("ua")
        if "Windows NT" in ua:
            u = "windows"
        elif "iPad" in ua:
            u = "ipad"
        elif "Android" in ua:
            u = "android"
        elif "Macintosh" in ua:
            u = "mac"
        elif "iPhone" in ua:
            u = "iphone"
        else:
            u = "其他设备"
        dic['ua'] = u

        # refer处理
        referer = result.group("referer")
        dic['referer'] = referer

        return dic

    except:
        return False


def analyse(lst): # [{ip:xxx, api:xxx, status:xxxx, ua:xxx}]
    df = pd.DataFrame(lst)  # 转换成表格
    # print(df['ip'])  # 只取出ip这一列
    ip_count = pd.value_counts(df['ip']).reset_index().rename(columns={"index": "ip", "ip": "count"}).iloc[:20, :]
    request_count = pd.value_counts(df['request']).reset_index().rename(columns={"index": "request", "request": "count"}).iloc[:20, :]
    ua_count = pd.value_counts(df['ua']).reset_index().rename(columns={"index": "ua", "ua": "count"}).iloc[:, :]

    # 从pandas转化成我们普通的数据
    ip_count_values = ip_count.values
    request_count_values = request_count.values
    ua_count_values = ua_count.values

    # 写入excel
    wb = xlwt.Workbook()  # 打开一个excel文档
    sheet = wb.add_sheet("ip访问top20")  # 新建一个sheet页
    # 写入头信息
    row = 0
    sheet.write(row, 0, "ip")  # 写入行，列，内容
    sheet.write(row, 1, "count")  # 写入行，列，内容
    row += 1  # 行号加一
    for item in ip_count_values:
        sheet.write(row, 0, item[0])
        sheet.write(row, 1, item[1])
        row += 1

    sheet = wb.add_sheet("request访问top20")  # 新建一个sheet页
    # 写入头信息
    row = 0
    sheet.write(row, 0, "request")  # 写入行，列，内容
    sheet.write(row, 1, "count")  # 写入行，列，内容
    row += 1  # 行号加一
    for item in request_count_values:
        sheet.write(row, 0, item[0])
        sheet.write(row, 1, item[1])
        row += 1

    sheet = wb.add_sheet("ua访问top")  # 新建一个sheet页
    # 写入头信息
    row = 0
    sheet.write(row, 0, "ua")
    sheet.write(row, 1, "count")
    row += 1  # 行号加一
    for item in ua_count_values:
        sheet.write(row, 0, item[0])
        sheet.write(row, 1, item[1])
        row += 1

    wb.save("nginx.xls")

if __name__ == '__main__':
    lst, error_lst = load_log("nginx_error.log")
    analyse(lst)