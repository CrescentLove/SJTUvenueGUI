# -*- coding = utf-8 -*-
# @TIME :2022/2/19 16:05
# @Author :CrescentLove
# @Software :PyCharm
import smtplib
from email.header import Header
from email.mime.text import MIMEText

import requests


class Mail(object):
    def __init__(self,mail_host,user,password,recr):

        self.mail_host = 'smtp.163.com'
        self.user = '15922132101'
        self.password = 'SUZATRCAGNESVOCH'
        self.sender = 'SJTU预定脚本@Crescentlove'
        self.recr = ['markdowndir@foxmail.com']
        self.miaoId = "tSe9OaP"
        self.text = ['预定失败', '预定成功']

    def mail2me(self, status):
        """
        :param status: 场地是否预定成功，1-->成功，0-->失败
        :return: 邮件是否发送成功，1-->成功，0-->失败
        """
        st_mail = 0
        try:
            smtpObj = smtplib.SMTP()
            # 连接到服务器
            smtpObj.connect(self.mail_host, 25)
            # 登录到服务器
            smtpObj.login(self.user, self.password)
            # 选择邮件内容
            mess = MIMEText(self.text[status], 'plain', 'utf-8')
            # 发送方信息
            mess['From'] = Header("预定脚本beta", 'utf-8')
            # # 接受方信息
            # mess['To'] = self.recr[0]
            # 邮件主题
            mess['Subject'] = '预定结果'
            # 发送
            smtpObj.sendmail(
                self.sender, self.recr, mess.as_string())
            # 退出
            smtpObj.quit()
            st_mail = 1

        except smtplib.SMTPException as e:
            print('errorMail', e)  # 打印错误

        return st_mail

    def miao(self, status):
        """

        :param status: 场地是否预定成功，1-->成功，0-->失败
        :return: 提醒是否发送成功，1-->成功，0-->失败
        """
        st_miao = 0
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                                ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 '
                                'Safari/537.36 Edg/98.0.1108.56'}
        miaoPage = requests.post("http://miaotixing.com/trigger?",
                                 headers=header, params={'id': 'tSe9OaP', 'text': self.text[status]}, )

        print(miaoPage.status_code)
        st_miao = 1
        # TODO:这里得改
