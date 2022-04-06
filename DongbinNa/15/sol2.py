import sys
import heapq

input = sys.stdin.readline


def solve():
    N, M, K, X = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    heap = []
    answer = []
    # 인접 리스트 생성
    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)

    # 최소 거리 배열 생성
    min_dists = [float('inf')] * (N + 1)

    # 최소 힙 세팅
    min_dists[X] = 0
    heapq.heappush(heap, [min_dists[X], X])

    # 최소 힙 순회
    while heap:
        dist, node = heapq.heappop(heap)
        if min_dists[node] < dist:
            continue
        if min_dists[node] == K:
            answer.append(str(node))
            continue
        for to in graph[node]:
            if min_dists[to] > dist + 1:
                min_dists[to] = dist + 1
                heapq.heappush(heap, [min_dists[to], to])

    return '\n'.join(answer) if answer else -1


print(solve())
