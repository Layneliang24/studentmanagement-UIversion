import wmi
import os


class SerialNumber(object):
    def __init__(self):
        # wmi.WMI() 用于生成wmi实例
        w = wmi.WMI()

        # 获取主板序列号
        mb = w.Win32_BaseBoard()
        mb_sn = mb[0].SerialNumber
        if len(mb_sn) > 6:
            mb_sn = mb_sn[-5:]
        else:
            print("获取主板序列号失败")
            os._exit(0)
        # 把三个序列号连起来
        self.serialnumber = mb_sn


if __name__ == '__main__':
    print(SerialNumber().serialnumber)
