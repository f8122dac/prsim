from random import shuffle

# returns edges in tuple, and edge counts for each tuple of edges
def randEdges(d, e):
    edges = []
    for _ in range(e):
        l = list(range(d))
        shuffle(l)
        edges.append(tuple(l[:2]))
    return tuple(edges), {e: edges.count(e) for e in set(edges)}
