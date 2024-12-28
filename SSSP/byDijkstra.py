import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue
import sys

def bidirectional_dijkstra(graph, start, end):
    # 시작점에서의 거리
    dist_forward = {node: float('inf') for node in graph}
    dist_forward[start] = 0
    # 도착점에서의 거리
    dist_backward = {node: float('inf') for node in graph}
    dist_backward[end] = 0

    # 방문 여부 추적
    visited_forward = set()
    visited_backward = set()

    # 우선순위 큐 초기화
    pq_forward = PriorityQueue()
    pq_backward = PriorityQueue()
    
    pq_forward.put((0, start))
    pq_backward.put((0, end))
    
    # 경로 추적
    parent_forward = {start: None}
    parent_backward = {end: None}

    # 최단 경로 후보들을 저장할 리스트
    candidates = []

    while not pq_forward.empty() and not pq_backward.empty():
        dist_f, current_f = pq_forward.get()
        dist_b, current_b = pq_backward.get()
        
        # 현재 경로가 지금까지의 최단 경로보다 길다면 중단
        if dist_f + dist_b >= min_path_length:
            break
            
        # Forward 노드가 backward set에 있는지 확인
        if current_f in visited_backward:
            path_length = dist_forward[current_f] + dist_backward[current_f]
            candidates.append((path_length, current_f))
            
        # Backward 노드가 forward set에 있는지 확인
        if current_b in visited_forward:
            path_length = dist_forward[current_b] + dist_backward[current_b]
            candidates.append((path_length, current_b))
            
        if current_f in visited_forward:
            continue
        visited_forward.add(current_f)

        print(f"\nForward 탐색 - 현재 노드: {current_f}")
        print(f"Forward 큐 상태: {list(pq_forward.queue)}")
        print(f"Forward 방문 집합: {visited_forward}")

        if current_b in visited_backward:
            continue
        visited_backward.add(current_b)

        print(f"\nBackward 탐색 - 현재 노드: {current_b}")
        print(f"Backward 큐 상태: {list(pq_backward.queue)}")
        print(f"Backward 방문 집합: {visited_backward}")

        # 양방향에서 만나는 지점 확인
        if current_f in visited_backward and current_b in visited_forward:
            path_length = dist_forward[current_f] + dist_backward[current_f]
            if path_length < min_path_length:
                min_path_length = path_length
                meeting_point = current_f

        # Forward 방향 업데이트
        for neighbor, weight in graph[current_f].items():
            if neighbor not in visited_forward:
                new_dist = dist_forward[current_f] + weight
                if new_dist < dist_forward[neighbor]:
                    dist_forward[neighbor] = new_dist
                    parent_forward[neighbor] = current_f
                    pq_forward.put((new_dist, neighbor))

        # Backward 방향 업데이트
        for neighbor, weight in graph[current_b].items():
            if neighbor not in visited_backward:
                new_dist = dist_backward[current_b] + weight
                if new_dist < dist_backward[neighbor]:
                    dist_backward[neighbor] = new_dist
                    parent_backward[neighbor] = current_b
                    pq_backward.put((new_dist, neighbor))

    # 모든 후보들 중에서 진짜 최단 경로 찾기
    if candidates:
        min_path_length, meeting_point = min(candidates)

    # 경로 재구성
    path = []
    if meeting_point:
        # Forward path
        current = meeting_point
        while current is not None:
            path.insert(0, current)
            current = parent_forward[current]

        # Backward path
        current = parent_backward[meeting_point]
        while current is not None:
            path.append(current)
            current = parent_backward[current]

    return path, min_path_length

# 예제 그래프 생성 (DAG)
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 3, 'E': 1},
    'C': {'B': 1, 'D': 5},
    'D': {'E': 2},
    'E': {'F': 4},
    'F': {}
}


# 그래프 시각화 함수
def visualize_graph(graph, path=None):
    G = nx.DiGraph(graph)
    pos = nx.spring_layout(G)

    plt.figure(figsize=(10, 8))

    # 노드 그리기
    nx.draw_networkx_nodes(G, pos, node_color='lightblue',
                           node_size=500)

    # 엣지 그리기
    nx.draw_networkx_edges(G, pos)

    # 경로가 있다면 강조 표시
    if path:
        path_edges = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges,
                               edge_color='r', width=2)

    # 레이블 그리기
    nx.draw_networkx_labels(G, pos)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    plt.title("Directed Acyclic Graph")
    plt.axis('off')
    plt.show()


# 알고리즘 실행 및 결과 시각화
start_node = 'A'
end_node = 'F'

print(f"시작 노드: {start_node}")
print(f"도착 노드: {end_node}")
print("\n양방향 Dijkstra 알고리즘 실행:")

shortest_path, shortest_distance = bidirectional_dijkstra(graph, start_node, end_node)

print(f"\n최단 경로: {' -> '.join(shortest_path)}")
print(f"최단 거리: {shortest_distance}")

# 그래프 시각화
print("\n그래프 시각화:")
visualize_graph(graph, shortest_path)