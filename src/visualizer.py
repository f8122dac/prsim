from tkinter import Canvas, LAST, ALL

from math import pi, sin, cos, log, atan, degrees, sqrt

from config import default_color
from utils.color import schemes, spectrum 
from utils.point import Point

class Visualizer(Canvas):
    @staticmethod
    def ngon(d, r, offset):
        offset += 100 
        r *= 1+d/240
        dtheta = (2*pi)/d
        offset *= (1-0.0075*(d-2))
        return tuple((r*cos(k*dtheta)+r+offset, r*sin(k*dtheta)+r+offset) for k in range(d))

    def __init__(self, master, degree, edges, pr, color_scheme=None, radius=250, offset=0):
        self.color = schemes[color_scheme or default_color]
        self.radius = radius
        self.offset = offset
        super().__init__(master, 
                width=radius*2.85+offset, height=radius*2.85+offset, 
                bg=self.color['bg'])
        self.render(degree, edges, pr)

    def render(self, degree, edges, pr):
        self.delete(ALL)
        self.size = int(60-0.7760*(degree-2))//2
        self.edges = {e: edges.count(e) for e in set(edges)}
        self.nodes = self.ngon(degree, self.radius, self.offset)
        self.pr = pr
        self.pr_vals = tuple(sorted(set(pr.values())))
        self.ranks = {val: rank for rank, val in enumerate(self.pr_vals)}
        
        self.render_nodes()
        self.render_edges()
        self.render_colorchart(10, 10, 590, 13, spectrum(len(self.pr_vals)))

    def render_nodes(self):
        sp =  spectrum(len(self.pr_vals))
        for idx, (x,y) in enumerate(self.nodes):
            if idx in self.pr.keys():
                node_color, text_color = sp[self.ranks[self.pr[idx]]], self.color['text']
                width = log(self.pr[idx]*370 + 1)
            else:
                node_color, text_color = self.color['isol_node'], self.color['isol_text']
                width = 0
            self.create_rectangle(x-self.size, y-self.size, x+self.size, y+self.size, fill=node_color, width=width)
            self.create_text(x, y, text=str(idx), fill=text_color) 

    def render_edges(self):
        L = 157
        l = self.size+2
        for (head, tail), count in self.edges.items():
            h, t = Point(*self.nodes[head]), Point(*self.nodes[tail])
            s = (h-t).norm()
            h,t = t+(h-t)*l/s, h-(h-t)*l/s

            theta = (h-t).ang()
            d = L/(count+1)
            pl = (h+t)/2 + Point(cos(theta), -sin(theta))*(L/2)
            ps = [pl + Point(-cos(theta),sin(theta))*d*(k+1) for k in range(count)]

            for p in ps:
                self.create_line(*h.crd(), *p.crd(), *t.crd(), 
                    fill=self.color['edges'], width=1, smooth=True, 
                    arrow=LAST, arrowshape=(8,9,4))

    def render_colorchart(self, x, y, l, w, c):
        d = l/len(c)
        label = (self.create_rectangle(x+w+5,y, x+w+37, y+24, fill='#DBDBDB'), 
                 self.create_rectangle(x+w+5, y+l-24, x+w+37, y+l, fill='#DBDBDB'))
        text = self.create_text(x+w+21,y+12, text='High'), self.create_text(x+w+21, y+l-12, text='Low')
        return label + text + \
               tuple(self.create_rectangle(x, y+d*k, x+w, y+d*(k+1), fill=color, width=1) for k, color in enumerate(c)) 
                
