# -*- coding = utf-8 -*-
# @TIME :2022/2/25 12:48
# @Author :CrescentLove
# @Software :PyCharm

from tkinter import *
import datetime
datelist = [(datetime.date.today()+datetime.timedelta(days=i)).strftime("%m-%d") for i in range(7)]
print(datelist)
c3 = datetime.date.today()+datetime.timedelta(days=4)
c4 = str(c3)
print(c4,type(c4))