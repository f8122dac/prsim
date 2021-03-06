from tkinter import Canvas, LAST, ALL

from math import pi, sin, cos, log, atan, degrees, sqrt

from config import default_color
from utils.color import schemes, spectrum 
from utils.point import Point

class GraphViewer(Canvas):
    @staticmethod
    def ngon(d, r, offset):
        offset += 100 
        r *= 1+d/240
        dtheta = (2*pi)/d
        offset *= (1-0.0075*(d-2))
        return tuple((r*cos(k*dtheta)+r+offset, r*sin(k*dtheta)+r+offset) for k in range(d))

    def __init__(self, master, degree, edge_counts, pagerank, color_scheme=None, radius=250, offset=50):
        self.color = schemes[color_scheme or default_color]
        self.radius = radius
        self.offset = offset
        super().__init__(master, 
                width=radius*2.85+offset, height=radius*2.85+offset, 
                bg=self.color['bg'])
        self.render(degree, edge_counts, pagerank)

    def render(self, degree, edge_counts, pagerank):
        self.delete(ALL)
        self.size = int(60-0.7760*(degree-2))//2
        self.nodes = self.ngon(degree, self.radius, self.offset)
        self.edge_counts = edge_counts
        self.pr = pagerank[0][-1] 
        self.pr_vals = tuple(reversed(sorted(set(self.pr.values()))))
        self.spectrum = spectrum(len(self.pr_vals))
        
        self.render_nodes()
        self.render_edges()
        self.render_colorchart(self.offset-40, self.offset-40, self.offset+540, 13)

    def render_nodes(self):
        for idx, (x,y) in enumerate(self.nodes):
            rank = self.pr_vals.index(self.pr[idx])
            node_color, text_color = self.spectrum[rank], self.color['text']
            width = round(log(self.pr[idx]*370 + 1))
            self.create_rectangle(x-self.size, y-self.size, 
                    x+self.size, y+self.size, fill=node_color, width=width)
            self.create_text(x, y, text=str(idx), fill=text_color) 

    def render_edges(self):
        L = 157
        l = self.size+2
        for (tail, head), count in self.edge_counts.items():
            if tail is not head:
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

    def render_colorchart(self, x, y, l, w):
        d = l/len(self.spectrum)
        label = (self.create_rectangle(x+w+5,y, x+w+37, y+24, fill='#DBDBDB'), 
                 self.create_rectangle(x+w+5, y+l-24, x+w+37, y+l, fill='#DBDBDB'))
        text = self.create_text(x+w+21,y+12, text='High'), self.create_text(x+w+21, y+l-12, text='Low')
        return label + text + \
               tuple(self.create_rectangle(x, y+d*k, x+w, y+d*(k+1), fill=color, width=1) 
                       for k, color in enumerate(self.spectrum))


