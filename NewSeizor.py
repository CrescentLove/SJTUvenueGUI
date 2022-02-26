# -*- coding = utf-8 -*-
# @TIME :2022/2/25 19:18
# @Author :CrescentLove
# @Software :PyCharm
import datetime
import os

from CrescentRes.login import loGin
from CrescentRes.seizor import venSeizor


class Auto():
    def __init__(self, slow, noam, noeat, notod, dlist, sport, venue, timeI, field, lcoo, bcoo, usag):
        self.usag = usag
        self.bcoo = bcoo
        self.lcoo = lcoo
        self.field = field
        self.timeI = timeI
        self.venue = venue
        self.sport = sport
        self.dlist = dlist
        self.notod = notod
        self.noeat = noeat
        self.slow = slow
        self.noam = noam
        self.datelist = [(datetime.date.today() + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(8)]
        self.__List2RealSite = ["场地1", "场地2", "场地3", "场地4", "场地5", "场地6", "场地7", "场地8", "场地9", "场地10", "场地11", "场地12"]
        self.__List2RealTime = ["07:00-08:00", "08:00-09:00", "09:00-10:00", "10:00-11:00", "11:00-12:00",
                                "12:00-13:00",
                                "13:00-14:00", "14:00-15:00", "15:00-16:00", "16:00-17:00", "17:00-18:00",
                                "18:00-19:00",
                                "19:00-20:00", "20:00-21:00", "21:00-22:00"]

    def run(self):
        loGin(self.usag)
        print(self.dlist)
        os.system("pause")
        timeN = int(datetime.datetime.now().strftime("%H%M"))
        Wtimen = self.__List2RealTime.index(self.timeI)
        Wsiten = self.__List2RealSite.index(self.field)
        seizor = venSeizor(self.lcoo, self.bcoo, self.usag, self.sport, self.venue)
        while 1:
            if timeN < 1150:
                for i in range(7, 0, -1):
                    if i == 0 and self.notod:
                        continue
                    if self.dlist[i] == 1:
                        seizor.getwhich(self.datelist[i], Wtimen, Wsiten, self.noam, self.noeat)
            else:

                st_One = seizor.getOne(self.datelist[6], Wtimen, Wsiten)
                for i in range(7, -1):
                    if i == 0 and self.notod:
                        continue
                    if self.dlist[i] == 1:
                        seizor.getwhich(self.datelist[i], Wtimen, Wsiten, self.noam, self.noeat)
