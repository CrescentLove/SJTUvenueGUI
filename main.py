# -*- coding = utf-8 -*-
# @TIME :2022/2/24 15:20
# @Author :CrescentLove
# @Software :PyCharm
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
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

        self.setup_widgets()

    def clickshouce(self):
        os.system(r".\userBook.md")

    def clickyouxiang(self):
        self.mailPage = ttk.LabelFrame(self,text="配置区", padding=(0, 0, 0, 10), labelanchor="n")
        self.mailPage.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew")
        self.mailPage.columnconfigure(index=0, weight=1)

        self.hostname = ttk.Label(self.mailPage,text="Mail Host")
        self.hostname.grid(row=1, column=1, padx=5,pady=(0,10),sticky="ew")
        self.Mailentry1 = ttk.Entry(self.mailPage)
        self.Mailentry1.insert(0, 'smtp.163.com')
        self.Mailentry1.grid(row=1, column=2, padx=5, pady=(0, 10), sticky="ew")

        self.username = ttk.Label(self.mailPage, text="User Name")
        self.username.grid(row=2, column=1, padx=5, pady=(0, 10), sticky="ew")
        self.Mailentry2 = ttk.Entry(self.mailPage)
        self.Mailentry2.insert(0,"需邮箱账号")
        self.Mailentry2.grid(row=2, column=2, padx=5, pady=(0, 10), sticky="ew")

        self.password = ttk.Label(self.mailPage, text="Password")
        self.password.grid(row=3, column=1, padx=5, pady=(0, 10), sticky="ew")
        self.Mailentry3 = ttk.Entry(self.mailPage)
        self.Mailentry3.insert(0, '需授权码/非账户密码')
        self.Mailentry3.grid(row=3, column=2, padx=5, pady=(0, 10), sticky="ew")

        self.receiver = ttk.Label(self.mailPage, text="Receiver")
        self.receiver.grid(row=4, column=1, padx=5, pady=(0, 10), sticky="ew")
        self.Mailentry4 = ttk.Entry(self.mailPage)
        self.Mailentry4.insert(0, '需要发送提醒的邮箱')
        self.Mailentry4.grid(row=4, column=2, padx=5, pady=(0, 10), sticky="ew")

        self.mailPage2 = ttk.LabelFrame(self, text="试试这些", padding=(0, 0, 0, 10), labelanchor="n")
        self.mailPage2.grid(row=1, column=1, padx=10, pady=(30, 10), sticky="nsew")
        self.mailPage2.columnconfigure(index=0, weight=1)

        self.storeMail = ttk.Button(self.mailPage2, text="保存方案", style="Accent.TButton")
        self.storeMail.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

    def clickwangluo(self):
        self.netPage = ttk.LabelFrame(self,text="配置区", padding=(0, 0, 0, 10),labelanchor="n")
        self.netPage.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew")
        self.netPage.columnconfigure(index=0, weight=1)

        self.cookielogin = ttk.Label(self.netPage, text="登录Cookies")
        self.cookielogin.grid(row=1, column=1, padx=5, pady=(0, 10), sticky="ew")
        self.Netentry1 = ttk.Entry(self.netPage)
        self.Netentry1.insert(0, '复制登录时Cookies')
        self.Netentry1.grid(row=1, column=2, padx=5, pady=(0, 10), sticky="ew")

        self.cookieConfirm = ttk.Label(self.netPage, text="下单Cookies")
        self.cookieConfirm.grid(row=2, column=1, padx=5, pady=(0, 10), sticky="ew")
        self.Netentry2 = ttk.Entry(self.netPage)
        self.Netentry2.insert(0, '复制下单时Cookies')
        self.Netentry2.grid(row=2, column=2, padx=5, pady=(0, 10), sticky="ew")

        self.userAgent = ttk.Label(self.netPage, text="User Agent")
        self.userAgent.grid(row=3, column=1, padx=5, pady=(0, 10), sticky="ew")
        self.Netentry3 = ttk.Entry(self.netPage)
        self.Netentry3.insert(0, '复制任意请求时user-agent参数')
        self.Netentry3.grid(row=3, column=2, padx=5, pady=(0, 10), sticky="ew")

        self.netPage2 = ttk.LabelFrame(self, text="试试这些", padding=(0, 0, 0, 10), labelanchor="n")
        self.netPage2.grid(row=1, column=1, padx=10, pady=(30, 10), sticky="nsew")
        self.netPage2.columnconfigure(index=0, weight=1)

        self.storeNet = ttk.Button(self.netPage2, text="保存方案", style="Accent.TButton")
        self.storeNet.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

    def clickchangdi(self):
        self.venuePage = ttk.LabelFrame(self,text="配置区", padding=(0, 0, 0, 10),labelanchor="n")
        self.venuePage.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew",)
        self.venuePage.columnconfigure(index=0, weight=1)

        self.yundongming = ttk.Label(self.venuePage, text="体育项目")
        self.yundongming.grid(row=1, column=0, padx=5, pady=(0, 10), sticky="w")
        self.yundongmenu = ttk.OptionMenu(self.venuePage, self.var_4, *self.option_menu_list)
        self.yundongmenu.grid(row=1, column=1, padx=5, pady=10, sticky="w")

        self.changdiming = ttk.Label(self.venuePage, text="体育项目")
        self.changdiming.grid(row=2, column=0, padx=5, pady=(0, 10), sticky="w")
        self.changdimenu = ttk.OptionMenu(self.venuePage, self.var_5, *self.option_menu_listVenue)
        self.changdimenu.grid(row=2, column=1, padx=5, pady=10, sticky="w")

        self.timeming = ttk.Label(self.venuePage, text="期望时间")
        self.timeming.grid(row=3, column=0, padx=5, pady=(0, 10), sticky="w")
        self.timemenu = ttk.OptionMenu(self.venuePage, self.var_6, *self.option_menu_listTime)
        self.timemenu.grid(row=3, column=1, padx=5, pady=10, sticky="w")

        self.fieldming = ttk.Label(self.venuePage, text="期望场地")
        self.fieldming.grid(row=4, column=0, padx=5, pady=(0, 10), sticky="w")
        self.fieldmenu = ttk.OptionMenu(self.venuePage, self.var_7, *self.option_menu_listfield)
        self.fieldmenu.grid(row=4, column=1, padx=5, pady=10, sticky="w")

        self.configming = ttk.Label(self.venuePage, text="配置方案")
        self.configming.grid(row=5, column=0, padx=5, pady=(0, 10), sticky="w")
        self.configmenu = ttk.OptionMenu(self.venuePage, self.var_8, *self.option_menu_listconfig)
        self.configmenu.grid(row=5, column=1, padx=5, pady=10, sticky="w")
        # 设置选项区
        self.venuePage2 = ttk.LabelFrame(self, text="试试这些", padding=(0, 0, 0, 10), labelanchor="n")
        self.venuePage2.grid(row=1, column=1, padx=10, pady=(30, 10), sticky="nsew")
        self.venuePage2.columnconfigure(index=0, weight=1)


        self.storeVenue = ttk.Button(self.venuePage2, text="保存方案", style="Accent.TButton")
        self.storeVenue.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")





    def clickzhuye(self):
        self.rootPage = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.rootPage.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=5)
        self.rootPage.columnconfigure(index=0, weight=1)

        # 点击开始抢票！（会检查是否配置方案，网络，如果没有弹出警告框跳转，检查是否配置邮件，弹出建议配置）






    def setup_widgets(self):
        # Create a Frame for the Checkbuttons

        self.menu_frame = ttk.LabelFrame(self, text="菜单", padding=(40, 10),labelanchor="n")
        self.menu_frame.grid(
            row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )

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
        self.menu_frame2.grid(row=1, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")


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
        #         self.changci = ttk.Checkbutton(
        #             self.widgets_frame, text="场地"+str(i+1), style="Toggle.TButton"
        #         )
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
