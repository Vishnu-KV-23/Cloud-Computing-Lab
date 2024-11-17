import numpy as np

# Define the graph with nodes and edge weights
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 7},
    'C': {'A': 4, 'B': 2, 'D': 3},
    'D': {'B': 7, 'C': 3}
}

# Initialize distance vector table for each node
distance_vector = {
    'A': {'A': 0, 'B': float('inf'), 'C': float('inf'), 'D': float('inf')},
    'B': {'A': float('inf'), 'B': 0, 'C': float('inf'), 'D': float('inf')},
    'C': {'A': float('inf'), 'B': float('inf'), 'C': 0, 'D': float('inf')},
    'D': {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': 0}
}

# Update initial distances based on direct connections
for node in graph:
    for neighbor, cost in graph[node].items():
        distance_vector[node][neighbor] = cost

# Function to display the routing table
def display_routing_table():
    print("\nRouting Table:")
    for node in distance_vector:
        print(f"{node}: {distance_vector[node]}")
    print("\n")

# Display the initial routing table
print("Initial Routing Table:")
display_routing_table()

# Distance Vector Routing Algorithm
def distance_vector_routing():
    iteration = 0
    while True:
        updated = False
        print(f"Iteration {iteration + 1}:")
        for node in distance_vector:
            for neighbor in graph[node]:
                for dest in distance_vector:
                    # Calculate the new cost
                    new_cost = distance_vector[node][neighbor] + distance_vector[neighbor][dest]
                    # If new cost is cheaper, update the distance vector
                    if new_cost < distance_vector[node][dest]:
                        distance_vector[node][dest] = new_cost
                        updated = True

        # Display the routing table for this iteration
        display_routing_table()
        
        # If no updates, algorithm has converged
        if not updated:
            break
        iteration += 1

# Run the algorithm and display results
distance_vector_routing()

# Display the shortest path from A to D
print(f"Shortest path from A to D: {distance_vector['A']['D']}")


