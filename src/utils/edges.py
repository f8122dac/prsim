from random import shuffle

def randEdges(d, e):
    res = []
    for _ in range(e):
        l = list(range(d))
        shuffle(l)
        res.append(tuple(l[:2]))
    return tuple(res)
