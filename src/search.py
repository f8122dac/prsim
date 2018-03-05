from tkinter import CENTER
from tkinter.ttk import Frame, Entry, Button, Treeview

from config import *

class Search(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = self.winfo_toplevel()
        self.root.title(" ".join((APPNAME, VERSION, "| Search")))
        self.entry= Entry(self, width=57)
        self.entry.grid(column=0, row=0, ipady=2)
        self.b = Button(self, text='Search', command=self.__search)
        self.b.grid(column=1, row=0)
        headers = ('Rank', 'Page')
        self.tree = Treeview(self, columns=headers, show="headings", height=SEARCH_HEIGHT)
        self.tree.grid(column=0, row=1)
        self.msg = Frame(self)
        self.msg.grid(column=1, row=1)
    def destroy(self):
        super().destroy()
        self.root.destroy()

    def __search(self):
        pass
