def dfs(s, adj):
    time = 0
    # 기본 구조 초기화
    color = {v: "WHITE" for v in adj}  # WHITE: 방문 전, GRAY: 방문 중, BLACK: 방문 완료
    parent = {v: None for v in adj}  # 부모 노드 맵
    d = {}  # 발견 시간
    f = {}  # 완료 시간

    def dfs_visit(u):
        nonlocal time
        color[u] = "GRAY"
        time += 1
        d[u] = time

        for v in adj[u]:
            if color[v] == "WHITE":  # 자식 노드를 방문
                parent[v] = u
                dfs_visit(v)

        color[u] = "BLACK"
        time += 1
        f[u] = time

    # Full - DFS 시작
    for v in adj:
        if color[v] == "WHITE":
            dfs_visit(v)

    return parent, d, f


def classify_edges(adj, parent, d, f):
    edges = {}
    for u in adj:
        for v in adj[u]:
            if parent[v] == u:
                edges[(u, v)] = "TREE"  # 트리 간선
            elif d[u] < d[v] < f[v] < f[u]:
                edges[(u, v)] = "FORWARD"  # 순방향 간선
            elif d[v] < d[u] < f[u] < f[v]:
                edges[(u, v)] = "BACK"  # 백 간선
            else:
                edges[(u, v)] = "CROSS"  # 교차 간선
    return edges


# 예제 그래프 (DAG)
adj = {
    "a": ["b", "c"],
    "b": ["e"],
    "c": ["e"],
    "e": []
}

# DFS와 간선 분류 실행
start_node = "a"
parent, discovery_times, finish_times = dfs(start_node, adj)
classified_edges = classify_edges(adj, parent, discovery_times, finish_times)

# 출력
print("Parent Map:", parent)
print("Discovery Times:", discovery_times)
print("Finish Times:", finish_times)
print("Edge Classification:", classified_edges)