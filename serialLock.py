import serial
import time
import threading
from tkinter import *
from tkinter.ttk import Button
from tkinter import messagebox
import datetime


class SerialLockControl:
    def __init__(self, board1, board2, serial_name, port=9600):

        self.board1 = board1
        self.board2 = board2
        self.serial_name = serial_name
        self.port = port
        self.B1 = ''
        self.B2 = ''
        self.lock_sta = []
        self.lock_sta2 = []
        self.state = 0
        self.BOARD1 = [int(board1), 242, 85]
        self.BOARD2 = [int(board2), 242, 85]
        self.BOARD1LIGHT = [int(board1), 245, 85]
        self.lock_number = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09,
                            0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10, 0x11, 0x12, 0x13, 0x14]

        self.window = Tk()
        self.window.title("锁控测试程序")

        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        x = int((ws / 2) - (300 / 2))
        y = int((hs / 2) - (300 / 2))
        self.window.geometry("{}x{}+{}+{}".format(500, 300, x, y))
        self.window.resizable(0, 0)

        self.v1 = StringVar()
        self.v1.set("关闭")
        Button(self.window, text="1号锁", command=lambda: self.open_lock(1)).grid(ipadx=10, row=1, column=1)
        Label(self.window, textvariable=self.v1).grid(ipadx=10, row=1, column=2)

        self.v2 = StringVar()
        self.v2.set("关闭")
        Button(self.window, text="2号锁", command=lambda: self.open_lock(2)).grid(ipadx=10, row=1, column=3)
        Label(self.window, textvariable=self.v2).grid(ipadx=10, row=1, column=4)

        self.v3 = StringVar()
        self.v3.set("关闭")
        Button(self.window, text="3号锁", command=lambda: self.open_lock(3)).grid(ipadx=10, row=1, column=5)
        Label(self.window, textvariable=self.v3).grid(ipadx=10, row=1, column=6)

        self.v4 = StringVar()
        self.v4.set("关闭")
        Button(self.window, text="4号锁", command=lambda: self.open_lock(4)).grid(ipadx=10, row=2, column=1)
        Label(self.window, textvariable=self.v4).grid(ipadx=10, row=2, column=2)

        self.v5 = StringVar()
        self.v5.set("关闭")
        Button(self.window, text="5号锁", command=lambda: self.open_lock(5)).grid(ipadx=10, row=2, column=3)
        Label(self.window, textvariable=self.v5).grid(ipadx=10, row=2, column=4)

        self.v6 = StringVar()
        self.v6.set("关闭")
        Button(self.window, text="6号锁", command=lambda: self.open_lock(6)).grid(ipadx=10, row=2, column=5)
        Label(self.window, textvariable=self.v6).grid(ipadx=10, row=2, column=6)

        self.v7 = StringVar()
        self.v7.set("关闭")
        Button(self.window, text="7号锁", command=lambda: self.open_lock(7)).grid(ipadx=10, row=3, column=1)
        Label(self.window, textvariable=self.v7).grid(ipadx=10, row=3, column=2)

        self.v8 = StringVar()
        self.v8.set("关闭")
        Button(self.window, text="8号锁", command=lambda: self.open_lock(8)).grid(ipadx=10, row=3, column=3)
        Label(self.window, textvariable=self.v8).grid(ipadx=10, row=3, column=4)

        self.v9 = StringVar()
        self.v9.set("关闭")
        Button(self.window, text="9号锁", command=lambda: self.open_lock(9)).grid(ipadx=10, row=3, column=5)
        Label(self.window, textvariable=self.v9).grid(ipadx=10, row=3, column=6)

        self.v10 = StringVar()
        self.v10.set("关闭")
        Button(self.window, text="10号锁", command=lambda: self.open_lock(10)).grid(ipadx=10, row=4, column=1)
        Label(self.window, textvariable=self.v10).grid(ipadx=10, row=4, column=2)

        self.v11 = StringVar()
        self.v11.set("关闭")
        Button(self.window, text="11号锁", command=lambda: self.open_lock(11)).grid(ipadx=10, row=4, column=3)
        Label(self.window, textvariable=self.v11).grid(ipadx=10, row=4, column=4)

        self.v12 = StringVar()
        self.v12.set("关闭")
        Button(self.window, text="12号锁", command=lambda: self.open_lock(12)).grid(ipadx=10, row=4, column=5)
        Label(self.window, textvariable=self.v12).grid(ipadx=10, row=4, column=6)

        self.v13 = StringVar()
        self.v13.set("关闭")
        Button(self.window, text="13号锁", command=lambda: self.open_lock(13)).grid(ipadx=10, row=5, column=1)
        Label(self.window, textvariable=self.v13).grid(ipadx=10, row=5, column=2)

        self.v14 = StringVar()
        self.v14.set("关闭")
        Button(self.window, text="14号锁", command=lambda: self.open_lock(14)).grid(ipadx=10, row=5, column=3)
        Label(self.window, textvariable=self.v14).grid(ipadx=10, row=5, column=4)

        self.v15 = StringVar()
        self.v15.set("关闭")
        Button(self.window, text="15号锁", command=lambda: self.open_lock(15)).grid(ipadx=10, row=5, column=5)
        Label(self.window, textvariable=self.v15).grid(ipadx=10, row=5, column=6)

        self.v16 = StringVar()
        self.v16.set("关闭")
        Button(self.window, text="16号锁", command=lambda: self.open_lock(16)).grid(ipadx=10, row=6, column=1)
        Label(self.window, textvariable=self.v16).grid(ipadx=10, row=6, column=2)

        self.v17 = StringVar()
        self.v17.set("关闭")
        Button(self.window, text="17号锁", command=lambda: self.open_lock(17)).grid(ipadx=10, row=6, column=3)
        Label(self.window, textvariable=self.v17).grid(ipadx=10, row=6, column=4)

        self.v18 = StringVar()
        self.v18.set("关闭")
        Button(self.window, text="18号锁", command=lambda: self.open_lock(18)).grid(ipadx=10, row=6, column=5)
        Label(self.window, textvariable=self.v18).grid(ipadx=10, row=6, column=6)

        self.v19 = StringVar()
        self.v19.set("关闭")
        Button(self.window, text="19号锁", command=lambda: self.open_lock(19)).grid(ipadx=10, row=7, column=1)
        Label(self.window, textvariable=self.v19).grid(ipadx=10, row=7, column=2)

        self.v20 = StringVar()
        self.v20.set("关闭")
        Button(self.window, text="20号锁", command=lambda: self.open_lock(20)).grid(ipadx=10, row=7, column=3)
        Label(self.window, textvariable=self.v20).grid(ipadx=10, row=7, column=4)

        self.v21 = StringVar()
        self.v21.set("关闭")
        Button(self.window, text="21号锁", command=lambda: self.open_lock(21)).grid(ipadx=10, row=7, column=5)
        Label(self.window, textvariable=self.v21).grid(ipadx=10, row=7, column=6)

        self.v22 = StringVar()
        self.v22.set("关闭")
        Button(self.window, text="22号锁", command=lambda: self.open_lock(22)).grid(ipadx=10, row=8, column=1)
        Label(self.window, textvariable=self.v22).grid(ipadx=10, row=8, column=2)

        self.v23 = StringVar()
        self.v23.set("关闭")
        Button(self.window, text="23号锁", command=lambda: self.open_lock(23)).grid(ipadx=10, row=8, column=3)
        Label(self.window, textvariable=self.v23).grid(ipadx=10, row=8, column=4)

        self.v24 = StringVar()
        self.v24.set("关闭")
        Button(self.window, text="24号锁", command=lambda: self.open_lock(24)).grid(ipadx=10, row=8, column=5)
        Label(self.window, textvariable=self.v24).grid(ipadx=10, row=8, column=6)

        self.v25 = StringVar()
        self.v25.set("关闭")
        Button(self.window, text="25号锁", command=lambda: self.open_lock(25)).grid(ipadx=10, row=9, column=1)
        Label(self.window, textvariable=self.v25).grid(ipadx=10, row=9, column=2)

        self.v26 = StringVar()
        self.v26.set("关闭")
        Button(self.window, text="26号锁", command=lambda: self.open_lock(26)).grid(ipadx=10, row=9, column=3)
        Label(self.window, textvariable=self.v26).grid(ipadx=10, row=9, column=4)

        self.v27 = StringVar()
        self.v27.set("关闭")
        Button(self.window, text="27号锁", command=lambda: self.open_lock(27)).grid(ipadx=10, row=9, column=5)
        Label(self.window, textvariable=self.v27).grid(ipadx=10, row=9, column=6)

        self.v28 = StringVar()
        self.v28.set("关闭")
        Button(self.window, text="28号锁", command=lambda: self.open_lock(28)).grid(ipadx=10, row=10, column=1)
        Label(self.window, textvariable=self.v28).grid(ipadx=10, row=10, column=2)

        self.v29 = StringVar()
        self.v29.set("关闭")
        Button(self.window, text="29号锁", command=lambda: self.open_lock(29)).grid(ipadx=10, row=10, column=3)
        Label(self.window, textvariable=self.v29).grid(ipadx=10, row=10, column=4)

        self.v30 = StringVar()
        self.v30.set("关闭")
        Button(self.window, text="30号锁", command=lambda: self.open_lock(30)).grid(ipadx=10, row=10, column=5)
        Label(self.window, textvariable=self.v30).grid(ipadx=10, row=10, column=6)

        Button(self.window, text="开灯", command=self.open_light).grid(ipadx=10, row=11, column=1)
        Button(self.window, text="关灯", command=self.open_light).grid(ipadx=10, row=11, column=2)

        Button(self.window, text="打开串口", command=self.open_serial).grid(ipadx=10, row=12, column=1)

        # Button(self.window, text="一键全开")

        self.window.mainloop()

    def open_serial(self):
        try:
            self.ser = serial.Serial(self.serial_name, self.port)
            t1 = threading.Thread(target=self._update)
            t1.setDaemon(True)
            t1.start()
        except Exception as e:
            messagebox.showerror("ERROR", e)
            exit(1)

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

    def _update(self):
        while True:
            self.get_board1_status()
            # time.sleep(5)
            self.get_board2_status()

    def get_board2_status(self):
        data = []
        time.sleep(3)
        if str(self.board2).__len__() == 1:
            self.B2 = '0' + str(self.board2)
        else:
            self.B2 = str(self.BOARD2)
        # while True:
            # TODO 这里的教检没有进行计算
        self.ser.write(bytes.fromhex(self.B2 + " F3 55 02 01 4D"))
        if self.ser.read().hex() == self.B2:
            if self.ser.read().hex() == 'f3':
                if self.ser.read().hex() == '55':
                    if self.ser.read().hex() == '02':
                        if self.ser.read().hex() == '00':
                            # 10-9
                            d1 = bin(int(self.ser.read().hex(), 16))[2:4]
                            # print(d1)
                            # 8-1
                            d2 = bin(int(self.ser.read().hex(), 16))[2:10]
                            # print(d2)
                            data.append(d2)
                            data.append(d1)
                            for i in range(len(data)):
                                for j in range(len(data[i])):
                                    self.lock_sta2.append(data[i][j])
                            # print(datetime.time.second, end='')
                            # print(self.lock_sta2)
                            self.update_status('2')
                            data.clear()
                            self.lock_sta2.clear()
            # print(str(time.time()) + "ok")
            time.sleep(0.5)

    def get_board1_status(self):
        data = []
        if str(self.board1).__len__() == 1:
            self.B1 = '0' + str(self.board1)
        else:
            self.B1 = str(self.BOARD1)
        # while True:
        self.ser.write(bytes.fromhex(self.B1 + " F3 55 02 01 4B"))

        if self.ser.read().hex() == self.B1:
            if self.ser.read().hex() == 'f3':
                if self.ser.read().hex() == '55':
                    if self.ser.read().hex() == '02':
                        # 20-17
                        d1 = bin(int(self.ser.read().hex(), 16))[6:11]
                        # 16-9
                        d2 = bin(int(self.ser.read().hex(), 16))[2:11]
                        # 8-1
                        d3 = bin(int(self.ser.read().hex(), 16))[2:11]
                        # print(d3)
                        # print(d2)
                        # print(d1)

                        data.append(d3)
                        data.append(d2)
                        data.append(d1)
                        for i in range(len(data)):
                            for j in range(len(data[i])):
                                self.lock_sta.append(data[i][j])

                        self.update_status('1')

                        data.clear()
                        self.lock_sta.clear()

            time.sleep(0.5)

    def update_status(self, board):

        if board == '1':
            print(self.lock_sta, end=' ')
            now = datetime.datetime.now()
            print(now.strftime('%H:%M:%S'))
            if self.lock_sta[0] == '1':
                self.v8.set("打开")
            else:
                self.v8.set("关闭")

            if self.lock_sta[1] == '1':
                self.v7.set("打开")
            else:
                self.v7.set("关闭")

            if self.lock_sta[2] == '1':
                self.v6.set("打开")
            else:
                self.v6.set("关闭")

            if self.lock_sta[3] == '1':
                self.v5.set("打开")
            else:
                self.v5.set("关闭")

            if self.lock_sta[4] == '1':
                self.v4.set("打开")
            else:
                self.v4.set("关闭")

            if self.lock_sta[5] == '1':
                self.v3.set("打开")
            else:
                self.v3.set("关闭")

            if self.lock_sta[6] == '1':
                self.v2.set("打开")
            else:
                self.v2.set("关闭")

            if self.lock_sta[7] == '1':
                self.v1.set("打开")
            else:
                self.v1.set("关闭")

            if self.lock_sta[8] == '1':
                self.v16.set("打开")
            else:
                self.v16.set("关闭")

            if self.lock_sta[9] == '1':
                self.v15.set("打开")
            else:
                self.v15.set("关闭")

            if self.lock_sta[10] == '1':
                self.v14.set("打开")
            else:
                self.v14.set("关闭")

            if self.lock_sta[11] == '1':
                self.v13.set("打开")
            else:
                self.v13.set("关闭")

            if self.lock_sta[12] == '1':
                self.v12.set("打开")
            else:
                self.v12.set("关闭")

            if self.lock_sta[13] == '1':
                self.v11.set("打开")
            else:
                self.v11.set("关闭")

            if self.lock_sta[14] == '1':
                self.v10.set("打开")
            else:
                self.v10.set("关闭")

            if self.lock_sta[15] == '1':
                self.v9.set("打开")
            else:
                self.v9.set("关闭")

            if self.lock_sta[15] == '1':
                self.v20.set("打开")
            else:
                self.v20.set("关闭")

            if self.lock_sta[16] == '1':
                self.v19.set("打开")
            else:
                self.v19.set("关闭")

            if self.lock_sta[17] == '1':
                self.v18.set("打开")
            else:
                self.v18.set("关闭")

            if self.lock_sta[18] == '1':
                self.v17.set("打开")
            else:
                self.v17.set("关闭")

        elif board == '2':
            print(self.lock_sta2)
            if self.lock_sta2[0] == '1':
                self.v28.set("打开")
            else:
                self.v28.set("关闭")

            if self.lock_sta2[1] == '1':
                self.v27.set("打开")
            else:
                self.v27.set("关闭")

            if self.lock_sta2[2] == '1':
                self.v26.set("打开")
            else:
                self.v26.set("关闭")

            if self.lock_sta2[3] == '1':
                self.v25.set("打开")
            else:
                self.v25.set("关闭")

            if self.lock_sta2[4] == '1':
                self.v24.set("打开")
            else:
                self.v24.set("关闭")

            if self.lock_sta2[5] == '1':
                self.v23.set("打开")
            else:
                self.v23.set("关闭")

            if self.lock_sta2[6] == '1':
                self.v22.set("打开")
            else:
                self.v22.set("关闭")

            if self.lock_sta2[7] == '1':
                self.v21.set("打开")
            else:
                self.v21.set("关闭")

            if self.lock_sta2[8] == '1':
                self.v30.set("打开")
            else:
                self.v30.set("关闭")

            if self.lock_sta2[9] == '1':
                self.v29.set("打开")
            else:
                self.v29.set("关闭")
        time.sleep(4)


if __name__ == '__main__':
    SerialLockControl("1", "3", "/dev/cu.usbserial-FTAJMSDO")
