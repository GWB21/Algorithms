from collections import defaultdict, deque

class DAG:
    def __init__(self):
        self.graph = defaultdict(list)
        self.indegree = defaultdict(int)
    
    def add_edge(self, u, v, weight=1):
        """그래프에 가중치가 있는 간선 추가"""
        self.graph[u].append((v, weight))
        self.indegree[v] += 1
        if u not in self.indegree:
            self.indegree[u] = 0

    def topological_sort(self):
        """위상 정렬 수행"""
        queue = deque()
        result = []
        
        # 진입차수가 0인 노드를 큐에 추가
        for node in self.indegree:
            if self.indegree[node] == 0:
                queue.append(node)
        
        # 위상 정렬 수행
        while queue:
            current = queue.popleft()
            result.append(current)
            
            for next_node, _ in self.graph[current]:
                self.indegree[next_node] -= 1
                if self.indegree[next_node] == 0:
                    queue.append(next_node)
        
        return result
    def shortest_path(self, start):
        """start 노드에서 시작하는 최단 경로 찾기"""
        # 위상 정렬 수행
        sorted_nodes = self.topological_sort()
        
        # DP 테이블 초기화 (무한대로 초기화)
        dp = defaultdict(lambda: float('inf'))
        dp[start] = 0
        
        # 위상 정렬된 순서대로 최단 경로 계산
        for node in sorted_nodes:
            if dp[node] != float('inf'):
                for next_node, weight in self.graph[node]:
                    dp[next_node] = min(dp[next_node], dp[node] + weight)
        
        return dp

# 사용 예시
if __name__ == "__main__":
    dag = DAG()
    
    # 예제 그래프 생성
    dag.add_edge(1, 2, 3)
    dag.add_edge(1, 3, 6)
    dag.add_edge(2, 4, 4)
    dag.add_edge(2, 5, 2)
    dag.add_edge(3, 5, 1)
    dag.add_edge(4, 6, 5)
    dag.add_edge(5, 6, 4)
    
    # 시작 노드에서부터 각 노드까지의 최단 경로 계산
    start_node = 1
    shortest_paths = dag.shortest_path(start_node)
    
    # 결과 출력
    print(f"노드 {start_node}에서 시작하는 최단 경로:")
    for node, distance in shortest_paths.items():
        if distance != float('inf'):
            print(f"노드 {node}까지의 최단 거리: {distance}")