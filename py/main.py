from tkinter import *
from tkinter import ttk
from container import *

class Origin:
    _origin = None
    _container = None
    _style = None

    def __init__(self):
        self._origin = ttk.tkinter.Tk()
        self._origin.title("Цифровой след")
        self._origin.geometry("1040x640")
        self._origin.resizable(0, 0)

        self._origin.tk.call("source", "py/sun-valley.tcl")
        self._origin.tk.call("set_theme", "light")
        
    def init_container(self):
        _container = Container(self._origin)
        
    def run(self):
        self._origin.mainloop()

origin = Origin()
origin.init_container()
origin.run()