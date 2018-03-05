from tkinter import Frame, CENTER
from tkinter.ttk import Treeview, Scrollbar

from config import *

class Report(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = self.winfo_toplevel()
        self.root.title(" ".join((APPNAME, VERSION, "| Report")))
        self.items= None
        self.header = ('Page',' PageRank Value', 'Incoming')
        self.tree = Treeview(self, columns=self.header, show="headings", height=REPORT_HEIGHT) 
        self.tree.column(0, anchor=CENTER, width=55)
        self.tree.column(2, anchor=CENTER, width=55)
        self.scroll = Scrollbar(self, command=self.tree.yview)
        self.scroll.pack(side='right', fill='y')
        self.tree.config(yscrollcommand=self.scroll.set)

        for col in self.header:
            self.tree.heading(col, text=col.title())


    def render(self, pr, edge_counts):
        ic = {k: 0 for k in pr.keys()} # incoming edges by nodes
        for k, n in map(lambda a: (a[0][0], a[1]), edge_counts.items()):
            ic[k] += n
        data = tuple((k, pr[k], ic[k]) for k in sorted(pr.keys()))
        if self.items: self.tree.delete(*self.items)
        self.items = [self.tree.insert('', 'end', values=line) for line in data]
        self.tree.pack(side='left', fill='y')

    def destroy(self):
        super().destroy()
        self.root.destroy()
