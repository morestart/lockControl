import serial


class SerialLockControl:
    def __init__(self, serial_name, port=9600):

        self.count = 0
        try:
            self.ser = serial.Serial(serial_name, port)
        except Exception as e:
            print(e)
        self.lock_number = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09,
                            0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x16, 0x17, 0x18, 0x19, 0x20]

        # 第一块板子
        self.open_one_lock = [0x01, 0xF2, 0x55]

    # 求和校验
    def _sum(self):
        hex_sum = 0
        self.open_one_lock.append(self.lock_number[self.count])
        # print(self.open_one_lock)
        for i in range(len(self.open_one_lock)):
            hex_sum += self.open_one_lock[i]
        print("十进制求和: ", hex_sum)
        del (self.open_one_lock[3])
        return hex(hex_sum)

    # 将0x149类似数据转化为 01 49
    def process_data(self):
        result = self._sum()
        res1 = result[2]
        if res1.__len__() == 1:
            res1 = '0' + res1
        res2 = result[3:5].upper()
        return res1, res2

    def order_open_all_lock(self, first_lock, final_lock):
        # 顺序打开第一块板子的lock
        self.count = first_lock - 1
        # print(hex(self.lock_number[self.count]))
        for i in range(first_lock, final_lock):
            re1, re2 = self.process_data()
            print("分解结果", re1, re2)

            if i < 10:
                result = '01 F2 55 0' + str(i), re1, re2
            elif i == 10:
                result = '01 F2 55 0A ' + re1, re2
            elif i == 11:
                result = '01 F2 55 0B ' + re1, re2
            elif i == 12:
                result = '01 F2 55 0C ' + re1, re2
            elif i == 13:
                result = '01 F2 55 0D ' + re1, re2
            elif i == 14:
                result = '01 F2 55 0E ' + re1, re2
            elif i == 15:
                result = '01 F2 55 0F ' + re1, re2
            else:
                result = '01 F2 55 0' + str(i), re1, re2

            self.count = i

            print(' '.join(result))
            print("---------------------------")


if __name__ == '__main__':
    control = SerialLockControl("1")
    control.order_open_all_lock(1, 15)
