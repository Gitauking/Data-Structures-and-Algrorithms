#types of graphs include unidirected(two way) Directed(oneway) and weighted graphs

#graph traversal algorithm 


#Breadth-first search

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex= queue.popleft()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            queue.extend(graph[vertex])


#Depth-first search

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    if start not in visited:
        print(start)
        visited.add(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)
