# -*- coding = utf-8 -*-
# @TIME :2022/2/25 19:18
# @Author :CrescentLove
# @Software :PyCharm
import datetime

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

    def sta(self):
        loGin(self.usag)
        print()
        timeN = int(datetime.datetime.now().strftime("%H%M"))
        Wtimen = self.__List2RealTime.index(self.timeI)
        Wsiten = self.__List2RealSite.index(self.field)
        print(self.dlist, '\n', Wtimen, Wsiten, self.slow, self.noam, self.noeat)
        seizor = venSeizor(self.lcoo, self.bcoo, self.usag, self.sport, self.venue)
        st_B = 0
        while 1:
            if timeN < 1150:
                for i in range(6, -1, -1):
                    if i == 0 and self.notod:
                        continue
                    if self.dlist[i] == '1':
                        print(self.dlist[i])
                        st_B += seizor.getwhich(self.datelist[i], Wtimen, Wsiten, self.noam, self.noeat)
                        print(st_B)
            else:
                if timeN < 1201:
                    st_B += seizor.getOne(self.datelist[6], Wtimen, Wsiten)
                for i in range(7, -1, -1):
                    if i == 0 and self.notod:
                        continue
                    if self.dlist[i] == '1':
                        print(self.dlist[i], '--下午巡航场地')
                        st_B += seizor.getwhich(self.datelist[i], Wtimen, Wsiten, self.noam, self.noeat)
#
#
# if __name__ == '__main__':
#     bcoo = "_ga=GA1.3.1895526322.1645009080; NSC_wt_tqpsut.tkuv.fev.do_2020=ffffffff097f1cec45525d5f4f58455e445a4a4229a0; rememberMe=1Q9+5BqJn6B1Z3NfIeS5WkyMPFdJC6gOsMCevAEoHei/mPV+fOa94pvS+NnV1mkKH1/zDCn5ZbP1Rpu6ksyeiH7s2DbIO0ZDQ6s4AZUXk3u0dVdCCWx7gYt52eKedx/wGHf8yL5GS1PESvpdet1D/vwuvw+6b9tfavj7atSmyAYs715DeWRBO9FZAUgpIR/DG5428Uj7nHwG1Ke4JvFS0TCtvlLZNtt9R2sYX25c7AV/bKTVzp0aMDzhsKn0+EnC8eT4yaXXW4bGxjmZOUVlZ7Kov5WRKng6Trkn2Qi3NXLePJ4nX+16c0X/Yg6QZGdEtDaRbYC+BzQ9Xx2MA0XJHUoFBfE6gtQQfFab4c3e7T5J+492EWChbwyVWO6WVvYqb73NvHm/33HIbWvi5O4hI7dcpewZx1dF0Oo9mo80fgMp/+butLW6ApufzuvO17ZHkvLe+f6ezoopQlH11gacI1PfezkcZ/ap78RtovVw94gNI3rC98k42vchwyEMM/s9VYtovr59Iyxm7+JnHt4fA4rPznl9rb9opLPvAfh5GHkQfoLyQLP/UWB1gSPvr3ySZPKEUQKUWmZrLrCfjesdp8yhKaJ3pQjvWTv1RVsf5CNAJ7v8xklR20Z0ch/aOiTbwShg7T7HCehDpuojrUmnpLXvPaPKu/8Akq1YkC4MAxku0eAaQMGvheOy6p4AwLmBFfTjpKiMaP+rpmpmS3tTJAgfMzME0AsZ7edcpWDmWqlwVFpF/0qhN/dtbYxJDbPWPzoD4TvTjUQ4h8QoNpNPodvdMW8GojptpGzbHabw1IQgtaw/2kt/cBrmhDYkCAjfQMv2dNsx16fLAdWlxCVWHSTJrXBL6hIwwIhIa2VUZZOseKYkOGrSLj9IZje6J280ulszdgtouGUvDLTHdiwcUa3qezZaWuVhNmW0MXshTN4IBm5c5IeDhzRtYYZadPhhVK2ANLIwpSBCFK12xkhQj5efmkyCvlRFlMIH8OJOM7ljHUYHKf6knS91r0jTF8XN2dYkIJIY67Sb6oNTsfUN2Cu6qpJJeh+f3Rtw4iJ1fb4vF6Lk0hIoXs9lBHr0JC1Iubo864XJ0PQB0TG8kA4oOyGjVcougXe7XtgEyuI5isv+D4rAr5cG/zGw6HZh/5MsqyyqgY+IYF0XFHBUV99MDKrNF14FXsQAp3SCMrOB3H07Q9cIDPZqr2565Vo4pWW2x6qALByzkJD8Xa0vyPkyTS9H8WEYUr8o7AIax8h+TlFmXE+EHNLJGCvQSibJltPS2Gypk8UWWmnA6vaSv6Q6dS6jJcBeK9i7YyNGgswiBtSz/NhDnc+kiSOjqRTryi/xLvoPgc1IxSVP31TMoX8QTroIbN/0Z2Kj+NLmYdeDbjDXXsBQ4aTwdRtif6SkkdQKzAMNynFT7OzlL3w7QmHo3Og/zjSIgx5h7nHgcZWDoXcF7RhSVqU98GsDkjeMsHHXUVfwW/4M3sDxKq48fsAZwap4ADLQM4OMFSvOxlMe9WZezWcNMg1rVML6w9qNHA1odv4sIzOKhVzV6UM+Aisdz+55eLjFARcf4Uv25iHzxxaFeWoHxV+5107RjbsJSiSeacloX19jzAmG2MGuIzW/rSCQrIvciXMTnsA/TrjGhsrIPuHPitsMcXpNlnyqKZV2pOfa/gbyDxlW2lrEi+DetvL+w6mGmeRizlM4aJQKR15ggOB3Hv6OfszE9OjoHgSnPF9p/+y10ZVm1jlUjrJ64SjEV/uZvJBabTvRfk3+8PxmsTn4W0qk56sLw8x2350NzUmfz3g7zs20QFXrPlyvGSxaoaKohsxEFqRgAtxiM53paX1ywP4RTGGZnNMb9NKIT/uc7TckXwAThq+sHZbffckyjCtcxN6f2dLV3YAdYbN8UFpU5Av63k+vC4yJAb4xMGdGtAp9mwdddujguGo/IirCrzIziUPXn23M+zRI2MoVjfW4GydWx+GwJrMjAQsShhBcLYWnYLfFDsH0TaDl8yTN1K23WSNuPltydEGGk9IBrrReuceLkO00obw1TuaM23HdtLIm2fdhRqnNEvWh4w==; JSESSIONID=40744859-e149-41e3-9447-5a7d91cc49f9"
#     a = Auto(True, True, True, True, bcoo, )
