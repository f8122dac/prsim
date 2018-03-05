from tkinter import Tk, Toplevel, Frame, Scale, HORIZONTAL, ALL

from config import *
from utils.pagerank import pagerank
from utils.edges import randEdges
from visualizer import Visualizer
from report import Report

class Search(Frame):
    pass

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

        self.generate()
        self.c = Visualizer(self, D, self.edges, self.p[0], offset=50)
        self.c.pack()

        self.root.bind('<Key>', self.__keys) 

    def generate(self):
        self.edges = randEdges(self.d.get(), self.e.get())
        self.p = pagerank(self.edges)

    def render(self):
        self.generate()
        self.c.render(self.d.get(), self.edges, self.p[0])
        try: self.r.render(self.get_ranks())
        except: pass

    def refresh(self, value=None):
        self.generate()
        self.render()

    def get_ranks(self):
        return tuple((k, self.p[0][k]) for k in sorted(self.p[0].keys()))
            
    def __open_report(self):
        self.__close_report()
        self.r = Report(Toplevel(self))
        self.r.pack()
        self.r.render(self.get_ranks())
        self.focus_force()

    def __close_report(self):
        try: self.r.destroy()
        except: pass

    def __keys(self, event):
        if event.char == 'q':
            self.destroy()
        elif event.char == 'n':
            self.refresh()

        elif event.char == 'r':
            self.__open_report()
        elif event.char == 'x':
            self.__close_report()

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
        self.__close_report()
        super().destroy()
        self.root.destroy()
        exit(1)


if __name__ == "__main__":
    root = Tk()
    s = Main(root)
    s.pack()
    root.mainloop()
