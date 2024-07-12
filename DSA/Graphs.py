from collections import deque

# Depth First Search (DFS) - Normal :-
def DFS_N(graph, start):
    visited = set()  # all visited nodes will be stored here
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)  # Making node as visited
            print(node, end=" ")
            neighbors = sorted(graph[node], reverse=True)  # Sort neighbors to ensure consistent order
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)

# Depth First Search (DFS) - Recursion :-
def DFS_R(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in sorted(graph[node]):
            DFS_R(graph, neighbor, visited)

# Breadth First Search (BFS) - Iterative :-
def BFS_N(graph, start):
    visited = set()  # All visited nodes will be stored here
    queue = [start]
    visited.add(start)
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        neighbors = graph[node]
        for neighbor in sorted(neighbors):  # Sort neighbors to ensure consistent order
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Breadth First Search (BFS) - Recursion :-
def BFS_recursive(graph, queue, visited):
    if not queue:
        return

    node = queue.popleft()
    print(node, end=" ")

    for neighbor in sorted(graph[node]):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
    
    BFS_recursive(graph, queue, visited)

def BFS_R(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    BFS_recursive(graph, queue, visited)

def run():
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"]
    }
    print("DFS - Normal = ",end="")
    DFS_N(graph, "A")
    print("\nDFS - Recursion = ",end="")
    DFS_R(graph, "A")
    print("\nBFS - Normal = ",end="")
    BFS_N(graph, "A")
    print("\nBFS - Recursion = ",end="")
    BFS_R(graph, "A")
    print()
    
run()
