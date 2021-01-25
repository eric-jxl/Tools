# -*- coding:utf-8 -*-
'''
@Author  : Eric
@Time    : 2020-11-30 15:06
@IDE     : PyCharm
'''
import paramiko


def remote_scp(host_ip, remote_path, local_path, username, password=None):
    t = paramiko.Transport(host_ip)
    t.connect(username=username, password=password)  # 登录远程服务器
    sftp = paramiko.SFTPClient.from_transport(t)  # sftp传输协议
    sftp.get(remote_path, local_path)
    t.close()


