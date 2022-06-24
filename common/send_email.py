# -*- coding:utf-8 -*-
'''
@Author  : Eric
@Time    : 2021-01-15 13:50
@IDE     : PyCharm
'''

__doc__ = ["测试QQ邮箱,pwd为邮箱授权码"]

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import sys
reload(sys)
sys.setdefaultencoding("utf-8")




def mail(send_email,receive_email,send_nickname,receive_nickname,pwd):
    try:
        msg = MIMEText('Test QQ Email', 'plain', 'utf-8')
        msg['From'] = formataddr([send_nickname, send_email])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr([receive_nickname, receive_email])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = str("发送邮件测试").decode('utf-8') # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(send_email, pwd)
        server.sendmail(send_email, [receive_email, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:
        print '发送邮件失败:%s' % e
        return e


