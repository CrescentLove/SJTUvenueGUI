# -*- coding = utf-8 -*-
# @TIME :2022/1/18 9:57
# @Author :CrescentLove
# @Software :PyCharm

import datetime
import json
import random
import time

import requests
from retry import retry

import CrescentRes.encrypt as encrypt

# 场地ID
VENTYPEID = {
    "羽毛球": "29942202-d2ac-448e-90b7-14d3c6be19ff",  # 羽毛球
    "篮球": "8dc0e52c-564a-4d9a-9cb2-08477f1a18d4"  # 篮球
}
# 场地类型
FIELDTYPE = {
    "羽毛球": "羽毛球",
    "篮球": "篮球"
}

# 场馆ID
VENUEID = {
    "气膜": "3b10ff47-7e83-4c21-816c-5edc257168c1",
    "霍体": "xxx"
}
# 场馆类型
VENUETYPE = {
    "气膜": "气膜",
    "霍体": "xxx"
}


class venSeizor():
    """
    1. 抓取场馆余票信息
    2. 按照选定的配置抢场地

    """

    def __init__(self, lcoo, bcoo, usag, spor, venu):
        self.Fcookie = lcoo
        self.userAgent = usag
        self.Fheader = {
            'User-Agent': self.userAgent,
            'Cookie': self.Fcookie,
            'Referer': 'https://sports.sjtu.edu.cn/pc/?locale=zh',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Content-Type': 'application/json;charset=UTF-8'}
        self.__Fieldurl = 'https://sports.sjtu.edu.cn/manage/fieldDetail/queryFieldSituation'
        self.Bcookie = bcoo
        self.__ConfirmUrl = 'https://sports.sjtu.edu.cn/venue/personal/ConfirmOrder'

        self.ConHeader = {
            'User-Agent': self.userAgent,
            'Cookie': self.Bcookie,
            'Referer': 'https://sports.sjtu.edu.cn/pc/?locale=zh',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json;charset=UTF-8'}

        self.venTypeId = VENTYPEID[spor]
        self.venueId = VENUEID[venu]
        self.fieldType = spor
        self.__ReturnUrl = "https://sports.sjtu.edu.cn/#/paymentResult/1"

        self.__List2RealSite = ["场地1", "场地2", "场地3", "场地4", "场地5", "场地6", "场地7", "场地8", "场地9", "场地10", "场地11", "场地12"]
        self.__List2RealTime = ["07:00-08:00", "08:00-09:00", "09:00-10:00", "10:00-11:00", "11:00-12:00",
                                "12:00-13:00",
                                "13:00-14:00", "14:00-15:00", "15:00-16:00", "16:00-17:00", "17:00-18:00",
                                "18:00-19:00",
                                "19:00-20:00", "20:00-21:00", "21:00-22:00"]
        self.__FieldId_list = [
            "fbe21877-f8f3-4ada-acb1-367691fd512c", "2b7b5e8a-93a5-477b-9902-8a0f6a84593e",
            "1849fc20-d081-4a6d-b7d4-2d26a384a56f", "1d9be5b2-6e1f-42a0-9628-1d9bf0f1ea19",
            "c45769d8-be9e-4c42-bc57-04c115afade6", "3ff530d0-df5f-4b8c-8066-a8f955fb7773",
            "745ac43b-9e83-4a76-ac0d-b2181105d18d", "c6e10322-a346-4da7-99c6-c58e72dd04a9",
            "300b4727-1aec-4469-b058-b7293a05c1a5", "e2761799-eff3-4abb-90b4-ee3ebaee0ab0",
            "ba748c5a-ac2f-4443-90f7-5b2d85510a00", "78aba2e4-9f18-4c8d-b2de-9b1cacfccfad"
        ]

    @retry(tries=3)
    def getField(self, WDate):
        """

        :param venTypeId: 羽毛球or篮球
        :param WDate: 爬取预定日期
        :return: SiteInfo预定日期
        """
        Fieldata = json.dumps({'fieldType': self.venTypeId, 'date': WDate})
        SiteInfo = [[0 for y in range(0, 12)] for x in range(0, 15)]
        try:
            FieldRes = requests.post(self.__Fieldurl, headers=self.Fheader, data=Fieldata)
            SiteInfo = [[int(FieldRes.json()["data"][y]["priceList"][x]["count"]) for y in range(0, 12)] for x in
                        range(0, 15)]
            print(SiteInfo)  # 测试用
        except Exception as e:
            print("爬取存量错误\n", e)

        return SiteInfo

    def getwhich(self, Wdate, Wtimen, Wsiten, isam, iseat):
        """
        GUI出来之前暂时不提供自由设定偏好的选项
        :param thres: 是否选择抢下午3:00前场地，默认no，
        :param Wdate: 预定日期xxxx-xx-xx,str
        :param Wtime: 预定场次x(0-->7:00-8:00,14-->21:00-22:00),int
        :param Wsite: 预定场地x(1-->场地1,12-->场地12),int
        :return: st_cru,1-->成功，0-->失败
        """

        st_cru = 0
        Sited = self.getField(self.venTypeId, Wdate)
        if Sited[Wtimen][Wsiten] == 1:
            payload = self.getInfo(Wdate, Wtimen, Wsiten)
            st_cru = self.Seizor(payload)
            time.sleep(random.randint(0, 58))
            if st_cru:
                return 1
        if 1 in Sited[Wtimen]:
            Wsite_1 = Sited[Wtimen].index(1)
            payload = self.getInfo(Wdate, Wtimen, Wsite_1)
            st_cru = self.Seizor(payload)
            if st_cru:
                return 1
            time.sleep(random.randint(0, 58))
        amlist = [-1]
        ealist = [-1]
        if isam:
            amlist = [0, 1, 2, 3]
        if iseat:
            ealist = [4, 5, 10, 11]

        for i in range(14, 0, -1):  # 不抢七点
            if i in amlist:
                continue
            if i in ealist:
                continue
            if 1 in Sited[i]:
                Wsite_1 = Sited[i].index(1)
                payload = self.getInfo(Wdate, i, Wsite_1)
                st_cru = self.Seizor(payload)
                if st_cru:
                    return 1
                time.sleep(random.randint(0, 58))

        return st_cru

    def getOne(self, Wdate, Wtime, Wsite, timeG=120000):
        """

        :param Wdate: 预定日期xxxx-xx-xx,str
        :param Wtime: 预定场次x(0-->7:00-8:00,14-->21:00-22:00),int
        :param Wsite: 预定场地x(1-->场地1,12-->场地12),int
        :return: _Status,1-->成功，0-->失败
        """
        payload = self.getInfo(Wdate, Wtime, Wsite)  # dict
        # payload = json.dumps(payload0)
        _Status = 0
        while (1):
            timeNow = datetime.datetime.now().strftime('%H%M%S')
            timeNow = int(timeNow)

            if timeNow + 1 - timeG > 0:
                _Status = self.Seizor(payload)
                if _Status:
                    break
                time.sleep(random.random() * 0.4)
                if timeNow - timeG > 20:
                    break

        return _Status

    ###########################################################################################
    @retry(tries=3)
    def Seizor(self, payload):
        """
        抢场地核心函数，
        :param payload:发送post请求所需负载,dict
        :return:st标识符，1-->成功，0-->失败
        """
        st = 0  # 标识符判断是否成功
        try:
            fieldjson = json.dumps(payload)
            print(type(fieldjson), "--SeizorNeed\n", fieldjson)  # 测试用
            aes_key = encrypt.get_key()
            data_encrypt = encrypt.aes_en(aes_key, fieldjson)

            sid = encrypt.rsa_en(aes_key)
            key_time = str(int(time.time()) * 1000)  # 前端获取的时间以毫秒为单位
            tim = encrypt.rsa_en(key_time)
            header = self.ConHeader
            header["sid"] = sid
            header["tim"] = tim
            ConRes = requests.post(self.__ConfirmUrl, headers=header, data=data_encrypt)
            # print(ConRes.json())
            if (ConRes.json()["code"] == 0):
                print('预定成功')
                st = 1
            else:
                print(ConRes.text)
                print('fail to confirm')
        except Exception as e:
            print('SeizorFail\n', e)

        return st

    def getInfo(self, Wishdate, TimeId, SiteId, UserIn=False):
        """
        生成特定日期特定时间特定场地的json
        :param Wishdate: 日期xxxx-xx-xx,str
        :param TimeId: 待抢时间(0-->7:00-8:00,14-->21:00-22:00),int
        :param SiteId: 场地号(1-->场地1,12-->场地12),int
        :param UserIn: 是否用户输入,默认false
        :return: fieldjson,场地信息,dict
        """
        if UserIn == False:
            Wdate_G = Wishdate
            Wtime_G = self.__List2RealTime[TimeId]
            Wsite_G = self.__List2RealSite[SiteId - 1]
        else:
            Wdate_G = str(input("日期：XXXX-xx-xx"))
            Wtime_G = int(input("时间：x"))
            Wsite_G = int(input("场地：x"))
        fieConfig = {
            "venTypeId": self.venTypeId,
            "venueId": self.venueId,
            "fieldType": self.fieldType,
            "returnUrl": self.__ReturnUrl,
            "scheduleDate": Wdate_G,
            "spaces": [
                {
                    "count": 1,
                    "venuePrice": "9",
                    "status": 1,
                    "scheduleTime": Wtime_G,
                    "subSitename": Wsite_G,
                    "subSiteId": self.__FieldId_list[SiteId - 1],
                    "tensity": "1",
                    "venueNum": 1
                }
            ],
            "tenSity": "紧张"}
        # fieJson = json.dumps(fieConfig)
        return fieConfig

    def fielData(self, venTypeId, WishDate):
        """
        产生获取特定日期所有场地现存数量信息所需的json
        :param venTypeId: 羽毛球或篮球，str类型
        :param WishDate: 想抢的日期xxxx-xx-xx,str
        :return: fielData场地,json
        """
        fielData = json.dumps({'fieldType': VENTYPEID[venTypeId], 'date': WishDate})
        return fielData
