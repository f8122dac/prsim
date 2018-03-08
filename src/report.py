from tkinter.ttk import Frame, Treeview, Scrollbar

from config import *

class Report(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = self.winfo_toplevel()
        self.root.title(" ".join((APPNAME, VERSION, "| Report")))
        self.items= None
        headers = ('Page',' PageRank Value', 'Incoming')
        self.tree = Treeview(self, columns=headers, show="headings", height=REPORT_HEIGHT) 
        self.tree.column(0, anchor='center', width=55)
        self.tree.column(1, width=175)
        self.tree.column(2, anchor='center', width=55)
        self.scroll = Scrollbar(self, command=self.tree.yview)
        self.scroll.pack(side='right', fill='y')
        self.tree.config(yscrollcommand=self.scroll.set)
        for col in headers:
            self.tree.heading(col, text=col.title())

    def render(self, pr, edge_counts):
        in_map = {k: 0 for k in pr.keys()} # incoming edges by nodes
        for (_, head), n in edge_counts.items():
            in_map[head] += n

        data = tuple((k, pr[k], in_map[k]) for k in sorted(pr.keys()))
        if self.items: self.tree.delete(*self.items)
        self.items = [self.tree.insert('', 'end', values=line) for line in data]
        self.tree.pack(side='left', fill='y')

    def destroy(self):
        super().destroy()
        self.root.destroy()


