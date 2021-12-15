from tkinter import *
from tkinter import ttk
import hint_entry
import name_search

class Control(Frame):
    sort_options = None
    search_entry = None
    search_btn = None
    dropdown_option_1 = None
    dropdown_option_2 = None
    reset_btn = None
    name_search = None

    forecast_sort = None
    percentage_entry = None
    percentage_btn = None
    percentage_slider = None

    def __init__(self, parent: Frame):
        Frame.__init__(self, parent)
        self.name_search = name_search.NameSearch(self)

        self.var1 = StringVar(self.sort_options)
        self.var1.set('Институт')
        self.var2 = StringVar(self.sort_options)
        self.var2.set('Группа')
        self.var3 = IntVar(self.sort_options)
        self.var3.set(0)

        self.configure_table()
        self.configure_sort_control()
        self.configure_forecast_sort()

    def configure_table(self):
        for i in range(4):
            self.columnconfigure(i, minsize = 250, weight = 1)

    def configure_sort_control(self):
        self.sort_options = Frame(self)
        self.sort_options_configure_table()
        self.sort_options.grid(row = 0, column = 0, sticky = NSEW, columnspan = 3)

        self.search_entry = hint_entry.HintEntry(self.sort_options, hint = "ФИО")
        self.search_entry.preserve_contents = True
        self.search_entry.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.search_btn = ttk.Button(self.sort_options, style = "Accent.TButton", text = 'Найти', command = self.name_search_command)
        self.search_btn.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = W)

        self.dropdown_option_1 = ttk.OptionMenu(self.sort_options, self.var1, *['Институт', 'Информатика и вычислительная техника'])
        self.dropdown_option_1.configure(width = 5)
        self.dropdown_option_1.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = EW)
        self.dropdown_option_2 = ttk.OptionMenu(self.sort_options, self.var2, *['Группа', 'Б19-782-2'])
        self.dropdown_option_2.configure(width = 5)
        self.dropdown_option_2.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = EW)

        self.reset_btn = ttk.Button(self.sort_options, style = "Accent.TButton", text = "Сбросить фильтр", command = self.reset_command)
        self.reset_btn.grid(row = 1, column = 2, padx = 10, pady = 10, sticky = EW)

    def configure_forecast_sort(self):
        self.forecast_sort = Frame(self)
        self.forecast_sort_configure_table()
        self.forecast_sort.grid(row = 0, column = 3, sticky = NSEW)

        self.percentage_entry = hint_entry.HintEntry(self.forecast_sort, hint="Прогноз, %")
        self.percentage_entry.configure(width = 12)
        self.percentage_entry.preserve_contents = True
        self.percentage_entry.grid(row = 0, column = 0, sticky = E, padx = (0, 10))

        self.percentage_btn = ttk.Button(self.forecast_sort, style = "Accent.TButton", text = 'Фильтр')
        self.percentage_btn.grid(row = 0, column = 1, sticky = EW, padx = (10, 0))

        self.percentage_slider = ttk.Scale(self.forecast_sort, from_ = 0, to = 100, variable = self.var3, command = self.percentage_slider_command, value = 0)
        self.percentage_slider.grid(row = 1, column = 0, sticky = EW, padx = 10, pady = 10, columnspan = 2)

    def forecast_sort_configure_table(self):
        for i in range(2):
            self.forecast_sort.columnconfigure(i, minsize = 125)
            self.forecast_sort.rowconfigure(i, minsize = 50)

    def sort_options_configure_table(self):
        for i in range(2):
            self.sort_options.columnconfigure(i, minsize = 125)
            self.sort_options.rowconfigure(i, minsize = 50)

    def percentage_slider_command(self, _):
        self.var3.set(self.percentage_slider.get())
        self.percentage_entry.set_value(self.var3.get())

    def reset_command(self):
        self.master.data_table.reset()
        self.search_entry.set_hint()
        self.var1.set("Институт")
        self.var2.set("Группа")

    def name_search_command(self):
        s = self.search_entry.get()
        if (s != "" and s != "ФИО"):
            self.master.data_table.set_data(self.name_search.search(self.search_entry.get()))
        else:
            self.master.data_table.reset()