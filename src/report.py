from tkinter import Frame
from tkinter.ttk import Treeview

from config import *

class Report(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = self.winfo_toplevel()
        self.root.title(" ".join((APPNAME, VERSION, "| Report")))
        self.items= None
        self.header = ('Page #',' PageRank Value')
        self.tree = Treeview(self, columns=self.header, show="headings", height=REPORT_HEIGHT) 
        for col in self.header:
            self.tree.heading(col, text=col.title())

    def render(self, data):
        if self.items: self.tree.delete(*self.items)
        self.items = [self.tree.insert('', 'end', values=line) for line in data]
        self.tree.pack()

    def destroy(self):
        super().destroy()
        self.root.destroy()
