from tkinter import *
from tkinter import ttk

class NameSearch():
    master = None

    def __init__(self, master: Frame):
        self.master = master

    def search(self, value: str) -> list:
        l: list = self.master.master.data_table.get_data()
        ret: list = []
        i = 0
        for elem in l:
            s = elem[0] + " " + elem[1] + " " + elem[2]
            if (value in s):
                ret.append(elem)
                i = i + 1
        return ret