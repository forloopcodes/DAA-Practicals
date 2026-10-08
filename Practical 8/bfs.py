from collections import deque

graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}

def bfs(graph, start, target):
  visited = {start}
  q = deque([start])
  if start == target:
    print(start)
    return
  while q:
    node = q.popleft()
    print(node, end=" ")
    for nbr in graph[node]:
      if nbr not in visited:
        visited.add(nbr)
        q.append(nbr)

bfs(graph, "A", "F")
