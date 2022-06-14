import tkinter as tk
import tkinter.messagebox
import json
from student import Student
import MainUI
import GUI


class Add(object):
    def __init__(self, window):
        self.window = window
        self.frame = tk.Frame(self.window, borderwidth=1)
        self.frame.pack()
        self.lab_name = tk.Label(self.frame, text='请输入姓名：')
        self.lab_name.pack()
        self.ent_name = tk.Entry(self.frame)
        self.ent_name.pack()
        self.lab_num = tk.Label(self.frame, text='请输入学号：')
        self.lab_num.pack()
        self.ent_num = tk.Entry(self.frame)
        self.ent_num.pack()
        self.lab_gra = tk.Label(self.frame, text='请输入年级：')
        self.lab_gra.pack()
        self.ent_gra = tk.Entry(self.frame)
        self.ent_gra.pack()
        self.lab_gen = tk.Label(self.frame, text='请输入性别：')
        self.lab_gen.pack()
        self.ent_gen = tk.Entry(self.frame)
        self.ent_gen.pack()
        self.but_sav = tk.Button(self.frame, text='保存', command=self.addstudent)
        self.but_sav.pack()
        self.but_can = tk.Button(self.frame, text='取消', command=self.cancel)
        self.but_can.pack()
        self.sv_name = tk.StringVar()
        self.sv_num = tk.StringVar()
        self.sv_gra = tk.StringVar()
        self.sv_gen = tk.StringVar()
        self.ent_name['textvariable'] = self.sv_name
        self.ent_num['textvariable'] = self.sv_num
        self.ent_gra['textvariable'] = self.sv_gra
        self.ent_gen['textvariable'] = self.sv_gen
        self.new_student_list = []
        self.load_student()

    def load_student(self):
        # 以读的形式打开文件
        f = open(GUI.get_address().student_address, 'r')
        # 把文件对象里的数据加载称为python对象
        content = json.load(f)
        # 加载出来后的数据是列表形式，还需要把列表里的字典的值提取出来，并作为参数创建Student实例
        self.new_student_list = [Student(i['name'], i['num'], i['grade'], i['gender']) for i in content]
        f.close()

    def addstudent(self):
        self.load_student()
        name = self.ent_name.get()
        num = self.ent_num.get()
        grade = self.ent_gra.get()
        gen = self.ent_gen.get()
        if num not in [i.num for i in self.new_student_list]:
            s = Student(name, num, grade, gen)
            self.new_student_list.append(s)
            # 我们要以字典的形式[{s1},{s2},{s3}]保存学员信息，所以还要使用学员对象内置的__dict__属性，一个个提取学员的信息
            new_list = [i.__dict__ for i in self.new_student_list]
            # 使用dumps方法把对象转化为字符串，加入indent使写入的数据更加直观
            a = json.dumps(new_list, indent=1)
            # 以写入的方式打开文档。
            try:
                f = open(GUI.get_address().student_address, 'w')
                f.write(a)
                f.close()
                tk.messagebox.showinfo(title='学院管理系统', message='新增用户成功')
            except:
                tk.messagebox.showerror(title='学院管理系统', message='未知错误，请联系管理员')
            self.frame.destroy()
            MainUI.Main(self.window)
        else:
            tk.messagebox.showerror(title='学员管理系统', message='此用户已存在！')
            self.frame.destroy()
            MainUI.Main(self.window)

    def cancel(self):
        self.sv_name.set('')
        self.sv_num.set('')
        self.sv_gra.set('')
        self.sv_gen.set('')
        self.frame.destroy()
        MainUI.Main(self.window)
