from IPython.display import Image
from graphviz import Digraph, Graph
unDiGraph = Graph(engine='neato')
unDiGraph.node(name ='r', label ='Node r', pos ='0,0!')
unDiGraph.node(name ='s', label='Node s', pos ='2,0!')
unDiGraph.node('t', 'Node t', pos ='4,0!')
unDiGraph.node('u', 'Node u', pos ='6,0!')
unDiGraph.node('v', 'Node v', pos ='0,-2!')
unDiGraph.node('w', 'Node w', pos ='2,-2!')
unDiGraph.node('x', 'Node x', pos ='4,-2!')
unDiGraph.node('y', 'Node y', pos ='6,-2!')


unDiGraph.edge('r', 's', 'Edge 1')
unDiGraph.edge('r', 'v', 'Edge 1')
unDiGraph.edge('s', 'w', 'Edge 1')
unDiGraph.edge('w', 't', 'Edge 1')
unDiGraph.edge('t', 'u', 'Edge 1')
unDiGraph.edge('t', 'x', 'Edge 1')
unDiGraph.edge('w', 'x', 'Edge 1')
unDiGraph.edge('x', 'y', 'Edge 1')
unDiGraph.edge('u', 'x', 'Edge 1')
unDiGraph.edge('u', 'y', 'Edge 1')

## digraph 라이브러리 자체 내에서 string parsing을 통해서 adj를 뽑아내는식으로 만들어봤습니다.
# dot.body를 프린트하면 스트링리스트형태로 구성되어있는걸 볼 수 있어서 이런식으로 해봤습니다.
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

    # -- 가 들어가있으면 edge추출이 가능합니다
    for line in body:
        if '--' in line:
            source, target = line.split('--')
            source = source.strip().lstrip('\t')  # 탭 문자 제거
            target = target.split('[')[0].strip()
            adj[source].add(target)
            adj[target].add(source)  # 양방향이기에 둘다에게 추가

    return adj

def bfs_with_dict(adj, start):
    levels = {start: 0}  #level 딕셔너리
    frontier = {start}  #프론티어세트
    current_level = 0   #레벨 기록을 위한 private 변수

    while frontier: # 다음에 정복할 프론티어가 있을 경우에만 반복!
        next_frontier = set() #다음 정복 프론티어 저장 프라이빗 변수
        for node in frontier: # 프론티어 개수만큼 반복
            for neighbor in adj[node]: # 개별 프론티어의 adj에 대한 검사 진행
                if neighbor not in levels: # adj가 레벨딕셔너리에에 있지 않다면
                    levels[neighbor] = current_level + 1  # 레벨 딕셔너리에 current_level +1 해서 등록
                    next_frontier.add(neighbor) # 다음 프론티어로 등록
        frontier = next_frontier # 다음 프론티어 받아서 등록하기
        current_level += 1 # 레벨 1 올려주기

    return levels #레벨 딕셔너리 리턴해주기

def create_graph_with_levels(original_graph, levels):
    new_graph = Graph(engine='neato')
    for node in original_graph.body:

        #label 정보 추출하기
        if '[label=' in node and '--' not in node:
            parts = node.strip().split()
            name = parts[0]
            label_part = node.split('[label=')[1]
            original_label = label_part.split('"')[1]

        # pos 정보 추출하기
        if 'pos=' in label_part:
            pos = label_part.split('pos=')[1].split('"')[1]
            pos = pos.rstrip('!')
            x, y = map(float, pos.split(','))
            x *= 1.4  # 노드 간격 조정
            y *= 1
            pos = f"{x},{y}"

        new_label = f"{original_label} level : {levels[name]}"
        #새 그래프 노드 생성
        new_graph.node(name, label=new_label, pos=f"{pos}!")

    #엣지 뽑아내서 새 그래프 엣지로 추가해주기
    for edge in original_graph.body:
        if '--' in edge:
            parts = edge.split('--')
            source = parts[0].strip().lstrip('\t')
            target = parts[1].split('[')[0].strip()
            new_graph.edge(source, target, '')

    return new_graph

# 인접 리스트 추출
adj = extract_adj(unDiGraph)

# BFS 수행 (시작 노드는 's'로 가정)
levels = bfs_with_dict(adj, 's')

# 레벨 정보가 포함된 새 그래프 생성
new_graph = create_graph_with_levels(unDiGraph, levels)
new_graph
