import heapq

INF = int(1e9)
n, m = map(int, input().split())
grids = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    grids[a].append((b, 1))
    grids[b].append((a, 1))
distance = [INF] * (n+1)

def dijkstra(start):
    q = []
    # 비용, node
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in grids[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
start = 1
dijkstra(start)
max_node = 0
max_distance = 0
result = []

for i in range(1, n+1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)

print(max_node, max_distance, len(result))



