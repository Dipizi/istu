from tkinter import *
from tkinter import ttk
from container import *

class HintEntry(ttk.Entry):
    hint = None
    preserve_contents = False
    var = None

    def __init__(self, master, hint = None):
        ttk.Entry.__init__(self, master)
        self.var = StringVar(self)
        self.var.set('')
        self.hint = hint
        self.bind("<FocusIn>", self.on_focused_in)
        self.bind("<FocusOut>", self.on_focused_out)
        self.set_hint()

    def set_hint(self):
        self.config(foreground = "grey")
        self.delete(0, END)
        self.insert(0, self.hint)

    def on_focused_in(self, _):
        if (not self.preserve_contents or (self.get() == self.hint)):
            self.delete(0, END)
        self.config(foreground = "black")

    def on_focused_out(self, _):
        if (not self.preserve_contents or self.get() == ''):
            self.delete(0, END)
            self.insert(0, self.hint)
        self.config(foreground = "grey")

    def set_value(self, value):
        self.delete(0, END)
        self.insert(0, value)
