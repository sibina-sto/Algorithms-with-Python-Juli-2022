from collections import deque

node = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(node + 1)]

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start_node = int(input())
destination_node = int(input())

visited = [False] * (node + 1)
parent = [None] * (node + 1)

visited[start_node] = True
queue = deque([start_node])

while queue:
    node = queue.popleft()
    if node == destination_node:
        break
    for child in graph[node]:
        if visited[child]:
            continue
        visited[child] = True
        queue.append(child)
        parent[child] = node

path = deque()
node = destination_node

while node is not None:
    path.appendleft(node)
    node = parent[node]

print(f'Shortest path length is: {len(path) - 1}')
print(*path, sep=' ')
