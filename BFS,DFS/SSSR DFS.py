# def reachable_nodes(graph, start):
#     """
#     특정 시작 노드에서 도달할 수 있는 모든 노드를 반환하는 함수.
#     parent dict를 통해 방문 여부를 관리하며 반복 기반으로 수행.
#
#     Args:
#         graph (dict): 인접 리스트 형식으로 표현된 그래프.
#         start (str): 탐색 시작 노드.
#
#     Returns:
#         set: 시작 노드에서 도달 가능한 모든 노드.
#     """
#     # 방문 여부를 관리하기 위한 parent 딕셔너리
#     parent = {}
#     parent[start] = None  # 시작 노드의 부모는 None으로 설정
#
#     # 도달 가능한 노드 (결과 집합)
#     reachable = set()
#
#     # 탐색할 노드를 저장할 스택
#     stack = [start]
#
#     while stack:
#         node = stack.pop()
#
#         # 노드가 도달 가능한 집합에 없다면 추가
#         if node not in reachable:
#             reachable.add(node)
#
#             # 현재 노드에서 갈 수 있는 모든 이웃 탐색
#             for neighbor in graph[node]:
#                 if neighbor not in parent:
#                     parent[neighbor] = node  # 부모 설정
#                     stack.append(neighbor)  # 스택에 추가
#
#     return reachable
#

# #
# # start = 'A'
# #
# # reachable = reachable_nodes(graph, start)
# # print("Reachable Nodes:", reachable)
#
# graph = {
#     'A': ['B'],
#     'B': ['C'],
#     'C': [],
#     'D': ['E'],
#     'E': []
# }

#
# start = 'A'
# reachable = reachable_nodes(graph, start)
# print("Reachable Nodes:", reachable)


parent = {}
parent['A'] = None
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}
def visit(u):
    for v in graph[u]:
        if v not in parent:
            parent[v] = u
            visit(v)

visit('A')
print(parent)