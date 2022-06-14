import tkinter as tk
import tkinter.messagebox
import json
from systemuser import Systemuser
import LoginUI
import GUI


class Register(object):  # 创建用户注册界面
    def __init__(self, window):
        self.window = window
        self.frame = tk.Frame(self.window, borderwidth=1)
        self.frame.grid(padx=10, pady=10)
        self.lab_name = tk.Label(self.frame, text='请输入用户名')
        self.lab_password = tk.Label(self.frame, text='请输入密码：')
        self.lab_password2 = tk.Label(self.frame, text='请再次输入密码：')
        self.entry_name = tk.Entry(self.frame)
        self.entry_password = tk.Entry(self.frame)
        self.entry_password2 = tk.Entry(self.frame)
        self.lab_name.grid(row=0, column=0)
        self.entry_name.grid(row=0, column=1)
        self.lab_password.grid(row=1, column=0)
        self.entry_password.grid(row=1, column=1)
        self.lab_password2.grid(row=2, column=0)
        self.entry_password2.grid(row=2, column=1)
        self.but_save = tk.Button(self.frame, text='保存', command=self.save_user)
        self.but_cancel = tk.Button(self.frame, text='取消', command=self.cancel)
        self.but_save.grid(row=3, column=0)
        self.but_cancel.grid(row=3, column=1)

        # 设置动态变量
        self.sv_name = tk.StringVar()
        self.sv_password = tk.StringVar()
        self.sv_password2 = tk.StringVar()
        self.entry_name['textvariable'] = self.sv_name
        self.entry_password['textvariable'] = self.sv_password
        self.entry_password2['textvariable'] = self.sv_password2

        # 初始化的时候就加载用户文件里的用户
        self.new_user_list = []
        self.load()

    def load(self):
        # 以读的形式打开文件
        f = open(GUI.get_address().systemuser_address, 'r')
        # 把文件对象里的数据加载称为python对象
        content = json.load(f)
        # 加载出来后的数据是列表形式，还需要把列表里的字典的值提取出来，并作为参数创建Student实例
        self.new_user_list = [Systemuser(i['name'], i['password']) for i in content]
        f.close()

    def save_user(self):
        self.load()
        name = self.entry_name.get()
        password = self.entry_password.get()
        password2 = self.entry_password2.get()
        if name not in [i.name for i in self.new_user_list]:
            if password == password2:
                s = Systemuser(name, password)
                self.new_user_list.append(s)
                # 我们要以字典的形式[{s1},{s2},{s3}]保存学员信息，所以还要使用学员对象内置的__dict__属性，一个个提取学员的信息
                new_list = [i.__dict__ for i in self.new_user_list]
                # 使用dumps方法把对象转化为字符串，加入indent使写入的数据更加直观
                a = json.dumps(new_list, indent=1)
                # 以写入的方式打开文档。
                try:
                    f = open(GUI.get_address().systemuser_address, 'w')
                    f.write(a)
                    f.close()
                    tk.messagebox.showinfo(title='学员管理系统', message='用户注册成功')
                    self.frame.destroy()
                    LoginUI.Login(self.window)
                except:
                    tk.messagebox.showerror(title='学员管理系统', message='未知错误，请联系管理员')
                    self.frame.destroy()
                    Register(self.window)
            else:
                tk.messagebox.showerror(title='学院管理系统', message='密码不一致！请重试')
                self.sv_password.set('')
                self.sv_password2.set('')
        else:
            tk.messagebox.showerror(title='学员管理系统', message='此用户已存在！')
            self.frame.destroy()
            LoginUI.Login(self.window)

    def cancel(self):
        self.frame.destroy()
        LoginUI.Login(self.window)
        # 为避免循环调用circular import错误，需要导入整个模块，from LoginUI import Login会出错，为啥？？？？


if __name__ == '__main__':
    pass
