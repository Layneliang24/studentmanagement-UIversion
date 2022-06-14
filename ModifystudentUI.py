import tkinter as tk
import json
from student import Student
import tkinter.messagebox
import MainUI
import GUI
import time


class Modify(object):
    def __init__(self, window):
        # 创建动态变量
        self.sv_nu1 = tk.StringVar()
        self.sv_na = tk.StringVar()
        self.sv_nu = tk.StringVar()
        self.sv_gr = tk.StringVar()
        # 创建窗口
        self.window = window
        self.frame = tk.Frame(self.window, borderwidth=1)
        self.frame.pack()
        # 先查找学员
        self.ent_nu1 = tk.Entry(self.frame, width=12, borderwidth=4, bg='#A9A9A9', textvariable=self.sv_nu1,
                                validate="focusout")
        self.ent_nu1.grid(row=0, column=0)
        self.ent_nu1.insert(0, '输入学员学号')  # 设置提示语
        self.ent_nu1.bind('<Button-1>', self.ent_nu1_clear)  # 单击鼠标左键，绑定ent_clear函数,点击鼠标的时候就清除提示
        self.but_chkall = tk.Button(self.frame, text='查找', relief='raised', command=self.get_student)
        self.but_chkall.grid(row=1, column=0)
        # 修改名字
        self.ent_na = tk.Entry(self.frame, width=12, borderwidth=4, bg='#A9A9A9', textvariable=self.sv_na,
                               validate="focusout")
        self.ent_na.grid(row=2, column=0)
        self.ent_na.insert(0, '输入学员名字')  # 设置提示语
        self.ent_na.bind('<Button-1>', self.ent_na_clear)  # 单击鼠标左键，绑定ent_clear函数,点击鼠标的时候就清除提示
        self.but_chk_na = tk.Button(self.frame, text='修改名字', relief='raised', command=self.mod_name)
        self.but_chk_na.grid(row=3, column=0)
        '''
        # 修改学号
        self.ent_nu = tk.Entry(self.frame, width=12, borderwidth=4, bg='#A9A9A9')
        self.ent_nu.grid(row=4, column=0)
        self.ent_nu.insert(0, '输入学员学号')  # 设置提示语
        self.ent_nu.bind('<Button-1>', self.ent_nu_clear)  # 单击鼠标左键，绑定ent_clear函数,点击鼠标的时候就清除提示
        self.but_chk_nu = tk.Button(self.frame, text='修改学号', relief='raised', command=self.mod_num)
        self.but_chk_nu.grid(row=5, column=0)
        '''
        # 修改年级
        self.ent_gr = tk.Entry(self.frame, width=12, borderwidth=4, bg='#A9A9A9')
        self.ent_gr.grid(row=6, column=0)
        self.ent_gr.insert(0, '输入学员年级')  # 设置提示语
        self.ent_gr.bind('<Button-1>', self.ent_gr_clear)  # 单击鼠标左键，绑定ent_clear函数,点击鼠标的时候就清除提示
        self.but_chk_gr = tk.Button(self.frame, text='修改年级', relief='raised', command=self.mod_grade)
        self.but_chk_gr.grid(row=7, column=0)
        # 创建返回按钮
        self.but_back = tk.Button(self.frame, text='返回', relief='raised', command=self.go_back)
        self.but_back.grid(row=8, column=0)
        # 创建文本框
        self.text = tk.Text(self.frame, borderwidth=5, bg='#B0E0E6')
        self.text.grid(row=0, column=1, rowspan=9)

    def load_student(self):
        # 以读的形式打开文件
        f = open(GUI.get_address().student_address, 'r')
        # 把文件对象里的数据加载称为python对象
        content = json.load(f)
        # 加载出来后的数据是列表形式，还需要把列表里的字典的值提取出来，并作为参数创建Student实例
        student_list = [Student(i['name'], i['num'], i['grade'], i['gender']) for i in content]
        f.close()
        return student_list

    def save_student(self, student):
        # 先加载原来的学生
        old_list = self.load_student()
        for i in old_list:
            if i.num == student.num:
                i.name = student.name
                i.grade = student.grade
                i.gender = student.gender
        new_list = [i.__dict__ for i in old_list]
        a = json.dumps(new_list, indent=1)
        # 以写入的方式打开文档。
        try:
            f = open(GUI.get_address().student_address, 'w')
            f.write(a)
            f.close()
        except:
            tk.messagebox.showerror(title='学院管理系统', message='未知错误，请联系管理员')

    def get_student(self):
        num = self.sv_nu1.get()
        new_student_list = self.load_student()
        if num in [i.num for i in new_student_list]:
            for i in new_student_list:
                if num == i.num:
                    self.text.delete(0.0, tk.END)
                    a = "名字:" + i.name.center(8), "  学号:" + i.num.zfill(4).center(8), "   年级:" + \
                        i.grade.center(8), " 性别:" + i.gender.center(8)
                    self.text.insert('insert', ''.join(str(''.join(a))) + '\n')  # 插入文本
                    time.sleep(0.02)
                    self.text.update()
                    return i
        else:
            tk.messagebox.showerror(message='此学员不存在！')

    def go_back(self):
        self.frame.destroy()
        MainUI.Main(self.window)

    def ent_nu1_clear(self, event):  # 加了event就不会报错，但是又没用到，不知道为啥？？？？？
        self.ent_nu1.delete(0, tk.END)

    def ent_na_clear(self, event):  # 加了event就不会报错，但是又没用到，不知道为啥？？？？？
        self.ent_na.delete(0, tk.END)

    def ent_gr_clear(self, event):  # 加了event就不会报错，但是又没用到，不知道为啥？？？？？
        self.ent_gr.delete(0, tk.END)

    def mod_name(self):
        student = self.get_student()
        if student:
            if self.ent_na.get() != '' and self.ent_na.get() != '输入学员名字':     # 如果有获取到学生和输入了名字
                student.name = self.ent_na.get()
                self.text.delete(0.0, tk.END)
                a = "名字:" + student.name.center(8), "  学号:" + student.num.zfill(4).center(8), "   年级:" + \
                    student.grade.center(8), " 性别:" + student.gender.center(8)
                self.text.insert('insert', ''.join(str(''.join(a))) + '\n')  # 插入文本
                time.sleep(0.02)
                self.text.update()
                self.save_student(student)
            else:
                tk.messagebox.showerror(message='请先输入名字')

    def mod_grade(self):
        student = self.get_student()
        if student:  # 如果有获取到学生
            if self.ent_gr.get() != '' and self.ent_gr.get() != '输入学员年级':
                student.grade = self.ent_gr.get()
                self.text.delete(0.0, tk.END)
                a = "名字:" + student.name.center(8), "  学号:" + student.num.zfill(4).center(8), "   年级:" + \
                    student.grade.center(8), " 性别:" + student.gender.center(8)
                self.text.insert('insert', ''.join(str(''.join(a))) + '\n')  # 插入文本
                time.sleep(0.02)
                self.text.update()
                self.save_student(student)
            else:
                tk.messagebox.showerror(message='请先输入年级')
