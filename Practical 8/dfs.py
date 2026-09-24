graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}

def dfs(graph, start):
  visited, stack = set(), [start]
  while stack:
    node = stack.pop()
    if node not in visited:
      visited.add(node)
      print(node, end=' ')
      stack.extend(reversed(graph[node]))

dfs(graph, "A") 
