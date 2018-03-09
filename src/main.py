from tkinter import Tk, Toplevel, Menu, Scale, Canvas, Button
from tkinter.ttk import Frame, Labelframe
import matplotlib.pyplot as plt

from utils.figure import draw_figure

from config import *
from utils.pagerank import pagerank
from utils.edges import randEdges
from graphviewer import GraphViewer
from report import Report

class Main(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = self.winfo_toplevel()
        self.root.option_add("*Font", "serif 10 bold")
        self.root.title(" ".join((APPNAME, VERSION, "| Main")))
        self.root.bind('<Key>', self.__keys) 

        # Menu
        menubar = Menu(self.root)
        self.windowsmenu = Menu(menubar, tearoff=0)
        self.windowsmenu.add_command(label="[ ] Report window", command=self.__toggle_report)
        self.windowsmenu.add_command(label="Plot current model", command=self.__plot)
        self.windowsmenu.add_separator()
        self.windowsmenu.add_command(label="Quit", command=self.destroy)
        menubar.add_cascade(label="Windows", menu=self.windowsmenu)
        settingmenu = Menu(menubar, tearoff=0)
        settingmenu.add_command(label="Spectrum range")
        settingmenu.add_command(label="Color scheme")
        menubar.add_cascade(label="Setting", menu=settingmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help", command=self.__help)
        helpmenu.add_separator()
        helpmenu.add_command(label="About", command=self.__about)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.root.config(menu=menubar)

        # Scale
        ctrls = Labelframe(self, text='Control', relief='ridge')
        self.e = Scale(ctrls, from_=E_MIN, to=E_MAX, label='Links',
                bd=1, width=7, length=150, orient='horizontal')
        self.d = Scale(ctrls, from_=D_MIN, to=D_MAX, label='Pages',
                bd=1, width=7, length=150, orient='horizontal')
        self.e.set(E)
        self.d.set(D)
        self.e.config(command=self.__refresh)
        self.d.config(command=self.__refresh)
        self.e.pack(side='left')
        self.d.pack(side='right')
        self.r_win = False
        ctrls.pack(side='top', anchor='e', padx=7, pady=5)

        # initialize model
        self.generate_model()
        self.c = GraphViewer(self, D, self.edge_counts, self.pagerank)
        self.c.pack()

        # open windows
        self.__toggle_report()
        #self.__toggle_search()

    def generate_model(self):
        edges, self.edge_counts = randEdges(self.d.get(), self.e.get())
        self.pagerank = pagerank(edges)

    def render(self):
        self.generate_model()
        self.c.render(self.d.get(), self.edge_counts, self.pagerank)
        try: self.r.render(self.pagerank, self.edge_counts, self.d.get(), self.e.get())
        except: pass

    def __refresh(self, value=None):
        self.generate_model()
        self.render()

    def __toggle_report(self):
        if self.r_win:
            try: self.r.destroy()
            except: pass
            self.r_win = False
            self.windowsmenu.entryconfig(0, label='[ ] Report window')
            return 
        self.r = Report(Toplevel(self))
        self.r.pack()
        self.r.render(self.pagerank, self.edge_counts, self.d.get(), self.e.get())
        self.r_win = True
        self.windowsmenu.entryconfig(0, label='[•] Report window ')

    def __plot(self):
        try: self.plot_root.destroy()
        except: pass
        plt.clf()
        plt.xticks(list(range(0, self.pagerank[1], 2)))
        ts =  list(range(self.pagerank[1]))
        ps = [[p[k] for p in self.pagerank[0]] for k in self.pagerank[0][0].keys()]
        fig = [plt.plot(ts, ps[i]) for i in range(len(ps))][-1][-1].figure
        _, _, w, h = fig.bbox.bounds
        fig.text(0,0,'PageRank vector at each iteration')

        self.plot_root = Toplevel(self)
        self.plot_root.title(" ".join((APPNAME, VERSION, "| Plot")))
        c = Canvas(self.plot_root, width=w, height=h)
        self.fig = draw_figure(c, fig)
        c.pack()
        self.focus_force()

    def __keys(self, event):
        if event.char == 'q':
            self.destroy()

        elif event.char == 'r':
            self.__toggle_report()
        elif event.char == 'p':
            self.__plot()
        elif event.char == 'x':
            try: self.plot_root.destroy()
            except: pass
            plt.clf()
        elif event.char == 's':
            self.__toggle_search()

        elif event.char == 'n':
            self.__refresh()

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
    
    def __help(self):
        pass
    
    def __about(self):
        pass
            
    def destroy(self):
        try: self.r.destroy()
        except: pass
        super().destroy()
        self.root.destroy()
        exit(1)


if __name__ == "__main__":
    main = Tk()
    s = Main(main)
    s.pack()
    main.mainloop()
