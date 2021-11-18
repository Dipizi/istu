from tkinter import *
from tkinter import ttk
import sqlite3

class DataTable(Frame):
    connection = None
    treeview = None
    treeview_columns = ['SecondName', 'FirstName', 'MiddleName', 'Faculty', 'Group', 'Forecast']
    treeview_headings = ['Фамилия', 'Имя', 'Отчество', 'Факультет', 'Группа', 'Прогноз']

    def __init__(self, parent: Frame):
        Frame.__init__(self, parent)

        self.treeview = ttk.Treeview(self, columns = self.treeview_columns, show = 'headings', height = 18)
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

    def reset(self):
        i = 0
        for row in self.connection.execute("""
        SELECT Student.surname, Student.name, Student.patronymic, Institute.name, Student.group_number
        FROM Student
        LEFT JOIN Institute
        ON Student.institute_code = Institute.institute_code
        ORDER BY Student.surname ASC
        """):
            self.treeview.insert("", i, values=row)
            i = i + 1