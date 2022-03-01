import base64
import random
from math import ceil

from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA


# 隐藏加密库
def get_key(n=16):
    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
             'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    res = ""
    for i in range(n):
        id = ceil(random.random() * 35)
        res += chars[id]
    # print(res)
    return res


def aes_en(key, data):
    # AES加密，传入str类型的key和data，返回str类型的密文（B64）
    key = key.encode("utf-8")
    aes = AES.new(key, mode=AES.MODE_ECB)
    data_bs = data.encode("utf-8")
    pad_len = 16 - len(data_bs) % 16
    data_bs += (pad_len * chr(pad_len)).encode("utf-8")
    bs = aes.encrypt(data_bs)
    bs_64 = base64.b64encode(bs).decode("utf-8")
    # print('AES密文：', bs)
    # print('AES密文b64字符串:', bs_64)
    return bs_64


def rsa_en(data):
    # RSA加密，公钥固定，传入str类型的参数，返回str类型的密文（B64）
    pub_key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArKZOdKQAL+iYzJ4Q5EQzwv/yvVPnfdNVKRgNG19HbCYM4qIzFPEOFv28SVFQh+xqAj8tAfjpMSTihFwt6BQuWfZXWYpAqf4jF4cU7ez/VHJyzsn8Cb7Lf/1KsLpuz+MbqufrA57AysnLAnRXHOwik+QnpsXZYjTcjgxQ0iLMe5iJyo06CKFxH1rmgYMwS4E89kNg1VtYrFKs1MajApfhu9hTEXnm/lP24TPdefRXbf+z84p1GLue2HRhZs3wECH1HJWZOsrdL/M+wigWldY0fHoiaKsjD9rK1NyaPtk4bIYuwPsfQu5RN4hkEPpTvdw1nKzOdo77zNa5ovCY0uNLZwIDAQAB'
    rsa_pub_key = RSA.importKey(base64.b64decode(pub_key))
    pk_rsa = PKCS1_v1_5.new(rsa_pub_key)
    rsa_code = pk_rsa.encrypt(data.encode("utf-8"))
    rsa_code_b64 = base64.b64encode(rsa_code).decode("utf-8")
    # print('rsa密文b64', rsa_code_b64)
    return rsa_code_b64
