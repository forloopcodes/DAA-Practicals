INF = 999
graph = [
  [0, 5, INF, 10],
  [INF, 0, 3, INF],
  [INF, INF, 0, 1],
  [INF, INF, INF, 0]
]

def floyd_warshall(graph):
  n = len(graph)
  dist = [row[:] for row in graph]
  for k in range(n):
    for i in range(n):
      for j in range(n):
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
  return dist

for row in floyd_warshall(graph):
  print(row)
