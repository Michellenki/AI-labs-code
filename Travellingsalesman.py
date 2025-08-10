import itertools

# Define the distance matrix
distances = [
    [0, 10, 15, 20],  # Node 1
    [10, 0, 35, 25],  # Node 2
    [15, 35, 0, 30],  # Node 3
    [20, 25, 30, 0]   # Node 4
]

def calculate_tour_distance(tour):
    total_distance = 0
    for i in range(len(tour)):
        j = (i + 1) % len(tour)
        total_distance += distances[tour[i] - 1][tour[j] - 1]
    return total_distance

# All nodes
nodes = [1, 2, 3, 4]
min_distance = float('inf')
best_tour = []

# Try all permutations starting from node 1
for perm in itertools.permutations(nodes[1:]):
    tour = [1] + list(perm)
    distance = calculate_tour_distance(tour)
    if distance < min_distance:
        min_distance = distance
        best_tour = tour

print("Shortest tour:", best_tour)
print("Minimum distance:", min_distance)