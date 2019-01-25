import serial
import time
import threading
from tkinter import *
from tkinter.ttk import Button
from tkinter import messagebox


class SerialLockControl:
    def __init__(self, board1, board2, serial_name, port=9600):

        self.board1 = board1
        self.board2 = board2
        self.B1 = ''
        self.B2 = ''
        self.lock_sta = []
        self.BOARD1 = [int(board1), 242, 85]
        self.BOARD2 = [int(board2), 242, 85]
        self.BOARD1LIGHT = [int(board1), 245, 85]
        self.lock_number = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09,
                            0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10, 0x11, 0x12, 0x13, 0x14]
        try:
            self.ser = serial.Serial(serial_name, port)
        except Exception as e:
            messagebox.showerror("ERROR", e)
        t = threading.Thread(target=self.get_lock_status)
        t.setDaemon(True)
        t.start()
        self.window = Tk()
        self.ui()

    def ui(self):
        self.window.title("锁控测试程序")

        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        x = int((ws / 2) - (300 / 2))
        y = int((hs / 2) - (300 / 2))
        self.window.geometry("{}x{}+{}+{}".format(500, 300, x, y))
        self.window.resizable(0, 0)
        self.v = StringVar()
        self.v.set("关闭")

        Button(self.window, text="1号锁", command=lambda: self.open_lock(1)).grid(ipadx=10, row=1, column=1)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=1, column=2)
        Button(self.window, text="2号锁", command=lambda: self.open_lock(2)).grid(ipadx=10, row=1, column=3)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=1, column=4)
        Button(self.window, text="3号锁", command=lambda: self.open_lock(3)).grid(ipadx=10, row=1, column=5)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=1, column=6)
        Button(self.window, text="4号锁", command=lambda: self.open_lock(4)).grid(ipadx=10, row=2, column=1)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=2, column=2)
        Button(self.window, text="5号锁", command=lambda: self.open_lock(5)).grid(ipadx=10, row=2, column=3)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=2, column=4)
        Button(self.window, text="6号锁", command=lambda: self.open_lock(6)).grid(ipadx=10, row=2, column=5)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=2, column=6)
        Button(self.window, text="7号锁", command=lambda: self.open_lock(7)).grid(ipadx=10, row=3, column=1)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=3, column=2)
        Button(self.window, text="8号锁", command=lambda: self.open_lock(8)).grid(ipadx=10, row=3, column=3)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=3, column=4)
        Button(self.window, text="9号锁", command=lambda: self.open_lock(9)).grid(ipadx=10, row=3, column=5)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=3, column=6)
        Button(self.window, text="10号锁", command=lambda: self.open_lock(10)).grid(ipadx=10, row=4, column=1)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=4, column=2)
        Button(self.window, text="11号锁", command=lambda: self.open_lock(11)).grid(ipadx=10, row=4, column=3)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=4, column=4)
        Button(self.window, text="12号锁", command=lambda: self.open_lock(12)).grid(ipadx=10, row=4, column=5)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=4, column=6)
        Button(self.window, text="13号锁", command=lambda: self.open_lock(13)).grid(ipadx=10, row=5, column=1)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=5, column=2)
        Button(self.window, text="14号锁", command=lambda: self.open_lock(14)).grid(ipadx=10, row=5, column=3)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=5, column=4)
        Button(self.window, text="15号锁", command=lambda: self.open_lock(15)).grid(ipadx=10, row=5, column=5)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=5, column=6)
        Button(self.window, text="16号锁", command=lambda: self.open_lock(16)).grid(ipadx=10, row=6, column=1)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=6, column=2)
        Button(self.window, text="17号锁", command=lambda: self.open_lock(17)).grid(ipadx=10, row=6, column=3)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=6, column=4)
        Button(self.window, text="18号锁", command=lambda: self.open_lock(18)).grid(ipadx=10, row=6, column=5)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=6, column=6)
        Button(self.window, text="19号锁", command=lambda: self.open_lock(19)).grid(ipadx=10, row=7, column=1)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=7, column=2)
        Button(self.window, text="20号锁", command=lambda: self.open_lock(20)).grid(ipadx=10, row=7, column=3)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=7, column=4)
        Button(self.window, text="21号锁", command=lambda: self.open_lock(21)).grid(ipadx=10, row=7, column=5)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=7, column=6)
        Button(self.window, text="22号锁", command=lambda: self.open_lock(22)).grid(ipadx=10, row=8, column=1)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=8, column=2)
        Button(self.window, text="23号锁", command=lambda: self.open_lock(23)).grid(ipadx=10, row=8, column=3)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=8, column=4)
        Button(self.window, text="24号锁", command=lambda: self.open_lock(24)).grid(ipadx=10, row=8, column=5)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=8, column=6)
        Button(self.window, text="25号锁", command=lambda: self.open_lock(25)).grid(ipadx=10, row=9, column=1)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=9, column=2)
        Button(self.window, text="26号锁", command=lambda: self.open_lock(26)).grid(ipadx=10, row=9, column=3)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=9, column=4)
        Button(self.window, text="27号锁", command=lambda: self.open_lock(27)).grid(ipadx=10, row=9, column=5)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=9, column=6)
        Button(self.window, text="28号锁", command=lambda: self.open_lock(28)).grid(ipadx=10, row=10, column=1)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=10, column=2)
        Button(self.window, text="29号锁", command=lambda: self.open_lock(29)).grid(ipadx=10, row=10, column=3)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=10, column=4)
        Button(self.window, text="30号锁", command=lambda: self.open_lock(30)).grid(ipadx=10, row=10, column=5)
        Label(self.window, textvariable=self.v).grid(ipadx=10, row=10, column=6)

        Button(self.window, text="一键全开")

        self.window.mainloop()

    def _sum(self, num):
        hex_sum = 0
        if num < 21:
            self.BOARD1.append(self.lock_number[num - 1])
            for i in range(len(self.BOARD1)):
                hex_sum += self.BOARD1[i]
            del (self.BOARD1[3])
        elif 21 <= num <= 30:
            num = num - 20
            self.BOARD2.append(self.lock_number[num - 1])
            for i in range(len(self.BOARD2)):
                hex_sum += self.BOARD2[i]
            del (self.BOARD2[3])
        elif num == 200:
            # TODO 开灯
            pass
        elif num == 201:
            # TODO 关灯
            pass
        return hex(hex_sum)

    @staticmethod
    def disintegrate_data(result):
        res1 = result[2]
        if res1.__len__() == 1:
            res1 = '0' + res1
        res2 = result[3:5].upper()
        return res1, res2

    def merge_data(self, lock_num):
        re1, re2 = self.disintegrate_data(self._sum(lock_num))
        if str(self.board1).__len__() == 1:
            self.B1 = '0' + str(self.board1)
        else:
            self.B1 = str(self.BOARD1)
        if str(self.board2).__len__() == 1:
            self.B2 = '0' + str(self.board2)
        else:
            self.B2 = str(self.BOARD2)

        if lock_num < 21:
            if lock_num < 10:
                result = self.B1 + ' F2 55 0' + str(lock_num), re1, re2
            elif lock_num == 10:
                result = self.B1 + ' F2 55 0A ' + re1, re2
            elif lock_num == 11:
                result = self.B1 + ' F2 55 0B ' + re1, re2
            elif lock_num == 12:
                result = self.B1 + ' F2 55 0C ' + re1, re2
            elif lock_num == 13:
                result = self.B1 + ' F2 55 0D ' + re1, re2
            elif lock_num == 14:
                result = self.B1 + ' F2 55 0E ' + re1, re2
            elif lock_num == 15:
                result = self.B1 + ' F2 55 0F ' + re1, re2
            else:
                result = self.B1 + ' F2 55 ' + str(hex(lock_num))[2:4], re1, re2
            # print(' '.join(result))
            return ' '.join(result)
        elif lock_num >= 21:
            lock_num = lock_num - 20
            if lock_num < 10:
                result = self.B2 + ' F2 55 0' + str(lock_num), re1, re2
            elif lock_num == 10:
                result = self.B2 + ' F2 55 0A ' + re1, re2
            elif lock_num == 11:
                result = self.B2 + ' F2 55 0B ' + re1, re2
            elif lock_num == 12:
                result = self.B2 + ' F2 55 0C ' + re1, re2
            elif lock_num == 13:
                result = self.B2 + ' F2 55 0D ' + re1, re2
            elif lock_num == 14:
                result = self.B2 + ' F2 55 0E ' + re1, re2
            elif lock_num == 15:
                result = self.B2 + ' F2 55 0F ' + re1, re2
            else:
                result = self.B2 + ' F2 55 ' + str(hex(lock_num))[2:4], re1, re2

            # print(' '.join(result))
            return ' '.join(result)

    def open_lock(self, number):
        data = self.merge_data(number)
        print(data)
        if self.ser.is_open:
            d = bytes.fromhex(data)
            self.ser.write(d)
        else:
            self.ser.open()
            d = bytes.fromhex(data)
            self.ser.write(d)

    def open_light(self):
        self.BOARD1LIGHT.append(1)
        print(self.BOARD1LIGHT)
        data = self.merge_data(self.BOARD1LIGHT)
        print(data)
        del (self.BOARD1LIGHT[3])

        if self.ser.is_open:
            d = bytes.fromhex(data)
            self.ser.write(d)
        else:
            self.ser.open()
            d = bytes.fromhex(data)
            self.ser.write(d)

    def close_light(self):
        self.BOARD1LIGHT.append(0)
        print(self.BOARD1LIGHT)
        data = self.merge_data(self.BOARD1LIGHT)
        print(data)
        del (self.BOARD1LIGHT[3])

        if self.ser.is_open:
            d = bytes.fromhex(data)
            self.ser.write(d)
        else:
            self.ser.open()
            d = bytes.fromhex(data)
            self.ser.write(d)

    def get_lock_status(self):
        data = []
        while True:
            self.ser.write(b'\x01')
            self.ser.write(b'\xF3')
            self.ser.write(b'\x55')
            self.ser.write(b'\x02')
            self.ser.write(b'\x01')
            self.ser.write(b'\x4B')
            # print(self.ser.read().hex())
            if self.ser.read().hex() == '01':
                if self.ser.read().hex() == 'f3':
                    if self.ser.read().hex() == '55':
                        if self.ser.read().hex() == '02':
                            data.append(bin(int(self.ser.read().hex(), 16))[2:11])
                            data.append(bin(int(self.ser.read().hex(), 16))[2:11])
                            data.append(bin(int(self.ser.read().hex(), 16))[2:11])
                            for i in range(len(data)):
                                for j in range(len(data[i])):
                                    self.lock_sta.append(data[i][j])
                            print(self.lock_sta)
                            # TODO 状态改变代码
                            if self.lock_sta[0] == '0':
                                self.v.set("开锁")
                            data.clear()
                            self.lock_sta.clear()
            time.sleep(0.1)




    def thread_lock_status(self):
        t = threading.Thread(target=self.get_lock_status)
        t.setDaemon(True)
        t.start()


if __name__ == '__main__':
    SerialLockControl("1", "3", "/dev/cu.usbserial-FTAJMSDO")
