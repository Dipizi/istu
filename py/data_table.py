from tkinter import *
from tkinter import ttk
from typing import *
import sqlite3
import xlsxwriter

class DataTable(Frame):
    connection = None
    treeview = None
    treeview_columns = ['SecondName', 'FirstName', 'MiddleName', 'Faculty', 'Group', 'Forecast']
    treeview_headings = ['Фамилия', 'Имя', 'Отчество', 'Факультет', 'Группа', 'Прогноз']

    def __init__(self, parent: Frame):
        Frame.__init__(self, parent)

        self.treeview = ttk.Treeview(self, style="Treeview", columns = self.treeview_columns, show = 'headings', height=18)
        self.reset_treeview_columns()
        self.treeview.grid(row = 0, column = 0, sticky = EW)

        self.connect()
        self.reset()

    def reset_treeview_columns(self):
        for i in range(6):
            self.treeview.heading(i, text = self.treeview_headings[i])
            self.treeview.column(i, width = 158, minwidth = 30)

    def connect(self):
        self.connection = sqlite3.connect("../db/sqlData.db")

    def clear_data(self):
        self.treeview.delete(*self.treeview.get_children())

    def get_cur_data(self) -> Tuple[str, ...]:
        return self.treeview.get_children()

    def get_data(self) -> list:
        return self.connection.execute("""
        SELECT Student.surname, Student.name, Student.patronymic, Institute.name, Student.group_number
        FROM Student
        LEFT JOIN Institute
        ON Student.institute_code = Institute.institute_code
        ORDER BY Student.surname ASC
        """)

    def set_data(self, list: list):
        self.clear_data()
        i = 0
        for row in list:
            self.treeview.insert("", i, values=row)
            i = i + 1

    def reset(self):
        self.set_data(self.get_data())

    def cur_to_excel(self, file: str):
        data = self.get_cur_data()
        l: list = []
        for id in data:
            l.append(self.treeview.item(id)["values"])
        
        workbook = xlsxwriter.Workbook(file)
        worksheet = workbook.add_worksheet()

        worksheet.write_row(0, 0, self.treeview_headings)
        row = 1
        for item in l:
            worksheet.write_row(row, 0, item)
            row += 1
        
        workbook.close()