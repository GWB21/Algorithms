class Node:
    def __init__(self, name):
        self.name = name
        self.adj_plus = []

    def add_neighbor(self, node):
        self.adj_plus.append(node)


def bfs(start_node):
    level_dictionary = {start_node.name: 0}
    parent = {start_node.name: None}
    level = 1
    frontier = [start_node]
    while frontier:
        next_list = []
        for f in frontier:
            for v in f.adj_plus:
                if v.name not in level_dictionary:
                    level_dictionary[v.name] = level
                    parent[v.name] = f.name
                    next_list.append(v)
        level += 1
        frontier = next_list
    return level_dictionary


class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)


graph = Graph()
nodelist = ['a', 's', 'd', 'f', 'z', 'x', 'c', 'v']
nodes = {}
for node_name in nodelist:
    nodes[node_name] = Node(node_name)
    graph.add_node(nodes[node_name])

def make_adj(u, v):
    nodes[u].add_neighbor(nodes[v])

make_adj('a','z')
make_adj('a','s')
make_adj('s','x')
make_adj('x','d')
make_adj('x','c')
make_adj('d','c')
make_adj('d','f')
make_adj('f','v')
make_adj('v','c')
make_adj('f','c')

print(bfs(nodes['a']))