# -*- coding = utf-8 -*-
# @TIME :2022/2/24 15:20
# @Author :CrescentLove
# @Software :PyCharm

import tkinter as tk
from tkinter import ttk


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        # self.var0
        self.setup_widgets()

    def clickshouce(self):
        print(1)

    def clickyouxiang(self):
        self.widgets_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.widgets_frame.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew",rowspan=5)
        self.widgets_frame.columnconfigure(index=0, weight=1)


        self.entry = ttk.Entry(self.widgets_frame)
        self.entry.insert(0, "Entry")
        self.entry.grid(row=1, column=1, padx=5, pady=(0, 10), sticky="ew")

    def setup_widgets(self):
        # Create a Frame for the Checkbuttons

        self.menu_frame = ttk.LabelFrame(self, text="菜单", padding=(40, 10))
        self.menu_frame.grid(
            row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )

        # Menubuttons
        self.zhuye = ttk.Button(
            self.menu_frame, text="主页", style="Accent.TButton",command=self.clickyouxiang)
        self.zhuye.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

        self.changdi = ttk.Button(self.menu_frame, text="场地配置",command=self.clickyouxiang)
        self.changdi.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

        self.wangluo = ttk.Button(self.menu_frame, text="网络配置",command=self.clickyouxiang)
        self.wangluo.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

        self.youxiang = ttk.Button(self.menu_frame, text="邮件配置",command=self.clickyouxiang)
        self.youxiang.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")

        self.shouce = ttk.Button(self.menu_frame, text="使用手册", command=self.clickshouce)
        self.shouce.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")

        self.widgets_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.widgets_frame.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew")

        self.widgets_frame.columnconfigure(index=0, weight=1)
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
