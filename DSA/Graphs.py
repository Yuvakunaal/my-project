# Depth First Search (DFS)
def DFS(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            neighbors = graph[node]
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)

def run():
    graph = {
        "A": {"B", "C"},
        "B": {"A", "D", "E"},
        "C": {"A", "F"},
        "D": {"B"},
        "E": {"B", "F"},
        "F": {"C", "E"}
    }
    DFS(graph, "A")
    print()
run()
