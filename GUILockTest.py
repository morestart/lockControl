import serial
import time
import threading
from tkinter import *
from tkinter.ttk import Button
from tkinter import messagebox


class SerialLockControl:
    def __init__(self):
        self.window = Tk()
        self.window.title("锁控测试程序")
        # TODO
        self.infoFrame = Frame(self.window)
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        x = int((ws / 2) - (300 / 2))
        y = int((hs / 2) - (300 / 2))
        self.window.geometry("{}x{}+{}+{}".format(430, 300, x, y))
        self.window.resizable(0, 0)



        self.window.mainloop()

    def open_lock(self, number):
        print(number)


if __name__ == '__main__':
    SerialLockControl()