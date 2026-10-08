graph = {
  'A': {'B': 4, 'C': 2},
  'B': {'A': 4, 'C': 1, 'D': 5},
  'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
  'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
  'E': {'C': 10, 'D': 2, 'F': 3},
  'F': {'D': 6, 'E': 3}
}

def prims(graph, start):
  visited = {start}
  edges = sorted((w, start, nbr) for nbr, w in graph[start].items())
  total = 0
  while edges and len(visited) < len(graph):
    w, u, v = edges.pop(0)
    if v in visited:
      continue
    visited.add(v)
    total += w
    print(u, "-", v, ":", w)
    for nbr, wt in graph[v].items():
      if nbr not in visited:
        edges.append((wt, v, nbr))
        edges.sort()
  print("Total cost:", total)

prims(graph, 'A')
