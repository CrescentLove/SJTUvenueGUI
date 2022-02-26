# -*- coding = utf-8 -*-
# @TIME :2022/1/18 9:54
# @Author :CrescentLove
# @Software :PyCharm
import requests


def loGin(usag):
    st_log = 0
    localUrl = 'https://sports.sjtu.edu.cn/pc/?locale=zh'
    localParam = {
        'locale': 'zh'
    }
    UserAgent = usag

    localHeader = {
        'User-Agent': UserAgent
    }
    loginRes = requests.get(localUrl, headers=localHeader, params=localParam)
    if loginRes.status_code == 200:
        print('Successful--login')
        st_log = 1
    return st_log
