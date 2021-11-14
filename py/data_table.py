from tkinter import *
from tkinter import ttk

class DataTable(Frame):
    _treeview = None
    _treeview_columns = ['SecondName', 'FirstName', 'MiddleName', 'Faculty', 'Group', 'Forecast']
    _treeview_headings = ['Фамилия', 'Имя', 'Отчество', 'Факультет', 'Группа', 'Прогноз']

    def __init__(self, parent: Frame):
        Frame.__init__(self, parent)

        self._treeview = ttk.Treeview(self, columns = self._treeview_columns, show = 'headings', height = 18)
        self._configure_treeview_columns()
        self._treeview.grid(row = 0, column = 0, sticky = NS)

    def _configure_treeview_columns(self):
        for i in range(6):
            self._treeview.heading(i, text = self._treeview_headings[i])
            self._treeview.column(i, width = 160, minwidth = 30)