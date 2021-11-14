from tkinter import *
from tkinter import ttk

class Control(Frame):
    sort_options = None
    search_entry = None
    search_btn = None
    dropdown_option_1 = None
    dropdown_option_2 = None

    forecast_sort = None
    percentage_entry = None
    percentage_btn = None

    def __init__(self, parent: Frame):
        Frame.__init__(self, parent)
        self.__configure_table()
        self.__configure_sort_control()
        self.__configure_forecast_sort()

    def __configure_table(self):
        for i in range(4):
            self.columnconfigure(i, minsize = 250, weight = 1)

    def __configure_sort_control(self):
        self.sort_options = Frame(self)
        self.__sort_options_configure_table()
        self.sort_options.grid(row = 0, column = 0, sticky = NSEW)

        self.search_entry = Entry(self.sort_options)
        self.search_entry.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.search_btn = Button(self.sort_options, text = 'Найти')
        self.search_btn.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = W)

        var = StringVar(self.sort_options)
        var.set('Институт')
        self.dropdown_option_1 = OptionMenu(self.sort_options, variable = var, value = 'Институт')
        self.dropdown_option_1.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = EW)

        var = StringVar(self.sort_options)
        var.set('ИИВТ')
        self.dropdown_option_2 = OptionMenu(self.sort_options, variable = var, value = 'ИИВТ')
        self.dropdown_option_2.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = EW)

    def __configure_forecast_sort(self):
        self.forecast_sort = Frame(self)
        self.__forecast_sort_configure_table()
        self.forecast_sort.grid(row = 0, column = 3, sticky = NSEW)

        self.percentage_entry = Entry(self.forecast_sort, width = 15)
        self.percentage_entry.grid(row = 0, column = 0, sticky = W)

        self.percentage_btn = Button(self.forecast_sort, text = 'Сортировать')
        self.percentage_btn.grid(row = 0, column = 1, padx = (10, 0))

    def __forecast_sort_configure_table(self):
        self.forecast_sort.rowconfigure(0, minsize = 100)

    def __sort_options_configure_table(self):
        for i in range(2):
            self.sort_options.columnconfigure(i, minsize = 125)
            self.sort_options.rowconfigure(i, minsize = 50)