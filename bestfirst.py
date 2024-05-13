# Define the graph as an adjacency list
graph = {
    'A': [('B', 3), ('C', 6), ('D', 5)],
    'B': [('A', 3), ('E', 9), ('F', 8)],
    'C': [('A', 6), ('G', 12), ('H', 14)],
    'D': [('A', 5), ('I', 7)],
    'E': [('B', 9)],
    'F': [('B', 8)],
    'G': [('C', 12)],
    'H': [('C', 14)],
    'I': [('D', 7), ('J', 5), ('K', 6)],
    'J': [('I', 5)],
    'K': [('I', 6)]
}

# Function for implementing Best First Search
def best_first_search(actual_Src, target, graph):
    visited = set()  # Keep track of visited nodes
    pq = [(0, actual_Src)]  # Priority queue to store nodes with their cost
    while pq:
        
        cost, node = pq.pop(0)  # Get the node with the lowest cost
        print(node, end=" ")  # Print the node
        visited.add(node)  # Mark the node as visited
        if node == target:
            break
        
        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                pq.append((edge_cost, neighbor))  # Add unvisited neighbors to the queue
        pq.sort()  # Sort the priority queue based on cost
    print()

# Define the source and target nodes
source = 'A'
target = 'K'

# Call the function to perform Best First Search
best_first_search(source, target, graph)
