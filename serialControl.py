import serial
import time


class SerialLockControl:
    def __init__(self, serial_name, port=9600):

        self.count = 0
        try:
            self.ser = serial.Serial(serial_name, port)
        except Exception as e:
            print(e)
        # 0x00 只充当第0个数 实际用不到
        self.lock_number = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09,
                            0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x16, 0x17, 0x18, 0x19, 0x20]

        # 第一块板子
        self.open_one_lock = [0x01, 0xF2, 0x55]

    def connect(self):
        if self.ser.is_open:
            return True
        else:
            return False

    # 求和校验
    def _sum(self):
        hex_sum = 0
        self.open_one_lock.append(self.lock_number[self.count])
        # print(self.open_one_lock)
        for i in range(len(self.open_one_lock)):
            hex_sum += self.open_one_lock[i]
        # print("十进制求和: ", hex_sum)
        del (self.open_one_lock[3])
        return hex(hex_sum)

    # 将0x149类似数据转化为 01 49
    def disintegrate_data(self):
        result = self._sum()
        res1 = result[2]
        if res1.__len__() == 1:
            res1 = '0' + res1
        res2 = result[3:5].upper()
        return res1, res2

    # 合并数据
    def merge_data(self, lock_num):
        self.count = lock_num
        re1, re2 = self.disintegrate_data()
        # print(re1, re2)
        # print("分解结果", re1, re2)
        if lock_num < 10:
            result = '01 F2 55 0' + str(lock_num), re1, re2
        elif lock_num == 10:
            result = '01 F2 55 0A ' + re1, re2
        elif lock_num == 11:
            result = '01 F2 55 0B ' + re1, re2
        elif lock_num == 12:
            result = '01 F2 55 0C ' + re1, re2
        elif lock_num == 13:
            result = '01 F2 55 0D ' + re1, re2
        elif lock_num == 14:
            result = '01 F2 55 0E ' + re1, re2
        elif lock_num == 15:
            result = '01 F2 55 0F ' + re1, re2
        else:
            result = '01 F2 55 0' + str(lock_num), re1, re2
        return ' '.join(result)

    def open_lock(self, first_lock, final_lock):
        for i in range(first_lock, final_lock + 1):
            send_data = self.merge_data(i)
            print(send_data)
            data = bytes.fromhex(send_data)
            self.ser.write(data)
            self.count = i
            print("---------------------------")
            time.sleep(1)


if __name__ == '__main__':

    lock = SerialLockControl("/dev/cu.usbserial-FTAJMSDO")
    if lock.connect():
        print("串口开启成功")
        print("""
            1. 随机测试
            2. 全开全闭
            """)
        propose = eval(input(">"))
        if propose == 1:
            lock.open_lock(1, 12)
        elif propose == 2:
            pass
    else:
        print("串口未开启")
