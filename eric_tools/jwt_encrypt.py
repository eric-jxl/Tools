# -*- coding:utf-8 -*-
'''
@Author  : Eric
@Time    : 2021-03-19 13:26
@IDE     : PyCharm
'''

from jose.exceptions import ExpiredSignatureError, JWTError
from jose import jwt
import uuid
from datetime import datetime, timedelta


class GenerateAuthenticate(object):
    def __init__(self, secretKey, cipher_text):
        self.secretKey = secretKey
        self.cipher_text = cipher_text
        super(GenerateAuthenticate, self).__init__(
            secret_key=secretKey, cipher_text=cipher_text)

    @staticmethod
    def generate_access_token(SECRET_KEY, Plaintext):
        expire = datetime.utcnow() + timedelta(minutes=1)
        to_encode = {"exp": expire, "sub": str(
            Plaintext), "uid": str(uuid.uuid4())}
        token = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
        return token

    @staticmethod
    def check_access_token(Ciphertext, secretKey):
        try:
            payload = jwt.decode(Ciphertext, secretKey, algorithms="HS256")
            import sys
            if isinstance(payload, unicode) or sys.version_info[0] < 3:
                print(str(payload).encode('utf-8').replace('u\'', ''))
            else:
                print(payload)
            return payload

        except ExpiredSignatureError:
            print(u"token过期")
        except JWTError:
            print(u"token验证失败")
