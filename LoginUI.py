import tkinter as tk
import tkinter.messagebox
import json
from RegisterUI import Register
import MainUI
import GUI


class Login(object):  # 创建登录页面
    def __init__(self, window):
        self.err_times = 0
        # 设置框架容器
        self.window = window
        self.frame = tk.Frame(self.window, borderwidth=1)
        self.frame.grid(padx=10, pady=10)
        # 创建标题标签
        self.lab1 = tk.Label(self.frame, width=31, height=2, text='学员管理系统', borderwidth=2,
                             font=('宋体', 20, 'bold italic'), anchor=tk.CENTER)
        self.lab1.grid(row=0, column=0, columnspan=5, rowspan=2)
        # 创建账号标签
        self.lab_name = tk.Label(self.frame, width=10, height=2, text='账号:', font=('宋体', 15, 'bold italic'),
                                 anchor=tk.E)
        self.lab_name.grid(row=2, column=0, rowspan=4, columnspan=2)
        # 创建账号输入框
        self.entry_name = tk.Entry(self.frame, width=30, validate='focusout')
        self.entry_name.grid(row=2, column=3, rowspan=4)
        # 创建密码标签
        self.lab_password = tk.Label(self.frame, width=10, height=2, text='密码:', font=('宋体', 15, 'bold italic'),
                                     anchor=tk.E)
        self.lab_password.grid(row=6, column=0, rowspan=4, columnspan=2)
        # 创建密码输入框
        self.entry_password = tk.Entry(self.frame, width=30, validate='focusout', show='*')
        self.entry_password.grid(row=6, column=3, rowspan=4)
        # 创建空白标签用于占位
        self.lab3 = tk.Label(self.frame)
        self.lab3.grid(row=12)
        # 创建动态变量
        self.sv_name = tk.StringVar()
        self.sv_password = tk.StringVar()
        self.entry_name['textvariable'] = self.sv_name
        self.entry_password['textvariable'] = self.sv_password
        # 创建登录按钮
        self.but1 = tk.Button(self.frame, width=10, height=2, text='登录', command=self.login_valid)
        self.but1.grid(row=13, column=1)
        # 创建取消按钮
        self.but2 = tk.Button(self.frame, width=10, height=2, text='取消', command=self.cancel)
        self.but2.grid(row=13, column=3)
        # 创建注册按钮
        self.but_reg = tk.Button(self.frame, text='没有账号？注册', command=self.register)
        self.but_reg.grid(row=18, column=4, columnspan=2, sticky='se')

    # 定义取消函数
    def cancel(self):
        self.sv_name.set('')
        self.sv_password.set('')

    # 检验用户账号和密码
    def login_valid(self):
        name = self.entry_name.get()
        password = self.entry_password.get()
        f = open(GUI.get_address().systemuser_address, 'r')
        user_list = json.load(f)
        if not name:  # 如果名字为空
            tk.messagebox.showerror(title='学员管理系统', message='请输入正确账号')
        elif not password:  # 如果密码为空
            tk.messagebox.showerror(title='学员管理系统', message='请输入密码')
        else:
            if name not in [i['name'] for i in user_list]:  # 先检查是否有这个用户
                tk.messagebox.showerror(title='学员管理系统', message='不存在此用户！')
            else:
                for i in user_list:
                    if name == i['name']:
                        if self.err_times == 3:  # 如果错误三次
                            tk.messagebox.showerror(title='学员管理系统', message='输入太频繁，请稍后重试')
                            self.frame.destroy()  # 强制退出
                            Login(self.window)
                        else:
                            if password == i['password']:
                                tk.messagebox.showinfo(title='学员管理系统', message=name + '您好, 欢迎使用学员管理系统')
                                self.frame.destroy()  # 销毁本窗口，加载下一个窗口，实现切换效果
                                MainUI.Main(self.window)  # 不用实例化类的对象先？？？？
                            else:
                                tk.messagebox.showerror(title='学员管理系统', message='密码错误！')
                                self.err_times += 1

    def register(self):  # 销毁当前界面去到注册界面
        self.frame.destroy()
        Register(self.window)


if __name__ == '__main__':
    pass
