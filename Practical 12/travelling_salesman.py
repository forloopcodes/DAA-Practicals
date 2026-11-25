from itertools import permutations

graph = [
  [0, 10, 15, 20],
  [10, 0, 35, 25],
  [15, 35, 0, 30],
  [20, 25, 30, 0]
]

def tsp(graph):
  best = float('inf')
  for path in permutations(range(1, len(graph))):
    cost = graph[0][path[0]] + graph[path[-1]][0]
    cost += sum(graph[path[i]][path[i + 1]] for i in range(len(path) - 1))
    if cost < best:
      best, route = cost, (0,) + path + (0,)
  return route, best

route, cost = tsp(graph)
print("Path:", " -> ".join(map(str, route)))
print("Cost:", cost)
