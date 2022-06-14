import tkinter as tk
import LoginUI
from Judgecomputer import SerialNumber


class get_address(object):              # 根据电脑硬件信息来决定数据路径
    def __init__(self):
        laptop_address = 'C:\@Python学习\脚本\学员管理系统GUI版本\data'
        hp_address = 'F:\@@-个人通用\@@-Linux Shell学习\@Python学习\脚本\学员管理系统GUI版本\data'
        if SerialNumber().serialnumber != 'D936A':
            laptop_address = hp_address
        self.student_address = laptop_address + '\\student.data'
        self.systemuser_address = laptop_address + '\\systemuser.data'


class Window(tk.Tk):  # 定义电脑窗口类
    def __init__(self):
        super().__init__()  # 用于调用父类(超类)的一个方法，为什么之前没用过这个方法？
        self.title("学院管理系统")  # 定义本类的窗口名字
        self.geometry("680x350+400+200")  # 定义本类的窗口大小
        self.resizable(True, True)
        self.err_times = 0


if __name__ == '__main__':
    win = Window()  # 实例化一个窗口
    LoginUI.Login(win)
    win.mainloop()
