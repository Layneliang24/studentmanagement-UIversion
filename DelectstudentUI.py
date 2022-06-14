import tkinter as tk
import json
import GUI
import tkinter.messagebox
from student import Student
import MainUI


class Delete(object):
    def __init__(self, window):
        self.window = window
        self.frame = tk.Frame(self.window, borderwidth=1)
        self.frame.pack()
        self.lab_num = tk.Label(self.frame, text='请输入学员学号：')
        self.lab_num.pack()
        self.sv_num = tk.StringVar()
        self.ent_num = tk.Entry(self.frame, textvariable=self.sv_num)
        self.ent_num.pack()
        self.but_num = tk.Button(self.frame, text='删除', command=self.delete)
        self.but_num.pack()
        self.but_bak = tk.Button(self.frame, text='返回', command=self.back)
        self.but_bak.pack()

    def delete(self):
        f = open(GUI.get_address().student_address, 'r')
        # 把文件对象里的数据加载称为python对象
        content = json.load(f)
        # 加载出来后的数据是列表形式，还需要把列表里的字典的值提取出来，并作为参数创建Student实例
        f.close()
        # 把加载后的数据转为对象
        student_list = [Student(i['name'], i['num'], i['grade'], i['gender']) for i in content]
        f.close()
        num = self.ent_num.get()
        if num in [i.num for i in student_list]:  # 先判断这个人名存不存在
            for i in student_list:
                if i.num == num:
                    student_list.remove(i)
                    tk.messagebox.showinfo(message='删除成功')
                    self.sv_num.set('')
        else:
            tk.messagebox.showerror(message='此学员不存在！')
            self.sv_num.set('')
        # 我们要以字典的形式[{s1},{s2},{s3}]保存学员信息，所以还要使用学员对象内置的__dict__属性，一个个提取学员的信息
        new_list = [i.__dict__ for i in student_list]
        # 使用dumps方法把对象转化为字符串，加入indent使写入的数据更加直观
        a = json.dumps(new_list, indent=1)
        # 以写入的方式打开文档。
        try:
            f = open(GUI.get_address().student_address, 'w')
            f.write(a)
            f.close()
        except:
            tk.messagebox.showerror(title='学院管理系统', message='未知错误，请联系管理员')

    def back(self):
        self.frame.destroy()
        MainUI.Main(self.window)
