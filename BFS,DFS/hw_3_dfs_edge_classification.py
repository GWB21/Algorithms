from graphviz import Digraph, Graph
diGraph = Digraph(engine='neato')
diGraph.node(name ='u', label ='Node u', pos ='0,0!')
diGraph.node(name ='v', label='Node v', pos ='2,0!')
diGraph.node('w', 'Node w', pos ='4,0!')
diGraph.node('x', 'Node x', pos ='0,-2!')
diGraph.node('y', 'Node y', pos ='2,-2!')
diGraph.node('z', 'Node z', pos ='4,-2!')


diGraph.edge('u', 'v', 'Edge 1')
diGraph.edge('u', 'x', 'Edge 1')
diGraph.edge('x', 'v', 'Edge 1')
diGraph.edge('v', 'y', 'Edge 1')
diGraph.edge('y', 'x', 'Edge 1')
diGraph.edge('w', 'y', 'Edge 1')
diGraph.edge('w', 'z', 'Edge 1')
diGraph.edge('z', 'z', 'Edge 1')

diGraph


def extract_adj(body):
    nodes = set()
    adj = {}

    # 노드 추출
    for line in body:
        # '[label=' 이렇게 시작하는 것에서 노드 이름을 추출하는것이 가능합니다
        if '[label=' in line:
            node = line.split()[0].strip().lstrip('\t')
            nodes.add(node)
            adj[node] = set()

    # -> 가 들어가있으면 edge추출이 가능합니다
    for line in body:
        if '->' in line:
            source, target = line.split('->')
            source = source.strip().lstrip('\t')  # 탭 문자 제거
            target = target.split('[')[0].strip()
            adj[source].add(target)

    return adj


def dfs(adj, start_node):
    def dfs_visit(u):
        nonlocal time
        time += 1  # 시간 1증가
        d[u] = time  # d값에 할당
        color[u] = 'gray'  # gray상태로 지정
        for v in adj[u]:  # 해당 노드의 adj에 대해서 조사
            if color[v] == 'white':
                parent[v] = u  # parent 지정하고 재귀
                dfs_visit(v)
        color[u] = 'black'  # 재귀가 끝나면 black으로 지정
        time += 1  # 시간 + 1
        f[u] = time  # 시간 할당

    # 필요한 자료구조 초기화 => adj를 세트로 만들어서 순서가 좀 뒤죽박죽..
    nodes = list(adj.keys())
    color = {node: 'white' for node in nodes}
    parent = {node: None for node in nodes}
    d = {}  # discovery time dictionary
    f = {}  # finishing time dictionary
    time = 0

    # 시작 노드부터 dfs_visit 실행
    dfs_visit(start_node)

    for node in nodes:
        if color[node] == 'white':
            dfs_visit(node)

    return d, f, parent

    # edge classification... adj, d, f, parent 딕셔너리 받아서 활용


def classify_edges(adj, d, f, parent):
    classification = {}  # 세트
    for u in adj:
        for v in adj[u]:

            # 직접적 자식이라면 tree
            if parent[v] == u:
                classification[(u, v)] = 'tree'

            # tree와 비슷하나 tree가 아닌, 이 값을 충족하는 노드를 향하는 edge는 forward임
            # u.d < v.d < v.f < u.f이면 forward.. 당연함. 나중에 찾아진것은 d값 크고, f값 작음 => but tree도 이것을 충족함
            elif d[u] < d[v] < f[v] < f[u]:
                classification[(u, v)] = 'forward'

            # 나보다 먼저 찾아진 친구를 쏘는 edge. 먼저 찾아졌다면 d값은 자신보다 작고, f값은 큼.
            # 내 "직계" 조상중에 한명을 가르킬때 back 자기 자신을 가르킬때를 위해 등호추가.
            elif d[v] <= d[u] <= f[u] <= f[v]:
                classification[(u, v)] = 'back'

            # 비 트리간 간선. 즉 완전 끊어져 있는.. 것이 연결될때 cross. v.d < v.f < u.d < u.f 충족시 cross.
            else:
                classification[(u, v)] = 'cross'
    return classification


def create_graph_with_dfs(original_graph, start_node):
    adj = extract_adj(original_graph)
    d, f, parent = dfs(adj, start_node)
    edge_classification = classify_edges(adj, d, f, parent)

    new_graph = Digraph(engine='neato')
    for item in original_graph.body:
        # 노드생성을 위한 작업. 라벨 만들어내고, pos 찾아서 지정
        if '[label=' in item:  # 노드인 경우
            parts = item.strip().split()
            name = parts[0]
            label_part = item.split('[label=')[1]
            original_label = label_part.split('"')[1]

            if 'pos=' in label_part:
                pos = label_part.split('pos=')[1].split('"')[1]
                pos = pos.rstrip('!')
                x, y = map(float, pos.split(','))
                x *= 1.4
                y *= 1.1
                pos = f"{x},{y}"
                new_label = f"{original_label} d:{d.get(name)},f:{f.get(name)}"
                new_graph.node(name, label=new_label, pos=f"{pos}!")

        # 엣지관련
        if '->' in item:  # 기존에서 엣지 추출해서 엣지 이름 새기고 새 그래프에 edge 추가
            parts = item.split('->')
            source = parts[0].strip().lstrip('\t')
            target = parts[1].split('[')[0].strip()
            edge_type = edge_classification.get((source, target))
            new_graph.edge(source, target, label=edge_type)

    return new_graph


# 사용 예:
new_graph = create_graph_with_dfs(diGraph, 'u')
new_graph