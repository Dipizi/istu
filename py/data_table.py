from sqlite3.dbapi2 import Connection
from tkinter import *
from tkinter import ttk
from typing import *
import sqlite3
import xlsxwriter

class DataTable(Frame):
    connection = None
    mlConnection = None
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
        self.mlConnection = sqlite3.connect("../db/ml.db")

    def clear_data(self):
        self.treeview.delete(*self.treeview.get_children())

    def get_cur_data(self) -> Tuple[str, ...]:
        return self.treeview.get_children()

    def get_cur_data_as_list(self) -> list:
        data = self.get_cur_data()
        l: list = []
        for id in data:
            l.append(self.treeview.item(id)["values"])

    def get_preview_data(self) -> list:
        return self.connection.execute("""
            SELECT Student.surname, Student.name, Student.patronymic, Institute.name, Student.group_number
            FROM Student
            LEFT JOIN Institute
            ON Student.institute_code = Institute.institute_code
            ORDER BY Student.surname ASC
        """).fetchall()

    def get_ml_data(self, con: Connection) -> list:
        a = [list(x) for x in con.execute("""
            SELECT Student.number_grade_book, Student.compensation_type, AcademicPerformance.status, NULL
            FROM Student
            LEFT JOIN AcademicPerformance
            ON Student.number_grade_book = AcademicPerformance.student_id
        """).fetchall()]
        b = [list(x) for x in con.execute("""
            SELECT Assessments.students_id, Assessments.exam_grade, Assessments.session_term
            FROM Assessments
        """).fetchall()]

        for rowa in a:
            rowa[0] = int(rowa[0])
            rowa[1] = int(rowa[1])
            rowa[2] = int(rowa[2])
            rowa[3] = []
            if (b.__len__() > 0):
                for rowb in b:
                    if (rowa[0] == rowb[0]):
                        x = 0
                        if (rowb[1] == 'Отлично'):
                            x = 5
                        elif (rowb[1] == 'Хорошо'):
                            x = 4
                        elif (rowb[1] == 'Удовлетворительно'):
                            x = 3
                        rowa[3].append(x * int(rowb[2]))
        
        return a

    def get_institutes(self) -> list:
        return self.connection.execute("""
        SELECT Institute.name
        FROM Institute
        """).fetchall()

    def set_data(self, list: list):
        self.clear_data()
        i = 0
        for row in list:
            self.treeview.insert("", i, values=row)
            i = i + 1

    def reset(self):
        self.set_data(self.get_preview_data())

    def cur_to_excel(self, file: str):
        l: list = self.get_cur_data_as_list()
        
        workbook = xlsxwriter.Workbook(file)
        worksheet = workbook.add_worksheet()

        worksheet.write_row(0, 0, self.treeview_headings)
        row = 1
        for item in l:
            worksheet.write_row(row, 0, item)
            row += 1
        
        workbook.close()