from tkinter import Tk, Toplevel, Frame, Scale, HORIZONTAL

from config import *
from utils.pagerank import pagerank
from utils.edges import randEdges
from visualizer import Visualizer
from report import Report

class Main(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = self.winfo_toplevel()
        self.root.title(" ".join((APPNAME, VERSION, "| Main")))

        self.e = Scale(self, from_=E_MIN, to=E_MAX, label='Links',
                bd=1, width=12, length=150, orient=HORIZONTAL)
        self.d = Scale(self, from_=D_MIN, to=D_MAX, label='Pages',
                bd=1, width=12, length=150, orient=HORIZONTAL)
        self.e.set(E)
        self.e.config(command=self.refresh)
        self.d.config(command=self.refresh)
        self.e.pack()
        self.d.pack()
        self.d.set(D)
        self.r_win = False

        self.generate_model()
        self.c = Visualizer(self, D, self.edge_counts, self.p[0], offset=50)
        self.c.pack()

        self.root.bind('<Key>', self.__keys) 

    def generate_model(self):
        edges = randEdges(self.d.get(), self.e.get())
        self.edge_counts = {e: edges.count(e) for e in set(edges)}
        self.p = pagerank(edges)

    def render(self):
        self.generate_model()
        self.c.render(self.d.get(), self.edge_counts, self.p[0])
        try: self.r.render(self.p[0], self.edge_counts)
        except: pass

    def refresh(self, value=None):
        self.generate_model()
        self.render()
            
    def __toggle_report(self):
        if self.r_win:
            try: self.r.destroy()
            except: pass
            self.r_win = False
            return 
        self.r = Report(Toplevel(self))
        self.r.pack()
        self.r.render(self.p[0], self.edge_counts)
        self.focus_force()
        self.r_win = True


    def __keys(self, event):
        if event.char == 'q':
            self.destroy()

        elif event.char == 'r':
            self.__toggle_report()

        elif event.char == 'n':
            self.refresh()

        elif event.char == 'j':
            self.d.set(self.d.get()-1)
        elif event.char == 'J':
            self.d.set(self.d.get()-5)
        elif event.char == 'k':
            self.d.set(self.d.get()+1)
        elif event.char == 'K':
            self.d.set(self.d.get()+5)

        elif event.char == 'h':
            self.e.set(self.e.get()-1)
        elif event.char == 'H':
            self.e.set(self.e.get()-40)
        elif event.char == 'l':
            self.e.set(self.e.get()+1)
        elif event.char == 'L':
            self.e.set(self.e.get()+40)
            
    def destroy(self):
        try: self.r.destroy()
        except: pass
        super().destroy()
        self.root.destroy()
        exit(1)


if __name__ == "__main__":
    root = Tk()
    s = Main(root)
    s.pack()
    root.mainloop()
