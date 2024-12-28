adj = {
    'a' : ['b','c'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : [],
}

def bfs(s):
    parent ={s:None}
    level = {s : 0}
    frontier = [s]
    cur_level = 0

    while frontier:
        next = []
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    parent[v] = u
                    level[v] = cur_level + 1
                    next.append(v)
        frontier = next
        cur_level += 1

    return level

print(bfs('a'))