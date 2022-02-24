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

    def __init__(self, ):
        self.Fcookie = '_ga=GA1.3.1288072830.1631693652; UM_distinctid=17c5f61356a720-0f5068f62ff94c-513c164a-190140-17c5f61356b705; rememberMe=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; NSC_wt_tqpsut.tkuv.fev.do_2020=ffffffff097f1cec45525d5f4f58455e445a4a4229a0; JSESSIONID=d6044edc-2e6b-4d37-8195-8a62260c8d87'
        self.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'
        self.Fheader = {
            'User-Agent': self.userAgent,
            'Cookie': self.Fcookie,
            'Referer': 'https://sports.sjtu.edu.cn/pc/?locale=zh',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Content-Type': 'application/json;charset=UTF-8'}
        self.__Fieldurl = 'https://sports.sjtu.edu.cn/manage/fieldDetail/queryFieldSituation'
        self.Bcookie = '_ga=GA1.3.1895526322.1645009080; NSC_wt_tqpsut.tkuv.fev.do_2020=ffffffff097f1cec45525d5f4f58455e445a4a4229a0; rememberMe=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; JSESSIONID=40744859-e149-41e3-9447-5a7d91cc49f9'
        self.ConfirmUrl = 'https://sports.sjtu.edu.cn/venue/personal/ConfirmOrder'

        self.ConHeader = {
            'User-Agent': self.userAgent,
            'Cookie': self.Bcookie,
            'Referer': 'https://sports.sjtu.edu.cn/pc/?locale=zh',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json;charset=UTF-8'}

        self.venTypeId = "29942202-d2ac-448e-90b7-14d3c6be19ff"
        self.venueId = "3b10ff47-7e83-4c21-816c-5edc257168c1"
        self.fieldType = "羽毛球"
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
    def getField(self, venTypeId, WDate):
        """

        :param venTypeId: 羽毛球or篮球
        :param WDate: 爬取预定日期
        :return: SiteInfo预定日期
        """
        Fieldata = json.dumps({'fieldType': VENTYPEID[venTypeId], 'date': WDate})
        SiteInfo = [[0 for y in range(0, 12)] for x in range(0, 15)]
        try:
            FieldRes = requests.post(self.__Fieldurl, headers=self.Fheader, data=Fieldata)
            SiteInfo = [[int(FieldRes.json()["data"][y]["priceList"][x]["count"]) for y in range(0, 12)] for x in
                        range(0, 15)]
            print(SiteInfo)  # 测试用
        except Exception as e:
            print("爬取存量错误\n", e)

        return SiteInfo

    def getwhich(self, Wdate, Wtime, Wsite, thres=7):
        """
        GUI出来之前暂时不提供自由设定偏好的选项
        :param thres: 是否选择抢下午3:00前场地，默认no，
        :param Wdate: 预定日期xxxx-xx-xx,str
        :param Wtime: 预定场次x(0-->7:00-8:00,14-->21:00-22:00),int
        :param Wsite: 预定场地x(1-->场地1,12-->场地12),int
        :return: st_cru,1-->成功，0-->失败
        """
        st_cru = 0

        Sited = self.getField(Wdate)
        for i in range(14, thres, -1):
            if Sited[i][Wsite] == 1:
                payload = self.getInfo(Wdate, i, Wsite)
                st_cru = self.Seizor(payload)
                if st_cru:
                    break
                Wsite_1 = Sited[i].index(1)
                payload = self.getInfo(Wdate, i, Wsite_1)
                st_cru = self.Seizor(payload)
                if (st_cru):
                    break

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
                time.sleep(random.random() * 0.1)
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
            print(type(fieldjson), "--SeizorNeed")  # 测试用
            aes_key = encrypt.get_key()
            data_encrypt = encrypt.aes_en(aes_key, fieldjson)

            sid = encrypt.rsa_en(aes_key)
            key_time = str(int(time.time()) * 1000)  # 前端获取的时间以毫秒为单位
            tim = encrypt.rsa_en(key_time)
            header = self.ConHeader
            header["sid"] = sid
            header["tim"] = tim
            ConRes = requests.post(self.ConfirmUrl, headers=header, data=data_encrypt)
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
