adj = {
    'a': ['b', 'd'],
    'b': ['e'],
    'c': ['e', 'f'],
    'd': ['b'],
    'e': ['a', 'd'],
    'f': [],
}

edge = {}
color = {}
parent = {}
d = {}
f = {}

def dfs(s):
    for v in adj:
        color[v] = "WHITE"
        parent[v] = None
    time = 0  # `time`은 dfs 함수의 지역 변수로 정의

    def dfs_visit(s):
        nonlocal time  # 바깥 `dfs` 함수의 time을 사용하겠다고 선언
        time += 1
        color[s] = "GRAY"
        d[s] = time
        for u in adj[s]:
            if color[u] == "WHITE":
                parent[u] = s
                edge[(s, u)] = "TREE"
                dfs_visit(u)
            elif color[u] == "GRAY":
                edge[(s, u)] = "BACK"
            elif d[s] < d[u]:  # Forward edge
                edge[(s, u)] = "FORWARD"
            else:  # Cross edge
                edge[(s, u)] = "CROSS"
        time += 1
        color[s] = "BLACK"
        f[s] = time

    for v in adj:
        if color[v] == "WHITE":
            dfs_visit(v)

    return parent, edge

par, ed = dfs('a')
print("Parent:", par)
print("Edges:", ed)
