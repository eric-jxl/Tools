import os

os.system("wget http://nginx.org/download/nginx-1.16.1.tar.gz")
os.system("tar -zxvf nginx-1.16.1.tar.gz")
os.system("cd nginx-1.16.1/")
os.system("./configure --prefix=/usr/local/nginx ")
os.system("make && make install && nginx -s reload")
os.system("/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf ")
