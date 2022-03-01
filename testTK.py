from tkinter import *
from tkinter import messagebox
# 测试用
root = Tk()
root.geometry('900x700')
root.title('计算机191班绩点计算小程序')
root.geometry('+400+200')

l1 = Label(text='高数(0-100)', bd=1, relief=SUNKEN, font=('楷体', 15))
l1.place(x=5, y=0)
l2 = Label(text='C++(0-100)', bd=1, relief=SUNKEN, font=('楷体', 15))
l2.place(x=5, y=50)
l3 = Label(text='英语(0-100)', bd=1, relief=SUNKEN, font=('楷体', 15))
l3.place(x=5, y=100)
l4 = Label(text='大学物理(0-100)', bd=1, relief=SUNKEN, font=('楷体', 15))
l4.place(x=5, y=150)
l5 = Label(text='线代(0-100)', bd=1, relief=SUNKEN, font=('楷体', 15))
l5.place(x=5, y=200)
l6 = Label(text='近代史(0-100)', bd=1, relief=SUNKEN, font=('楷体', 15))
l6.place(x=5, y=250)
l7 = Label(text='思修(0-100)', bd=1, relief=SUNKEN, font=('楷体', 15))
l7.place(x=5, y=300)
l8 = Label(text='形式与政策\n(优秀/良好/中等/及格）', bd=1, relief=SUNKEN, font=('楷体', 10))
l8.place(x=5, y=350)

e1 = Entry(root, bd=3)
e1.place(x=180, y=0)
e2 = Entry(root, bd=3)
e2.place(x=180, y=50)
e3 = Entry(root, bd=3)
e3.place(x=180, y=100)
e4 = Entry(root, bd=3)
e4.place(x=180, y=150)
e5 = Entry(root, bd=3)
e5.place(x=180, y=200)
e6 = Entry(root, bd=3)
e6.place(x=180, y=250)
e7 = Entry(root, bd=3)
e7.place(x=180, y=300)
e8 = Entry(root, bd=3)
e8.place(x=180, y=350)

ll1 = Label(text='4学分', bd=1, relief=SUNKEN, font=('楷体', 10))
ll1.place(x=355, y=0)
ll2 = Label(text='3学分', bd=1, relief=SUNKEN, font=('楷体', 10))
ll2.place(x=355, y=50)
ll3 = Label(text='3学分', bd=1, relief=SUNKEN, font=('楷体', 10))
ll3.place(x=355, y=100)
ll4 = Label(text='2.5学分', bd=1, relief=SUNKEN, font=('楷体', 10))
ll4.place(x=355, y=150)
ll5 = Label(text='3学分', bd=1, relief=SUNKEN, font=('楷体', 10))
ll5.place(x=355, y=200)
ll6 = Label(text='3学分', bd=1, relief=SUNKEN, font=('楷体', 10))
ll6.place(x=355, y=250)
ll7 = Label(text='3学分', bd=1, relief=SUNKEN, font=('楷体', 10))
ll7.place(x=355, y=300)
ll8 = Label(text='0.5学分', bd=1, relief=SUNKEN, font=('楷体', 10))
ll8.place(x=355, y=350)


def calculate():
    global gaoshu1
    global cpp1
    global yingyu1
    global daxuewuli1
    global xiandai1
    global jindaishi1
    global sixiu1
    global xingshiyuzhence1
    global zong
    global zong1
    var1 = e1.get()
    var2 = e2.get()
    var3 = e3.get()
    var4 = e4.get()
    var5 = e5.get()
    var6 = e6.get()
    var7 = e7.get()
    var8 = e8.get()
    if eval(var1) < 60:
        gaoshu1 = 0
    else:
        gaoshu1 = (eval(var1) - 50.0) / 10.0

    if eval(var2) < 60:
        cpp1 = 0
    else:
        cpp1 = (eval(var2) - 50.0) / 10.0

    if eval(var3) < 60:
        yingyu1 = 0
    else:
        yingyu1 = (eval(var3) - 50.0) / 10.0

    if eval(var4) < 60:
        daxuewuli1 = 0
    else:
        daxuewuli1 = (eval(var4) - 50.0) / 10.0
    if eval(var5) < 60:
        xiandai1 = 0
    else:
        xiandai1 = (eval(var5) - 50.0) / 10.0
    if eval(var6) < 60:
        jindaishi1 = 0
    else:
        jindaishi1 = (eval(var6) - 50.0) / 10.0
    if eval(var7) < 60:
        sixiu1 = 0
    else:
        sixiu1 = (eval(var7) - 50.0) / 10.0
    if var8 == '优秀':
        xingshiyuzhence1 = 4.0
    elif var8 == '良好':
        xingshiyuzhence1 = 3.0
    elif var8 == '中等':
        xingshiyuzhence1 = 2.0
    elif var8 == '及格':
        xingshiyuzhence1 = 1.0
    elif var8 == '不及格':
        xingshiyuzhence1 = 0

    messagebox.showwarning('提示', '计算完成，请点击输出按钮')
    zong = (
                   gaoshu1 * 4 + cpp1 * 3 + yingyu1 * 3 + daxuewuli1 * 2.5 + xiandai1 * 3 + jindaishi1 * 3 + sixiu1 * 3 + xingshiyuzhence1 * 0.5) / 22
    zong1 = round(zong, 3)


def print_result():
    t.insert('insert', '高数绩点：')
    t.insert('end', gaoshu1)
    t.insert('end', '\n\nc++:')
    t.insert('end', cpp1)
    t.insert('end', '\n\n英语绩点：')
    t.insert('end', yingyu1)
    t.insert('end', '\n\n大学物理绩点:')
    t.insert('end', daxuewuli1)
    t.insert('end', '\n\n线代绩点:')
    t.insert('end', xiandai1)
    t.insert('end', '\n\n近代史绩点:')
    t.insert('end', jindaishi1)
    t.insert('end', '\n\n思修绩点:')
    t.insert('end', sixiu1)
    t.insert('end', '\n\n形式与政策绩点:')
    t.insert('end', xingshiyuzhence1)
    t.insert('end', '\n\n总绩点：')
    t.insert('end', zong1)
    t.insert('end', '\n……………………………………\n')


button1 = Button(text='计算绩点', width=15, height=3, command=calculate, bd=4)
button1.place(x=30, y=400)

button2 = Button(text='输出结果', width=15, height=3, command=print_result, bd=4)
button2.place(x=180, y=400)


def cl():
    t.delete(0.0, 'end')
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    e5.delete(0, 'end')
    e6.delete(0, 'end')
    e7.delete(0, 'end')
    e8.delete(0, 'end')


button3 = Button(text='清空', width=15, height=3, command=cl, bd=4, fg='red')
button3.place(x=30, y=490)

t = Text(root, height=24, width=30, font=('黑体', 20))
t.place(x=410, y=0)

root.mainloop()
