distance = [
    [0, 10, 15],
    [10, 0, 20],
    [15, 20, 0]
]

n = len(distance)
visited = [False] * n
visited[0] = True

cost = 0
current = 0

for i in range(n - 1):
    next_city = -1
    min_distance = float('inf')

    for j in range(n):
        if not visited[j] and distance[current][j] < min_distance:
            min_distance = distance[current][j]
            next_city = j

    cost += min_distance
    visited[next_city] = True
    current = next_city

cost += distance[current][0]

print("Total distance:", cost)
