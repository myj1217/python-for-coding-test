from collections import deque

# 도시의 개수, 도로의 개수, 거리정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 모든 도로정보 입력받기
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)