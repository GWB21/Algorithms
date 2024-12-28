adj = {
    'a' : ['b', 'e', 'f'],
    'b' : ['c','g'],
    'c' : ['d'],
    'd' : [],
    'e' : ['d'],
    'f' : ['g'],
    'g' : []
}

weight = {
    ('a', 'b') : 3,
    ('a', 'e') : -1,
    ('a', 'f') : 1,
    ('b', 'c') : 2,
    ('b', 'g') : 4,
    ('c', 'd') : -7,
    ('e', 'd') : 2,
    ('f', 'g') : -3,
    ('g', 'a') : 1,
}

d = {}
parent = {}

def bellman_ford(s):
    def init_single_s(s):
        for v in adj:
            parent[v] = None
            d[v] = float('inf')
        d[s] = 0

    def relaxation(u,v):
        if d[v] > d[u] + weight[(u, v)]:
            d[v] = d[u] + weight[(u, v)]
            parent[v] = u

    init_single_s(s)

    #개수 -1개 만큼 반복할것.
    #노드가 5개라면 4번 시도.
    for _ in range(len(adj) - 1):
        for (u, v) in weight:
            relaxation(u, v)

    for (u, v) in weight:
        if d[v] > d[u] + weight[(u, v)]:
            return False

    return True, d

print(bellman_ford('a'))