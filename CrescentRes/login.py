# -*- coding = utf-8 -*-
# @TIME :2022/1/18 9:54
# @Author :CrescentLove
# @Software :PyCharm
import requests


def loGin():
    st_log = 0
    localUrl = 'https://sports.sjtu.edu.cn/pc/?locale=zh'
    localParam = {
        'locale': 'zh'
    }
    UserAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'

    localHeader = {
        'User-Agent': UserAgent
    }
    loginRes = requests.get(localUrl, headers=localHeader, params=localParam)
    if loginRes.status_code == 200:
        print('Successful--login')
        st_log = 1
    return st_log
