# https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python
graph = {
  'A': ['B','C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': [],
  'E': ['F'],
  'F': []
}

visited = []
queue = []


def bfs(visited, graph, node):
    visited.append(node)  # List to keep track of visited nodes.
    queue.append(node)    # Initialize a queue

    while queue:
        s = queue.pop(0)
        print(s)

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


bfs(visited, graph, 'A')