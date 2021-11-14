from tkinter import *
from tkinter import ttk
from container import *

class Origin:
    _origin = None
    _container = None

    def __init__(self):
        self._origin = Tk()
        self._origin.title("Title")
        self._origin.geometry("1000x600")
        self._origin.resizable(0, 0)
        
    def init_container(self):
        _container = Container(self._origin)
        
    def run(self):
        self._origin.mainloop()

origin = Origin()
origin.init_container()
origin.run()