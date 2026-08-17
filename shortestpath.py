import numpy as np
import heapq

cities = ["Delhi", "Jaipur", "Agra", "Lucknow", "Chandigarh"]
n = len(cities)
INF = float("inf")

dist_matrix = np.array([
    [0,   280, 233, 555, 250],   # Delhi
    [280, 0,   238, INF, INF],   # Jaipur
    [233, 238, 0,   330, INF],   # Agra
    [555, INF, 330, 0,   INF],   # Lucknow
    [250, INF, INF, INF, 0],     # Chandigarh
])

def dijkstra(start_city):
    start = cities.index(start_city)

    dist = [INF] * n
    dist[start] = 0
    visited = [False] * n
    prev = [None] * n 


    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)

        if visited[u]:
            continue
        visited[u] = True

        for v in range(n):
            weight = dist_matrix[u][v]
            if weight == INF or weight == 0 and u != v:
                continue
            if u == v:
                continue

            new_dist = d + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u
                heapq.heappush(pq, (new_dist, v))

    return dist, prev

def reconstruct_path(prev, start_city, end_city):
    end = cities.index(end_city)
    start = cities.index(start_city)
    path = []
    node = end
    while node is not None:
        path.append(node)
        if node == start:
            break
        node = prev[node]
    path.reverse()
    return [cities[i] for i in path]

# Example
start_city = "Delhi"
distances, prev = dijkstra(start_city)

print(f"Shortest distances from {start_city}:\n")
for city, d in zip(cities, distances):
    print(f"  {start_city} -> {city}: {d} km")

print(f"\nShortest path {start_city} -> Lucknow:")
print(" -> ".join(reconstruct_path(prev, start_city, "Lucknow")))

print(f"\nShortest path {start_city} -> Jaipur (no direct road needed via other city here):")
print(" -> ".join(reconstruct_path(prev, start_city, "Jaipur")))