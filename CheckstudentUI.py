import time
import tkinter as tk
import json
import MainUI
import GUI


class Check(object):
    def __init__(self, window):
        self.window = window
        self.frame = tk.Frame(self.window, borderwidth=1)
        self.frame.grid()
        self.but_chkall = tk.Button(self.frame, text='查询全部', relief='raised', command=self.showall)
        self.but_chkall.grid(row=0, column=0)
        # 创建动态变量
        self.sv_na = tk.StringVar()
        self.sv_nu = tk.StringVar()
        self.sv_gr = tk.StringVar()
        # 按名字查询
        self.ent_na = tk.Entry(self.frame, width=12, borderwidth=4, bg='#A9A9A9', textvariable=self.sv_na, validate="focusout",
                               validatecommand=self.input_check)
        self.ent_na.grid(row=1, column=0)
        self.ent_na.insert(0, '输入学员名字')             # 设置提示语
        self.ent_na.bind('<Button-1>', self.ent_na_clear)  # 单击鼠标左键，绑定ent_clear函数,点击鼠标的时候就清除提示
        self.but_chk_na = tk.Button(self.frame, text='按名字查询', relief='raised', command=self.showbyname)
        self.but_chk_na.grid(row=2, column=0)

        self.ent_nu = tk.Entry(self.frame, width=12, borderwidth=4, bg='#A9A9A9')
        self.ent_nu.grid(row=3, column=0)
        self.ent_nu.insert(0, '输入学员学号')  # 设置提示语
        self.ent_nu.bind('<Button-1>', self.ent_nu_clear)  # 单击鼠标左键，绑定ent_clear函数,点击鼠标的时候就清除提示
        self.but_chk_nu = tk.Button(self.frame, text='按学号查询', relief='raised', command=self.showbynum)
        self.but_chk_nu.grid(row=4, column=0)

        self.ent_gr = tk.Entry(self.frame, width=12, borderwidth=4, bg='#A9A9A9')
        self.ent_gr.grid(row=5, column=0)
        self.ent_gr.insert(0, '输入学员年级')  # 设置提示语
        self.ent_gr.bind('<Button-1>', self.ent_gr_clear)  # 单击鼠标左键，绑定ent_clear函数,点击鼠标的时候就清除提示
        self.but_chk_gr = tk.Button(self.frame, text='按年级查询', relief='raised', command=self.showbygrade)
        self.but_chk_gr.grid(row=6, column=0)

        self.but_back = tk.Button(self.frame, text='返回', relief='raised', command=self.go_back)
        self.but_back.grid(row=7, column=0)
        # 创建文本框
        self.text = tk.Text(self.frame, borderwidth=5, bg='#B0E0E6')
        self.text.grid(row=0, column=1, rowspan=9)

    def ent_na_clear(self, event):        # 加了event就不会报错，但是又没用到，不知道为啥？？？？？
        self.ent_na.delete(0, tk.END)

    def ent_nu_clear(self, event):        # 加了event就不会报错，但是又没用到，不知道为啥？？？？？
        self.ent_nu.delete(0, tk.END)

    def ent_gr_clear(self, event):        # 加了event就不会报错，但是又没用到，不知道为啥？？？？？
        self.ent_gr.delete(0, tk.END)

    def input_check(self):
        if self.ent_na.get() == '':   # 如果用户没有有输入，则返回非法，启用下一个函数invalidcommand
            return False
        else:
            return True

    def input(self):
        print('我被调用了')
        self.ent_na.insert(0, '输入学员名字')         # 恢复提示

    def showall(self):
        self.text.delete(0.0, tk.END)
        # 以读的形式打开文件
        f = open(GUI.get_address().student_address, 'r')
        # 把文件对象里的数据加载称为python对象
        content = json.load(f)
        # 加载出来后的数据是列表形式，还需要把列表里的字典的值提取出来，并作为参数创建Student实例
        f.close()
        for i in content:
            a = "名字:" + i['name'].center(8), "  学号:" + i['num'].zfill(4).center(8), "   年级:" + \
                i['grade'].center(8), " 性别:" + i['gender'].center(8)
            self.text.insert('insert', ''.join(str(''.join(a))) + '\n')  # 插入文本
            time.sleep(0.02)
            self.text.update()

    def showbyname(self):
        self.text.delete(0.0, tk.END)
        # 以读的形式打开文件
        f = open(GUI.get_address().student_address, 'r')
        # 把文件对象里的数据加载称为python对象
        content = json.load(f)
        # 加载出来后的数据是列表形式，还需要把列表里的字典的值提取出来，并作为参数创建Student实例
        f.close()
        name = self.ent_na.get()
        if name in [i['name'] for i in content]:        # 先判断这个人名存不存在
            for i in content:
                if name == i['name']:
                    a = "名字:" + i['name'].center(6), "  学号:" + i['num'].zfill(4).center(6), "   年级:" + \
                        i['grade'].center(6), " 性别:" + i['gender'].center(6)
                    self.text.insert('insert', ''.join(str(''.join(a))) + '\n')  # 插入文本
        else:
            self.text.insert('insert', '没找到相关学员')  # 插入文本

    def showbynum(self):
        self.text.delete(0.0, tk.END)
        # 以读的形式打开文件
        f = open(GUI.get_address().student_address, 'r')
        # 把文件对象里的数据加载称为python对象
        content = json.load(f)
        # 加载出来后的数据是列表形式，还需要把列表里的字典的值提取出来，并作为参数创建Student实例
        f.close()
        num = self.ent_nu.get()
        if num in [i['num'] for i in content]:        # 先判断这个人名存不存在
            for i in content:
                if num == i['num']:
                    a = "名字:" + i['name'].center(6), "  学号:" + i['num'].zfill(4).center(6), "   年级:" + \
                        i['grade'].center(6), " 性别:" + i['gender'].center(6)
                    self.text.insert('insert', ''.join(str(''.join(a))) + '\n')  # 插入文本
        else:
            self.text.insert('insert', '没找到相关学员')  # 插入文本

    def showbygrade(self):
        self.text.delete(0.0, tk.END)
        # 以读的形式打开文件
        f = open(GUI.get_address().student_address, 'r')
        # 把文件对象里的数据加载称为python对象
        content = json.load(f)
        # 加载出来后的数据是列表形式，还需要把列表里的字典的值提取出来，并作为参数创建Student实例
        f.close()
        grade = self.ent_gr.get()
        if grade in [i['grade'] for i in content]:        # 先判断这个人名存不存在
            for i in content:
                if grade == i['grade']:
                    a = "名字:" + i['name'].center(6), "  学号:" + i['num'].zfill(4).center(6), "   年级:" + \
                        i['grade'].center(6), " 性别:" + i['gender'].center(6)
                    self.text.insert('insert', ''.join(str(''.join(a))) + '\n')  # 插入文本
        else:
            self.text.insert('insert', '没找到相关学员')  # 插入文本

    def go_back(self):
        self.frame.destroy()
        MainUI.Main(self.window)
