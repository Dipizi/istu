from tkinter import *
from tkinter import ttk
from control import *
from data_table import *

class Container(Frame):
    _control = None
    _data_table = None
    _forecast = None
    _forecast_btn = None

    def __init__(self, origin: Tk):
        self.__internal_init(origin)

        self._control = Control(self)
        self._control.grid(row = 0, column = 0, padx = 20, pady = (20, 0), sticky = NSEW)

        self._data_table = DataTable(self)
        self._data_table.grid(row = 1, column = 0, padx = 20, sticky = NSEW)

        self._forecast = Frame(self)
        self._forecast.grid(row = 2, column = 0, padx = 20, sticky = NSEW)
        self._forecast_btn = Button(self._forecast, text = 'Прогноз', width = 30, height = 3)
        self._forecast_btn.pack()

    def __internal_init(self, origin: Tk):
        Frame.__init__(self, origin, width = 100, height = 600)
        self.__configure_table()
        self.place(x = 0, y = 0)

    def __configure_table(self):
        self.rowconfigure(0, minsize = 100)
        self.rowconfigure(1, minsize = 400)
        self.rowconfigure(2, minsize = 100)