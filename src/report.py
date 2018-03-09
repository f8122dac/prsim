from tkinter import Scale
from tkinter.ttk import Frame, Label, Treeview, Scrollbar

from config import *

class Report(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = self.winfo_toplevel()
        self.root.title(" ".join((APPNAME, VERSION, "| Report")))
        self.items= None
        headers = ('Page', 'Rank', 'PageRank Value', 'Incoming')
        self.label = Label(self, anchor='e')
        self.label.pack(fill='x')
        self.t = Scale(self, from_=0, to=1, label='nth iteration',
                bd=1, width=7, orient='horizontal', command=self.__set_t)
        self.t.pack(fill='x')
        self.tree = Treeview(self, columns=headers, show="headings", height=REPORT_HEIGHT) 
        self.tree.column(0, anchor='center', width=55)
        self.tree.column(1, anchor='center', width=55)
        self.tree.column(2, width=175)
        self.tree.column(3, anchor='center', width=55)
        self.scroll = Scrollbar(self, command=self.tree.yview)
        self.scroll.pack(side='right', fill='y')
        self.tree.config(yscrollcommand=self.scroll.set)
        for col in headers:
            self.tree.heading(col, text=col.title())
        self.root.master.focus_force()
        self.root.bind('<Key>', self.__keys) 

    def __keys(self, event):
        if event.char == 'i':
            self.t.set(self.t.get()-1)
        elif event.char == 'o':
            self.t.set(self.t.get()+1)

    def __set_t(self, t=None):
        self.render(self.pagerank, self.edge_counts, self.d, self.e, t=int(t))

    def render(self, pagerank, edge_counts, d, e, t=None):
        self.d, self.e = d, e
        self.edge_counts = edge_counts
        self.pagerank = pagerank 
        if t is not None:
            pr = pagerank[0][t]
        else:
            self.t.config(command=None)
            self.t.config(to=self.pagerank[1])
            self.t.set(self.pagerank[1])
            self.t.config(command=self.__set_t)
            pr = pagerank[0][-1]
        label_text = 'Iterations:{0:>3}   Ranks:{1:>3}'.format(
                self.pagerank[1], len(set(pr.values())))
        self.label.config(text=label_text)
        in_map = {k: 0 for k in pr.keys()} # incoming edges by nodes
        for (tail, head), n in edge_counts.items():
            if tail is not head:
                in_map[head] += n

        get_rank = lambda k: len(pr.keys())-sorted(pr.values()).index(pr[k])
        data = tuple((k, get_rank(k), pr[k], in_map[k]) for k in sorted(pr.keys()))
        if self.items: self.tree.delete(*self.items)
        self.items = [self.tree.insert('', 'end', values=line) for line in data]
        self.tree.pack(side='left', fill='y')
        #self.root.master.focus_force()

    def destroy(self):
        super().destroy()
        self.root.master.r_win=False
        self.root.master.windowsmenu.entryconfig(0, label='[ ] Report window')
        self.root.destroy()


