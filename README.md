# Tools
[![License](https://img.shields.io/:license-apache-blue.svg)](https://opensource.org/licenses/Apache-2.0)
![latest 1.3.4](https://img.shields.io/badge/latest-1.3.4-green.svg?style=flat)
![GitHub commits since latest release](https://img.shields.io/github/commits-since/eric-jxl/Tools/latest)
[![Publish Python Package](https://github.com/eric-jxl/Tools/actions/workflows/publish-pypi.yml/badge.svg)](https://github.com/eric-jxl/Tools/actions/workflows/publish-pypi.yml)


[Reids](https://eric-jxl.github.io/bak/index.html)

#### Project management of Python daily tools

```shell 
pip install eric_tools
```



|                                                                文件名                                                                |              说明               |
| :----------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------: |
| [encryption_classmethod.py ](https://github.com/eric-jxl/Tools/blob/62f538a1d34df869722c68e3ea5df222bdd1605e/eric_tools/Abstract.py) |      HMAC+MD5加密签名算法       |
| [exception_class.py](https://github.com/eric-jxl/Tools/blob/62f538a1d34df869722c68e3ea5df222bdd1605e/eric_tools/exception_class.py)  |             异常类              |
|    [resize_image.py](https://github.com/eric-jxl/Tools/blob/62f538a1d34df869722c68e3ea5df222bdd1605e/eric_tools/resize_image.py)     |            图片压缩             |
|              [ip.py](https://github.com/eric-jxl/Tools/blob/62f538a1d34df869722c68e3ea5df222bdd1605e/eric_tools/ip.py)               |          ip地址定位API          |
|          [logger.py](https://github.com/eric-jxl/Tools/blob/62f538a1d34df869722c68e3ea5df222bdd1605e/eric_tools/logger.py)           |   日志模块类和高级日志装饰器    |
|          [remove.py](https://github.com/eric-jxl/Tools/blob/62f538a1d34df869722c68e3ea5df222bdd1605e/eric_tools/remove.py)           |            删除文件             |
|      [send_email.py](https://github.com/eric-jxl/Tools/blob/62f538a1d34df869722c68e3ea5df222bdd1605e/eric_tools/send_email.py)       |            发送邮件             |
|            [sftp.py](https://github.com/eric-jxl/Tools/blob/62f538a1d34df869722c68e3ea5df222bdd1605e/eric_tools/sftp.py)             |         ssh远程下载文件         |
|           [pgsql.py](https://github.com/eric-jxl/Tools/blob/62f538a1d34df869722c68e3ea5df222bdd1605e/eric_tools/pgsql.py)            |         postgresql CRUD         |
|      [readconfig.py](https://github.com/eric-jxl/Tools/blob/62f538a1d34df869722c68e3ea5df222bdd1605e/eric_tools/readconfig.py)       |        读取.ini配置文件         |
|     [jwt_encrypt.py](https://github.com/eric-jxl/Tools/blob/62f538a1d34df869722c68e3ea5df222bdd1605e/eric_tools/jwt_encrypt.py)      | 生成jwt Access Token 加密及解密 |
|    [convert_json.py](https://github.com/eric-jxl/Tools/blob/62f538a1d34df869722c68e3ea5df222bdd1605e/eric_tools/convert_json.py)     |    支持json和object之间转换     |
|        [Abstract.py](https://github.com/eric-jxl/Tools/blob/62f538a1d34df869722c68e3ea5df222bdd1605e/eric_tools/Abstract.py)         |           抽象类模型            |
|       [decorator.py](https://github.com/eric-jxl/Tools/blob/62f538a1d34df869722c68e3ea5df222bdd1605e/eric_tools/decorator.py)        |         惰性属性装饰器          |
|     [async_queue.py](https://github.com/eric-jxl/Tools/blob/62f538a1d34df869722c68e3ea5df222bdd1605e/eric_tools/async_queue.py)      |            异步队列             |
|      [downloader.py](https://github.com/eric-jxl/Tools/blob/62f538a1d34df869722c68e3ea5df222bdd1605e/eric_tools/downloader.py)       |             下载器              |
|        [logMixin.py](https://github.com/eric-jxl/Tools/blob/62f538a1d34df869722c68e3ea5df222bdd1605e/eric_tools/logMixin.py)         |    日志元类和高级日志装饰器     |
|       [nginx_log.py](https://github.com/eric-jxl/Tools/blob/62f538a1d34df869722c68e3ea5df222bdd1605e/eric_tools/nginx_log.py)        |  nginx日志解析(默认access.log)  |



​            

>[!TIP]
>
> * async_queue.py          异步队列操作
> 
> * downloader.py           下载器
> 
> * logMixIn.py             日志元类和高级日志装饰器
> 
> * nginx_log.py            nginx日志解析(默认access.log)
>
> * dynamic_settings        一个动态加载配置类(支持toml、yml、conf、csv、ini等)
>
> * delete_duplicate        删除工作区重复文件(包括图片等)
