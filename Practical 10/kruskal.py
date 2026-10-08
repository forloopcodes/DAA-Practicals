edges = [
  (4, 'A', 'B'), (2, 'A', 'C'), (1, 'B', 'C'),
  (5, 'B', 'D'), (8, 'C', 'D'), (10, 'C', 'E'),
  (2, 'D', 'E'), (6, 'D', 'F'), (3, 'E', 'F')
]
vertices = ['A', 'B', 'C', 'D', 'E', 'F']

def find(parent, v):
  while parent[v] != v:
    parent[v] = parent[parent[v]]
    v = parent[v]
  return v

def kruskal(edges, vertices):
  parent = {v: v for v in vertices}
  total = 0
  for w, u, v in sorted(edges):
    pu, pv = find(parent, u), find(parent, v)
    if pu != pv:
      parent[pu] = pv
      total += w
      print(u, "-", v, ":", w)
  print("Total cost:", total)

kruskal(edges, vertices)
