"""
name:GymSeizor
date:2022-01-16
author:Crescentlove
description:气膜抢票程序，实现功能如下：
            1.整点抢预先设定场次√
            2.零碎时间设定优先级抢票
            3.成功/异常邮箱提醒功能√
            4.GUI界面
            5.可能的封装程序
"""
import random
import time

from CrescentRes.Mail import Mail
from CrescentRes.login import loGin
from CrescentRes.seizor import venSeizor

CONFIG = ['2022-3-2', 13, 4, 120000]


def selMode(Mode=1):
    if Mode == 1:
        # Wdate = str(input("日期：如2022-2-12"))
        # Wtime = int(input("时间段：x"))
        # Wsite = int(input("场地：x"))
        Wdate = CONFIG[0]
        Wtime = CONFIG[1]
        Wsite = CONFIG[2]
        Gtime = CONFIG[3]
        st_Buy = venSeizor().getOne(Wdate, Wtime, Wsite, Gtime)
        Mail().mail2me(status=st_Buy)

    if Mode == 2:
        # 待加多线程，json配置多选项场地时间信息
        # Wdate2 = str(input("日期：如2022-2-12"))
        # Wtime2 = int(input("时间段：x"))
        # Wsite2 = int(input("场地：x"))
        Wdate2 = CONFIG[0]
        Wtime2 = CONFIG[1]
        Wsite2 = CONFIG[2]
        while (1):
            sta = venSeizor().getwhich(Wdate2, Wtime2, Wsite2)
            if sta == 1:
                break
            time.sleep(random.randint(1, 60))


def main():
    loGin();
    selMode(Mode=2);

    # gymSeizor = venSeizor().getwhich(3,0)


if __name__ == '__main__':
    main()
