# -*- coding = utf-8 -*-
# @TIME :2022/2/24 15:20
# @Author :CrescentLove
# @Software :PyCharm
import datetime
import json
import os
import tkinter as tk
import tkinter.messagebox  # 这个是消息框，对话框的关键
from tkinter import ttk

# from tkinter import filedialog
from NewSeizor import Auto


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        # Make the app responsive
        self.recr = None
        self.passw = None
        self.user = None
        self.host = None
        self.usag = None
        self.bcoo = None
        self.lcoo = None
        self.field = None
        self.timeI = None
        self.venue = None
        self.sport = None
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1, )
            self.rowconfigure(index=index, weight=1)

        self.option_menu_list = ["", "羽毛球", "篮球"]
        self.var_4 = tk.StringVar(value=self.option_menu_list[1])
        self.option_menu_listVenue = ["", "气膜", "霍体"]
        self.var_5 = tk.StringVar(value=self.option_menu_listVenue[1])
        self.option_menu_listTime = ["", "07:00-08:00", "08:00-09:00", "09:00-10:00", "10:00-11:00", "11:00-12:00",
                                "12:00-13:00",
                                "13:00-14:00", "14:00-15:00", "15:00-16:00", "16:00-17:00", "17:00-18:00",
                                "18:00-19:00",
                                "19:00-20:00", "20:00-21:00", "21:00-22:00"]
        self.var_6 = tk.StringVar(value=self.option_menu_listTime[1])
        self.option_menu_listfield = ["", "全选", "场地1", "场地2", "场地3", "场地4", "场地5", "场地6", "场地7", "场地8", "场地9", "场地10", "场地11", "场地12"]
        self.var_7 = tk.StringVar(value=self.option_menu_listfield[1])
        self.option_menu_listconfig = ["", "方案1", "方案2", "方案3"]
        self.var_8 = tk.StringVar(value=self.option_menu_listconfig[1])
        self.datelist = [(datetime.date.today() + datetime.timedelta(days=i)).strftime("%m-%d") for i in range(8)]
        self.var_isam = tk.BooleanVar(value=True)
        self.var_tod = tk.BooleanVar(value=True)
        self.var_isfast = tk.BooleanVar(value=True)
        self.var_isfood = tk.BooleanVar(value=True)
        self.var_d1 = tk.StringVar()
        self.var_d2 = tk.StringVar()
        self.var_d3 = tk.StringVar()
        self.var_d4 = tk.StringVar()
        self.var_d5 = tk.StringVar()
        self.var_d6 = tk.StringVar()
        self.var_d7 = tk.StringVar()
        self.var_d8 = tk.StringVar()

        self.setup_widgets()

############################################################################
    def start(self):
        if not os.path.exists('mailConfig.json'):
            ismail = tkinter.messagebox.askokcancel('提示','是否配置邮箱?')
            if ismail:
                self.clickyouxiang()
        if not os.path.exists('venueConfig.json'):
            isven = tkinter.messagebox.showwarning('警告','请配置场地信息')
            self.clickchangdi()
        if not os.path.exists('venueConfig.json'):
            isven = tkinter.messagebox.showwarning('警告','请配置网络参数')
            self.clickwangluo()
        with open('venueConfig.json') as f:
            ve = json.loads(f.read())
            self.sport = ve['sport']
            self.venue = ve['venue']
            self.timeI = ve['time']
            self.field = ve['ci']

        with open('netConfig.json') as f:
            ve = json.loads(f.read())
            self.lcoo = ve['loginCookie']
            self.bcoo = ve['confirmCookie']
            self.usag = ve['userAgent']
        with open('mailConfig.json') as f:
            ve = json.loads(f.read())
            self.host = ve['host']
            self.user = ve['user']
            self.passw = ve['password']
            self.recr = ve['recr']
            a = self.var_d3
        print(self.var_d1.get().isalnum(), self.var_d2.get().isalnum(), self.var_d3.get())
        daylist = [self.var_d1.get(), self.var_d2.get(), self.var_d3.get(), self.var_d4.get(), self.var_d5.get(),
                   self.var_d6.get(), self.var_d7.get(), self.var_d8.get()]
        # 执行关键程序
        mainApp = Auto(self.var_isfast, self.isAm, self.var_isfood, self.isToday, daylist, self.sport, self.venue,
                       self.timeI, self.field, self.lcoo, self.bcoo, self.usag)
        mainApp.run()

        # 推出功能



####################################################################################################
    def delnet(self):
        self.Netentry1.delete(0,"end")
        self.Netentry2.delete(0, "end")
        self.Netentry3.delete(0, "end")
    def savenet(self):
        with open(file='netConfig.json',mode='w+',encoding='utf-8') as n:
            data = {"loginCookie":self.Netentry1.get(),"confirmCookie":self.Netentry2.get(),"userAgent":self.Netentry3.get()}
            json.dump(data, n)

    def delmail(self):
        self.Mailentry1.delete(0,"end")
        self.Mailentry2.delete(0, "end")
        self.Mailentry3.delete(0, "end")
        self.Mailentry4.delete(0, "end")
    def savemail(self):
        with open(file='mailConfig.json',mode='w+',encoding='utf-8') as n:
            data = {"host":self.Mailentry1.get(),"user":self.Mailentry2.get(),"password":self.Mailentry3.get(),"recr":self.Mailentry4.get()}
            json.dump(data, n)

    def saveven(self):
        with open(file='venueConfig.json',mode='w+',encoding='utf-8') as n:
            data = {"sport":self.var_4.get(),"venue":self.var_5.get(),"time":self.var_6.get(),"ci":self.var_7.get(),"proj":self.var_8.get()}
            json.dump(data, n)

#####################################################################################################
    def clickshouce(self):
        os.system(r".\userBook.md")

    def clickyouxiang(self):
        self.mailPage = ttk.LabelFrame(self, text="配置", padding=(10, 5), labelanchor="n")  # 修改按钮和边框宽度
        self.mailPage.grid(row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew")
        self.mailPage.columnconfigure(index=0, weight=1)

        self.hostname = ttk.Label(self.mailPage,text="Mail Host")
        self.hostname.grid(row=1, column=0, padx=5,pady=(0,10),sticky="ew")
        self.Mailentry1 = ttk.Entry(self.mailPage)
        self.Mailentry1.grid(row=1, column=1, padx=5, pady=(0, 10), sticky="ew")

        self.username = ttk.Label(self.mailPage, text="User Name")
        self.username.grid(row=2, column=0, padx=5, pady=(0, 10), sticky="ew")
        self.Mailentry2 = ttk.Entry(self.mailPage)
        self.Mailentry2.grid(row=2, column=1, padx=5, pady=(0, 10), sticky="ew")

        self.password = ttk.Label(self.mailPage, text="Password")
        self.password.grid(row=3, column=0, padx=5, pady=(0, 10), sticky="ew")
        self.Mailentry3 = ttk.Entry(self.mailPage,show='*')
        self.Mailentry3.grid(row=3, column=1, padx=5, pady=(0, 10), sticky="ew")

        self.receiver = ttk.Label(self.mailPage, text="Receiver")
        self.receiver.grid(row=4, column=0, padx=5, pady=(0, 10), sticky="ew")
        self.Mailentry4 = ttk.Entry(self.mailPage)
        self.Mailentry4.grid(row=4, column=1, padx=5, pady=(0, 10), sticky="ew")

        try:
            with open("mailConfig.json") as fmail:
                k = json.loads(fmail.read())

                self.Mailentry1.insert(0, k["host"])
                self.Mailentry2.insert(0, k["user"])
                self.Mailentry3.insert(0, k["password"])
                self.Mailentry4.insert(0,k["recr"])

        except Exception as e:
            print(e)
            self.Mailentry1.insert(0, '邮箱host/如smtp.163.com')
            self.Mailentry2.insert(0, '邮箱账号')
            self.Mailentry3.insert(0, '授权码,非登陆密码')
            self.Mailentry4.insert(0, '需要发送提醒的邮箱')

        self.qingkongM = ttk.Button(self.mailPage, text="清空", command=self.delmail)
        self.qingkongM.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")

        self.baocunM = ttk.Button(self.mailPage, text="保存", style="Accent.TButton", command=self.savemail)
        self.baocunM.grid(row=5, column=1, padx=5, pady=10, sticky="nsew")

    def clickwangluo(self):
        self.netPage = ttk.LabelFrame(self, text="配置", padding=(10, 5), labelanchor="n")  # 修改按钮和边框宽度
        self.netPage.grid(row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew")
        self.netPage.columnconfigure(index=0, weight=1)

        self.cookielogin = ttk.Label(self.netPage, text="登录Cookies")
        self.cookielogin.grid(row=1, column=0, padx=5, pady=(0, 10), sticky="ewsn")
        self.Netentry1 = ttk.Entry(self.netPage)
        # self.Netentry1.insert(0, '复制登录时Cookies')
        self.Netentry1.grid(row=1, column=1, padx=5, pady=(0, 10), sticky="ew")

        self.cookieConfirm = ttk.Label(self.netPage, text="下单Cookies")
        self.cookieConfirm.grid(row=2, column=0, padx=5, pady=(0, 10), sticky="ewsn")
        self.Netentry2 = ttk.Entry(self.netPage)
        # self.Netentry2.insert(0, '复制下单时Cookies')
        self.Netentry2.grid(row=2, column=1, padx=5, pady=(0, 10), sticky="ew")

        self.userAgent = ttk.Label(self.netPage, text="User Agent")
        self.userAgent.grid(row=3, column=0, padx=5, pady=(0, 10), sticky="ewsn")
        self.Netentry3 = ttk.Entry(self.netPage)
        # self.Netentry3.insert(0, '复制任意请求时user-agent参数')
        self.Netentry3.grid(row=3, column=1, padx=5, pady=(0, 10), sticky="ew")

        try:
            with open("netConfig.json") as fnet:
                k = json.loads(fnet.read())

                self.Netentry1.insert(0, k["loginCookie"])
                self.Netentry2.insert(0, k["confirmCookie"])
                self.Netentry3.insert(0, k["userAgent"])

        except Exception as e:
            print(e)
            self.Netentry1.insert(0, '复制登录时Cookies')
            self.Netentry2.insert(0, '复制下单时Cookies')
            self.Netentry3.insert(0, '复制任意请求时user-agent参数')

        self.qingkongN = ttk.Button(self.netPage, text="清空", command=self.delnet)
        self.qingkongN.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")

        self.baocunN = ttk.Button(self.netPage, text="保存",style="Accent.TButton", command=self.savenet)
        self.baocunN.grid(row=4, column=1, padx=5, pady=10, sticky="nsew")




        # self.netPage2 = ttk.LabelFrame(self, text="试试这些", padding=(0, 0, 0, 10), labelanchor="n")
        # self.netPage2.grid(row=1, column=1, padx=10, pady=(5, 10), sticky="nsew")
        # self.netPage2.columnconfigure(index=0, weight=1)
        #
        # self.storeNet = ttk.Button(self.netPage2, text="保存方案", style="Accent.TButton")
        # self.storeNet.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

    def clickchangdi(self):
        try:
            with open("venueConfig.json") as fven:
                k = json.loads(fven.read())
                self.var_4 = tk.StringVar(value=k["sport"])
                self.var_5 = tk.StringVar(value=k["venue"])
                self.var_6 = tk.StringVar(value=k["time"])
                self.var_7 = tk.StringVar(value=k["ci"])
                self.var_8 = tk.StringVar(value=k["proj"])
        except Exception as e:
            print(e)

        self.venuePage = ttk.LabelFrame(self, text="配置", padding=(10, 5), labelanchor="n")  # 修改按钮和边框宽度
        self.venuePage.grid(row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew")
        self.venuePage.columnconfigure(index=0, weight=1)

        self.yundongming = ttk.Label(self.venuePage, text="体育项目")
        self.yundongming.grid(row=1, column=0, padx=5, pady=(0, 10), sticky="ewsn")
        self.yundongmenu = ttk.OptionMenu(self.venuePage, self.var_4, *self.option_menu_list)
        self.yundongmenu.grid(row=1, column=1, padx=5, pady=(0, 10), sticky="w"+"n"+"s"+"e")

        self.changdiming = ttk.Label(self.venuePage, text="体育场馆")
        self.changdiming.grid(row=2, column=0, padx=5, pady=(0, 10), sticky="ewsn")
        self.changdimenu = ttk.OptionMenu(self.venuePage, self.var_5, *self.option_menu_listVenue)
        self.changdimenu.grid(row=2, column=1, padx=5, pady=(0, 10), sticky="w"+"n"+"s"+"e")

        self.timeming = ttk.Label(self.venuePage, text="期望时间")
        self.timeming.grid(row=3, column=0, padx=5, pady=(0, 10), sticky="ewsn")
        self.timemenu = ttk.OptionMenu(self.venuePage, self.var_6, *self.option_menu_listTime)
        self.timemenu.grid(row=3, column=1, padx=5, pady=(0, 10), sticky="w"+"n"+"s"+"e")

        self.fieldming = ttk.Label(self.venuePage, text="期望场地")
        self.fieldming.grid(row=4, column=0, padx=5, pady=(0, 10), sticky="ewsn")
        self.fieldmenu = ttk.OptionMenu(self.venuePage, self.var_7, *self.option_menu_listfield)
        self.fieldmenu.grid(row=4, column=1, padx=5, pady=(0, 10), sticky="w"+"n"+"s"+"e")

        self.configming = ttk.Label(self.venuePage, text="配置方案")
        self.configming.grid(row=5, column=0, padx=5, pady=(0, 10), sticky="ewsn")
        self.configmenu = ttk.OptionMenu(self.venuePage, self.var_8, *self.option_menu_listconfig)
        self.configmenu.grid(row=5, column=1, padx=5, pady=(0, 10), sticky="w"+"n"+"s"+"e")

        self.baocunV = ttk.Button(self.venuePage, text="保存", style="Accent.TButton", command=self.saveven)
        self.baocunV.grid(row=6, column=0, padx=5, pady=10, sticky="nsew",columnspan=3)


        # 设置选项区
        # self.venuePage2 = ttk.LabelFrame(self, text="试试这些", padding=(0, 0, 0, 10), labelanchor="n")
        # self.venuePage2.grid(row=1, column=1, padx=10, pady=(5, 10), sticky="nsew")
        # self.venuePage2.columnconfigure(index=0, weight=1)
        #
        #
        # self.storeVenue = ttk.Button(self.venuePage2, text="保存方案", style="Accent.TButton")
        # self.storeVenue.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

    def clickzhuye(self):
        self.rootPage = ttk.LabelFrame(self, text="菜单", padding=(10, 5), labelanchor="n")  # 修改按钮和边框宽度
        self.rootPage.grid(row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew")
        self.rootPage.columnconfigure(index=0, weight=1)

        self.isAm = ttk.Checkbutton(self.rootPage, text="不抢上午",style="Switch.TCheckbutton", variable=self.var_isam)
        self.isAm.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

        self.isToday = ttk.Checkbutton(self.rootPage, text="不抢今日",style="Switch.TCheckbutton", variable=self.var_tod)
        self.isToday.grid(row=1, column=2, padx=5, pady=10, sticky="nsew")

        self.isAm = ttk.Checkbutton(self.rootPage, text="不抢饭点", style="Switch.TCheckbutton", variable=self.var_isfood)
        self.isAm.grid(row=1, column=1, padx=5, pady=10, sticky="nsew")

        self.isAm = ttk.Checkbutton(self.rootPage, text="慢速防挂", style="Switch.TCheckbutton", variable=self.var_isfast)
        self.isAm.grid(row=1, column=3, padx=5, pady=10, sticky="nsew")

        self.d1 = ttk.Checkbutton(self.rootPage, text=self.datelist[0], style="Toggle.TButton",variable=self.var_d1)
        self.d1.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
        self.d2 = ttk.Checkbutton(self.rootPage, text=self.datelist[1], style="Toggle.TButton", variable=self.var_d2)
        self.d2.grid(row=2, column=1, padx=5, pady=10, sticky="nsew")
        self.d3 = ttk.Checkbutton(self.rootPage, text=self.datelist[2], style="Toggle.TButton", variable=self.var_d3)
        self.d3.grid(row=2, column=2, padx=5, pady=10, sticky="nsew")
        self.d4 = ttk.Checkbutton(self.rootPage, text=self.datelist[3], style="Toggle.TButton", variable=self.var_d4)
        self.d4.grid(row=2, column=3, padx=5, pady=10, sticky="nsew")
        self.d5 = ttk.Checkbutton(self.rootPage, text=self.datelist[4], style="Toggle.TButton", variable=self.var_d5)
        self.d5.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")
        self.d6 = ttk.Checkbutton(self.rootPage, text=self.datelist[5], style="Toggle.TButton", variable=self.var_d6)
        self.d6.grid(row=3, column=1, padx=5, pady=10, sticky="nsew")
        self.d7 = ttk.Checkbutton(self.rootPage, text=self.datelist[6], style="Toggle.TButton", variable=self.var_d7)
        self.d7.grid(row=3, column=2, padx=5, pady=10, sticky="nsew")
        self.d8 = ttk.Checkbutton(self.rootPage, text=self.datelist[7], style="Toggle.TButton", variable=self.var_d8)
        self.d8.grid(row=3, column=3, padx=5, pady=10, sticky="nsew")

        self.switch = ttk.Button(self.rootPage, text="START", command=self.start)
        self.switch.grid(row=4, column=0, padx=5, pady=10, sticky="nsew", columnspan=4)

        # self.menu_frame2 = ttk.LabelFrame(self, text="About", padding=(40, 10), labelanchor="n")
        # self.menu_frame2.grid(row=1, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew", columnspan=4)
        # 点击开始抢票！（会检查是否配置方案，网络，如果没有弹出警告框跳转，检查是否配置邮件，弹出建议配置）

    def setup_widgets(self):
        # Create a Frame for the Checkbuttons

        self.menu_frame = ttk.LabelFrame(self, text="菜单", padding=(10, 5),labelanchor="n") # 修改按钮和边框宽度
        self.menu_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

        # Menubuttons
        self.zhuye = ttk.Button(
            self.menu_frame, text="主页", style="Accent.TButton",command=self.clickzhuye)
        self.zhuye.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

        self.changdi = ttk.Button(self.menu_frame, text="场地配置",command=self.clickchangdi)
        self.changdi.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

        self.wangluo = ttk.Button(self.menu_frame, text="网络配置",command=self.clickwangluo)
        self.wangluo.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

        self.youxiang = ttk.Button(self.menu_frame, text="邮件配置",command=self.clickyouxiang)
        self.youxiang.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")

        self.shouce = ttk.Button(self.menu_frame, text="使用手册", command=self.clickshouce)
        self.shouce.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")


        self.menu_frame2 = ttk.LabelFrame(self, text="About", padding=(40, 10),labelanchor="n")
        self.menu_frame2.grid(row=1, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew",columnspan=4)

        self.mailA = ttk.Label(self.menu_frame2, text="Mail: markdowndir@foxmail.com", padding=(40, 10))
        self.mailA.grid(row=1, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew", columnspan=4)

        self.rootPage = ttk.LabelFrame(self, text="菜单", padding=(10, 5), labelanchor="n")  # 修改按钮和边框宽度
        self.rootPage.grid(row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="nsew")
        self.rootPage.columnconfigure(index=0, weight=1)

        self.isAm = ttk.Checkbutton(self.rootPage, text="不抢上午", style="Switch.TCheckbutton", variable=self.var_isam)
        self.isAm.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

        self.isToday = ttk.Checkbutton(self.rootPage, text="不抢今日", style="Switch.TCheckbutton", variable=self.var_tod)
        self.isToday.grid(row=1, column=2, padx=5, pady=10, sticky="nsew")

        self.isAm = ttk.Checkbutton(self.rootPage, text="不抢饭点", style="Switch.TCheckbutton", variable=self.var_isfood)
        self.isAm.grid(row=1, column=1, padx=5, pady=10, sticky="nsew")

        self.isAm = ttk.Checkbutton(self.rootPage, text="慢速防挂", style="Switch.TCheckbutton", variable=self.var_isfast)
        self.isAm.grid(row=1, column=3, padx=5, pady=10, sticky="nsew")

        self.d1 = ttk.Checkbutton(self.rootPage, text=self.datelist[0], style="Toggle.TButton", variable=self.var_d1)
        self.d1.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
        self.d2 = ttk.Checkbutton(self.rootPage, text=self.datelist[1], style="Toggle.TButton", variable=self.var_d2)
        self.d2.grid(row=2, column=1, padx=5, pady=10, sticky="nsew")
        self.d3 = ttk.Checkbutton(self.rootPage, text=self.datelist[2], style="Toggle.TButton", variable=self.var_d3)
        self.d3.grid(row=2, column=2, padx=5, pady=10, sticky="nsew")
        self.d4 = ttk.Checkbutton(self.rootPage, text=self.datelist[3], style="Toggle.TButton", variable=self.var_d4)
        self.d4.grid(row=2, column=3, padx=5, pady=10, sticky="nsew")
        self.d5 = ttk.Checkbutton(self.rootPage, text=self.datelist[4], style="Toggle.TButton", variable=self.var_d5)
        self.d5.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")
        self.d6 = ttk.Checkbutton(self.rootPage, text=self.datelist[5], style="Toggle.TButton", variable=self.var_d6)
        self.d6.grid(row=3, column=1, padx=5, pady=10, sticky="nsew")
        self.d7 = ttk.Checkbutton(self.rootPage, text=self.datelist[6], style="Toggle.TButton", variable=self.var_d7)
        self.d7.grid(row=3, column=2, padx=5, pady=10, sticky="nsew")
        self.d8 = ttk.Checkbutton(self.rootPage, text=self.datelist[7], style="Toggle.TButton", variable=self.var_d8)
        self.d8.grid(row=3, column=3, padx=5, pady=10, sticky="nsew")

        self.switch = ttk.Button(self.rootPage, text="START", command=self.start)
        self.switch.grid(row=4, column=0, padx=5, pady=10, sticky="nsew", columnspan=4)
        # fd = filedialog.LoadFileDialog(self.menu_frame2)  # 创建打开文件对话框
        # filename = fd.go()  # 显示打开文件对话框，并获取选择的文件名称
        # filedialog.Open(filename)

        # self.labelmail = ttk.Label(
        #     self.menu_frame2,
        #     image=tk.PhotoImage(file='./res/mail.png'),
        # )
        # self.labelmail.grid(row=1, column=0, pady=10)
        # self.labelgit = ttk.Label(
        #     self.menu_frame2,
        #     text="github",
        #     anchor='ne'
        # )
        # self.labelgit.grid(row=2, column=0, pady=10)
        #
        # for j in range(15):
        #     for i in range(12):
        #         self.changci = ttk.Checkbutton(self.widgets_frame, text="场地"+str(i+1), style="Toggle.TButton")
        #         self.changci.grid(row=j+1, column=i, padx=5, pady=10, sticky="nsew")


if __name__ == "__main__":
    root = tk.Tk()  # 创建tk对象
    root.title("气膜爷来了")
    root.tk.call("source", "sun-valley.tcl")    # 设置主题sun-valley
    root.tk.call("set_theme", "dark")

    # 设置主窗口组件，设置pack填充方式
    app = App(root)
    app.pack(fill="both", expand=True)

    # 设置居中
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))


    root.mainloop()
