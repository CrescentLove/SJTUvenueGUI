# -*- coding = utf-8 -*-
# @TIME :2022/1/18 10:06
# @Author :CrescentLove
# @Software :PyCharm

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

FieldId_list = [
    "fbe21877-f8f3-4ada-acb1-367691fd512c", "2b7b5e8a-93a5-477b-9902-8a0f6a84593e",
    "1849fc20-d081-4a6d-b7d4-2d26a384a56f", "1d9be5b2-6e1f-42a0-9628-1d9bf0f1ea19",
    "c45769d8-be9e-4c42-bc57-04c115afade6", "3ff530d0-df5f-4b8c-8066-a8f955fb7773",
    "745ac43b-9e83-4a76-ac0d-b2181105d18d", "c6e10322-a346-4da7-99c6-c58e72dd04a9",
    "300b4727-1aec-4469-b058-b7293a05c1a5", "e2761799-eff3-4abb-90b4-ee3ebaee0ab0",
    "ba748c5a-ac2f-4443-90f7-5b2d85510a00", "78aba2e4-9f18-4c8d-b2de-9b1cacfccfad"
]

import json


class fieldCase():
    # def __init__(self,venTypeId,venueId,fieldType,WishDate,WishTime,WishSite):
    #     self.venTypeId = venTypeId
    #     self.venueId = venueId
    #     self.fieldType = fieldType
    #     self.WishDate = WishDate
    #     self.WishTime = WishTime
    #     self.WishSite = WishSite
    #     self.ReturnUrl = "https://sports.sjtu.edu.cn/#/paymentResult/1"
    def __init__(self):
        self.venTypeId = "29942202-d2ac-448e-90b7-14d3c6be19ff"
        self.venueId = "3b10ff47-7e83-4c21-816c-5edc257168c1"
        self.fieldType = "羽毛球"
        self.__ReturnUrl = "https://sports.sjtu.edu.cn/#/paymentResult/1"

        self.List2RealSite = ["场地1", "场地2", "场地3", "场地4", "场地5", "场地6", "场地7", "场地8", "场地9", "场地10", "场地11", "场地12"]
        self.List2RealTime = ["07:00-08:00", "08:00-09:00", "09:00-10:00", "10:00-11:00", "11:00-12:00", "12:00-13:00",
                              "13:00-14:00", "14:00-15:00", "15:00-16:00", "16:00-17:00", "17:00-18:00", "18:00-19:00",
                              "19:00-20:00", "20:00-21:00", "21:00-22:00"]

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
            Wtime_G = self.List2RealTime[TimeId]
            Wsite_G = self.List2RealSite[SiteId - 1]
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
                    "subSiteId": FieldId_list[SiteId - 1],
                    "tensity": "1",
                    "venueNum": 1
                }
            ],
            "tenSity": "紧张"}
        # fieJson = json.dumps(fieConfig)
        return fieConfig

    def _fielData(self, venTypeId, WishDate):
        """
        产生获取特定日期所有场地现存数量信息所需的json
        :param venTypeId: 羽毛球或篮球，str类型
        :param WishDate: 想抢的日期xxxx-xx-xx,str
        :return: fielData场地,json
        """
        fielData = json.dumps({'fieldType': VENTYPEID[venTypeId], 'date': WishDate})
        return fielData

    def __str__(self):
        return ("待改")

    def __repr__(self):
        return self.venTypeId

# __ALL__ = []
