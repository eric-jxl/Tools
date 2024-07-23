import sys
import os
import datetime

# 定义一个函数来获取用户的输入


def get_user_input(prompt):
    return input(prompt)


# 获取当前日期
today = datetime.date.today()

# 获取过去三天的日期
three_days_ago = today - datetime.timedelta(days=3)

# 获取要切割的日志文件路径
log_file_path = '/var/log/nginx/access.log'

# 获取要匹配的IP地址
ip_address = get_user_input("Enter the IP address to match: ")

# 创建一个新文件来存储切割后的日志
output_file_path = 'nginx_access_log_cut.txt'
with open(output_file_path, 'w') as output_file:
    # 逐行读取日志文件
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            # 分割日志行
            parts = line.split()

            # 获取日志日期
            log_date = parts[3][1:]

            # 检查日志日期是否在过去三天内
            if log_date >= three_days_ago.strftime('%d/%b/%Y'):
                # 检查日志行是否包含匹配的IP地址
                if ip_address in line:
                    # 将日志行写入输出文件
                    output_file.write(line)

# 打印切割后的日志文件路径
print(f"Cut nginx access log saved to: {output_file_path}")
