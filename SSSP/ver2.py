import networkx as nx
import queue
import random
from collections import defaultdict


def bidirectional_dijkstra(g, s, t, wt):
    # Find the length of the shortest path from s to t in the undirected
    # networkx Graph g with edge weight function weight, using
    # bidirectional Dijkstra. s and t must be distinct.

    def weight(x, y):
        return wt(x, y, None)

    df = defaultdict(lambda: float("inf"))  # df[v] = forward approximation of d(s, v)
    df[s] = 0
    db = defaultdict(lambda: float("inf"))  # db[v] = backward approximation of d(t, v)
    db[t] = 0

    fq = queue.PriorityQueue()  # queue of vertices to explore in foward search
    fq.put((0, s))  # queue elements have the form (priority, node)
    bq = queue.PriorityQueue()  # queue of vertices to explore in backward search
    bq.put((0, t))

    mu = float("inf")  # length of best path yet seen

    sf = set()  # nodes processed in the forward search
    sb = set()  # nodes processed in the backward search

    while (not fq.empty()) and (not bq.empty()):
        u = fq.get()[1]  # get is a "pop"
        v = bq.get()[1]
        sf.add(u)
        sb.add(v)

        for x in g.adj[u]:
            # relax u-x
            if (x not in sf) and df[x] > df[u] + weight(u, x):
                df[x] = df[u] + weight(u, x)
                fq.put((df[x], x))

            # check for a path s --- u - x --- t, and update mu
            if (x in sb) and (df[u] + weight(u, x) + db[x] < mu):
                mu = df[u] + weight(u, x) + db[x]

        for x in g.adj[v]:
            # relax v-x
            if (x not in sb) and db[x] > db[v] + weight(v, x):
                db[x] = db[v] + weight(v, x)
                bq.put((db[x], x))

            # check for a path t --- v - x --- s, and update mu
            if (x in sf) and (db[v] + weight(v, x) + df[x] < mu):
                mu = db[v] + weight(v, x) + df[x]

        # check the termination condition
        if df[u] + db[v] >= mu:
            return mu
    print("something badly wrong happened.")


def test_bidirectional_dijkstra(g, s, t, weight):
    # compare the results of calling bidirectional_dijkstra on g, s, t,
    # weight with the shortest path computed by networkx
    nxDistance = nx.shortest_path_length(g, s, t, weight)
    myDistance = bidirectional_dijkstra(g, s, t, weight)
    if nxDistance == myDistance:
        print("success! dist was", nxDistance)
    else:
        print("Fail. nx: ", nxDistance, "\t bidirectional: ", myDistance)


##############
# Test cases #
##############

# Very basic example:
#  /2\
# 1  4
#  \3/

g = nx.Graph()  # nx.Graph is undirected
g.add_nodes_from([1, 2, 3, 4])
g.add_edge(1, 2)
g.add_edge(2, 4)
g.add_edge(1, 3)
g.add_edge(3, 4)
weights = {(1, 2): 1, (2, 4): 2, (1, 3): 1, (3, 4): 1}


def w(x, y, _):
    if (x, y) in weights:
        return weights[(x, y)]
    else:
        return weights[(y, x)]


test_bidirectional_dijkstra(g, 1, 4, w)
