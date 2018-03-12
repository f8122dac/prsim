from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def draw_figure(master, pagerank):
    #fig = Figure(figsize=(5,5))
    fig = Figure()
    ax = fig.add_subplot(111)
    ax.set_xticklabels(list(range(0, pagerank[1]+1, 3)))
    ax.set_title('PageRank Values for Each Iteration')
    ax.set_xlabel('n-th iteration')
    ax.set_ylabel('PageRank value')

    ts =  list(range(pagerank[1]+1))
    ps = [[p[k] for p in pagerank[0]] for k in pagerank[0][0].keys()]
    for i in range(len(ps)):
        ax.plot(ts, ps[i])

    canvas = FigureCanvasTkAgg(fig, master=master)
    canvas.get_tk_widget().pack()


