def solution(n, s, a, b, fares):
    dist = [[1e9] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dist[i][i] = 0
    for ele in fares:
        i, j, f = ele
        dist[i][j] = f
        dist[j][i] = f
    # 경로 업데이트
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # 경유 없는 경우
    answer = dist[s][a] + dist[s][b]
    # 경유 있는 경우
    for i in range(1, n + 1):
        tmp = dist[s][i] + dist[i][a] + dist[i][b]
        if tmp < answer:
            answer = tmp
    return answer



n = 7
s = 3
a = 4
b = 1
fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
print(solution(n, s, a, b, fares))