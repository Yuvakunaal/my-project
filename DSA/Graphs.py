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

# Breadth First Search (BFS) - Normal :-
def BFS_N(graph):
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
    print()
run()
