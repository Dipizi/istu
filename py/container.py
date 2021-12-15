from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from control import *
from data_table import *
from ml_controller import MLController

class Container(Frame):
    control = None
    data_table: DataTable = None
    forecast = None
    forecast_btn = None
    export_btn = None
    mlController = None

    def __init__(self, origin: Tk):
        self.__internal_init(origin)

        self.data_table = DataTable(self)
        self.data_table.grid(row = 1, column = 0, sticky = NSEW, pady = (0, 10))
        
        self.control = Control(self)
        self.control.grid(row = 0, column = 0, sticky = NSEW, pady = (0, 10))

        self.forecast = Frame(self)
        self.forecast.grid(row = 2, column = 0, sticky = NSEW)
        self.forecast_btn = ttk.Button(self.forecast, style='Accent.TButton', text = 'Прогноз', width = 30)
        self.forecast_btn.pack()
        self.export_btn = ttk.Button(self.forecast, text = "Экспортировать таблицу", command = self.save_table_as_excel)
        self.export_btn.place(x = 0, y = 0)

        self.mlController = MLController()

    def __internal_init(self, origin: Tk):
        Frame.__init__(self, origin, width = 1000, height = 600)
        self.configure_table()
        self.pack(padx = 20, pady = 20)

    def configure_table(self):
        self.rowconfigure(0, minsize = 100)
        self.rowconfigure(1, minsize = 400)
        self.rowconfigure(2, minsize = 100)

    def save_table_as_excel(self):
        file = filedialog.asksaveasfilename(title = "Выберите файл", defaultextension = ".xlsx", filetypes = [("Excel file", "*.xlsx")], confirmoverwrite = True)
        if file:
            try:
                self.data_table.cur_to_excel(file)
            except:
                pass

    def do_forecast(self):
        self.mlController.init_model(self.data_table.get_ml_data(self.data_table.mlConnection))
        _in: list = self.mlController.get_input(self.data_table.get_ml_data(self.data_table.connection))
        _out: list = self.mlController.predict_for(_in)

        for i in range(0, _in.__len__()):
            self.data_table.connection.execute("""
                UPDATE AcademicPerformance
                SET status = '%s'
                WHERE student_id = '%s'
            """, (str(_out[i]), str(_in[i][0])))