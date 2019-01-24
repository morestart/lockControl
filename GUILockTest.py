from tkinter import *
from tkinter.ttk import *
import serial
import threading


class SerialLockControl:
    def __init__(self, serial_name, board1, board2, port=9600):
        self.board = board1
        self.board2 = board2
        self.ser = serial.Serial(serial_name, port)
        self.lock_number = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09,
                            0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10, 0x11, 0x12, 0x13, 0x14]

        self.open = [0x01, 0xF2, 0x55]
        self.open2 = [0x03, 0xF2, 0x55]

        self.window = Tk()
        self.window.title("锁控测试程序")
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        x = int((ws / 2) - (300 / 2))
        y = int((hs / 2) - (300 / 2))
        self.window.geometry("{}x{}+{}+{}".format(430, 300, x, y))
        self.window.resizable(0, 0)
        Button(self.window, text="1号", command=lambda: self.open_lock(1)).grid(ipadx=10, row=1, column=1)
        Button(self.window, text="2号", command=lambda: self.open_lock(2)).grid(ipadx=10, row=1, column=2)
        Button(self.window, text="3号", command=lambda: self.open_lock(3)).grid(ipadx=10, row=1, column=3)
        Button(self.window, text="4号", command=lambda: self.open_lock(4)).grid(ipadx=10, row=1, column=4)
        Button(self.window, text="5号", command=lambda: self.open_lock(5)).grid(ipadx=10, row=2, column=1)
        Button(self.window, text="6号", command=lambda: self.open_lock(6)).grid(ipadx=10, row=2, column=2)
        Button(self.window, text="7号", command=lambda: self.open_lock(7)).grid(ipadx=10, row=2, column=3)
        Button(self.window, text="8号", command=lambda: self.open_lock(8)).grid(ipadx=10, row=2, column=4)
        Button(self.window, text="9号", command=lambda: self.open_lock(9)).grid(ipadx=10, row=3, column=1)
        Button(self.window, text="10号", command=lambda: self.open_lock(10)).grid(ipadx=10, row=3, column=2)
        Button(self.window, text="11号", command=lambda: self.open_lock(11)).grid(ipadx=10, row=3, column=3)
        Button(self.window, text="12号", command=lambda: self.open_lock(12)).grid(ipadx=10, row=3, column=4)
        Button(self.window, text="13号", command=lambda: self.open_lock(13)).grid(ipadx=10, row=4, column=1)
        Button(self.window, text="14号", command=lambda: self.open_lock(14)).grid(ipadx=10, row=4, column=2)
        Button(self.window, text="15号", command=lambda: self.open_lock(15)).grid(ipadx=10, row=4, column=3)
        Button(self.window, text="16号", command=lambda: self.open_lock(16)).grid(ipadx=10, row=4, column=4)
        Button(self.window, text="17号", command=lambda: self.open_lock(17)).grid(ipadx=10, row=5, column=1)
        Button(self.window, text="18号", command=lambda: self.open_lock(18)).grid(ipadx=10, row=5, column=2)
        Button(self.window, text="19号", command=lambda: self.open_lock(19)).grid(ipadx=10, row=5, column=3)
        Button(self.window, text="20号", command=lambda: self.open_lock(20)).grid(ipadx=10, row=5, column=4)
        Button(self.window, text="21号", command=lambda: self.open_lock(21)).grid(ipadx=10, row=6, column=1)
        Button(self.window, text="22号", command=lambda: self.open_lock(22)).grid(ipadx=10, row=6, column=2)
        Button(self.window, text="23号", command=lambda: self.open_lock(23)).grid(ipadx=10, row=6, column=3)
        Button(self.window, text="24号", command=lambda: self.open_lock(24)).grid(ipadx=10, row=6, column=4)
        Button(self.window, text="25号", command=lambda: self.open_lock(25)).grid(ipadx=10, row=7, column=1)
        Button(self.window, text="26号", command=lambda: self.open_lock(26)).grid(ipadx=10, row=7, column=2)
        Button(self.window, text="27号", command=lambda: self.open_lock(27)).grid(ipadx=10, row=7, column=3)
        Button(self.window, text="28号", command=lambda: self.open_lock(28)).grid(ipadx=10, row=7, column=4)
        Button(self.window, text="29号", command=lambda: self.open_lock(29)).grid(ipadx=10, row=8, column=1)
        Button(self.window, text="30号", command=lambda: self.open_lock(30)).grid(ipadx=10, row=8, column=2)

        self.window.mainloop()

    def _sum(self, num):
        hex_sum = 0
        if num < 21:
            self.open.append(self.lock_number[num - 1])
            # print(self.open_one_lock)
            for i in range(len(self.open)):
                hex_sum += self.open[i]
            # print("十进制求和: ", hex_sum)
            del (self.open[3])
        else:
            # 第二个板子从1号开始算起
            num = num - 20
            self.open2.append(self.lock_number[num - 1])
            print(self.open2)
            for i in range(len(self.open2)):
                hex_sum += self.open2[i]
            print("十进制求和: ", hex_sum)
            del (self.open2[3])
        return hex(hex_sum)

    def disintegrate_data(self, result):
        res1 = result[2]
        if res1.__len__() == 1:
            res1 = '0' + res1
        res2 = result[3:5].upper()
        return res1, res2

    def merge_data_board1(self, lock_num):
        re1, re2 = self.disintegrate_data(self._sum(lock_num))
        if lock_num < 10:
            result = self.board + ' F2 55 0' + str(lock_num), re1, re2
        elif lock_num == 10:
            result = self.board + ' F2 55 0A ' + re1, re2
        elif lock_num == 11:
            result = self.board + ' F2 55 0B ' + re1, re2
        elif lock_num == 12:
            result = self.board + ' F2 55 0C ' + re1, re2
        elif lock_num == 13:
            result = self.board + ' F2 55 0D ' + re1, re2
        elif lock_num == 14:
            result = self.board + ' F2 55 0E ' + re1, re2
        elif lock_num == 15:
            result = self.board + ' F2 55 0F ' + re1, re2
        else:
            result = self.board + ' F2 55 ' + str(hex(lock_num))[2:4], re1, re2
        return ' '.join(result)

    def merge_data_board2(self, lock_num):
        re1, re2 = self.disintegrate_data(self._sum(lock_num))
        print(re1, re2)
        lock_num = lock_num - 20
        print(lock_num)
        if lock_num < 10:
            result = self.board2 + ' F2 55 0' + str(lock_num), re1, re2
        elif lock_num == 10:
            result = self.board2 + ' F2 55 0A ' + re1, re2
        elif lock_num == 11:
            result = self.board2 + ' F2 55 0B ' + re1, re2
        elif lock_num == 12:
            result = self.board2 + ' F2 55 0C ' + re1, re2
        elif lock_num == 13:
            result = self.board2 + ' F2 55 0D ' + re1, re2
        elif lock_num == 14:
            result = self.board2 + ' F2 55 0E ' + re1, re2
        elif lock_num == 15:
            result = self.board2 + ' F2 55 0F ' + re1, re2
        else:
            result = self.board2 + ' F2 55 ' + str(hex(lock_num))[2:4], re1, re2
        return ' '.join(result)

    def open_lock(self, number):

        if number < 21:
            data = self.merge_data_board1(number)
            print(data)
            if self.ser.is_open:
                if self.ser.is_open:
                    d = bytes.fromhex(data)
                    self.ser.write(d)
                self.ser.close()
            else:
                self.ser.open()
                d = bytes.fromhex(data)
                self.ser.write(d)
                self.ser.close()
        elif number >= 21:
            print(number)
            data = self.merge_data_board2(number)
            print(data)
            if self.ser.is_open:
                if self.ser.is_open:
                    d = bytes.fromhex(data)
                    self.ser.write(d)
                self.ser.close()
            else:
                self.ser.open()
                d = bytes.fromhex(data)
                self.ser.write(d)
                self.ser.close()


SerialLockControl("/dev/cu.usbserial-FTAJMSDO", '01', '03')
