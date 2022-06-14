import tkinter as tk
import AddstudentUI
import LoginUI
import CheckstudentUI
import DelectstudentUI
import ModifystudentUI


class Main(object):  # 创建主界面
    def __init__(self, window):
        self.window = window
        self.frame = tk.Frame(self.window, borderwidth=1)
        self.frame.grid()
        self.label = tk.Label(self.frame, text='hello', font=('宋体', 30, 'bold italic'))
        self.label.grid(row=0, column=0)
        self.text = tk.Text(self.frame, )
        # 创建增加学员按钮
        self.but_add = tk.Button(self.frame, text='添加学员', command=self.go_add)
        self.but_add.grid(row=1, column=0)
        # 创建删除学员按钮
        self.but_dele = tk.Button(self.frame, text='删除学员', command=self.go_del)
        self.but_dele.grid(row=2, column=0)
        # 修改学员按钮
        self.but_mod = tk.Button(self.frame, text='修改学员', command=self.go_mod)
        self.but_mod.grid(row=3, column=0)
        # 查询学员按钮
        self.but_chk = tk.Button(self.frame, text='查询学员', command=self.go_chk)
        self.but_chk.grid(row=4, column=0)
        # 退出按钮
        self.but_out = tk.Button(self.frame, text='退出', command=self.go_login)
        self.but_out.grid(row=5, column=0)

    def go_login(self):
        self.frame.destroy()
        LoginUI.Login(self.window)

    def go_add(self):
        self.frame.destroy()
        AddstudentUI.Add(self.window)

    def go_chk(self):
        self.frame.destroy()
        CheckstudentUI.Check(self.window)

    def go_del(self):
        self.frame.destroy()
        DelectstudentUI.Delete(self.window)

    def go_mod(self):
        self.frame.destroy()
        ModifystudentUI.Modify(self.window)


if __name__ == '__main__':
    pass
