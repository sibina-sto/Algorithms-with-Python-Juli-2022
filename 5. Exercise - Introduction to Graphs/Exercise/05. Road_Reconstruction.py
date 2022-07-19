# Variant 1

def dfs(node, graph, visited):
    if visited[node]:
        return
    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited)


nodes_count = int(input())
edges_count = int(input())

graph = []
[graph.append([]) for _ in range(nodes_count)]

edges = []

for _ in range(edges_count):
    first, second = [int(x) for x in input().split(" - ")]
    graph[first].append(second)
    graph[second].append(first)
    edges.append((min(first, second), max(first, second)))

# important_streets = []
print(f'Important streets:')

for first, second in edges:
    graph[first].remove(second)
    graph[second].remove(first)

    visited = [False] * nodes_count
    dfs(0, graph, visited)

    if not all(visited):
        print(first, second)

    graph[first].append(second)
    graph[second].append(first)

# Variant 2

# from collections import defaultdict

# def dfs(node, graph, visited, component):
#     if visited[node] == True:
#         return
#     visited[node] = True
#     for child in graph[node]:
#         dfs(child, graph, visited, component)
#     component.append(node)

# cities = int(input())
# streets = int(input())

# graph = defaultdict(list)
# edges = []

# for _ in range(streets):
#     edge_parts = input().split(' - ')
#     edges.append(edge_parts)
#     graph[edge_parts[0]].append(edge_parts[1])
#     graph[edge_parts[1]].append(edge_parts[0])

# important_streets = []

# for edge in sorted(edges):
#     start_node = edge[0]
#     end_node = edge[1]
#     graph[start_node].remove(end_node)
#     graph[end_node].remove(start_node)
#     component = []
#     visited = {}
#     for node in graph.keys():
#         visited[node] = False
#     dfs(start_node, graph, visited, component)
#     if end_node not in component:
#         sorted_edge = sorted([start_node, end_node])
#         important_streets.append(f"{sorted_edge[0]} {sorted_edge[1]}")
#     graph[start_node].append(end_node)
#     graph[end_node].append(start_node)

# print("Important streets:")
# [print(street) for street in important_streets]
