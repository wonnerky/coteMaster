# floid marshall 사용해서 각 도시마다 연결 가능한지 먼저 체크

n, m = map(int, input().split())
board = [[0]*(n+1)]
for _ in range(n):
    board.append([0]+list(map(int, input().split())))
plan = list(map(int, input().split()))

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            board[i][j] = board[i][k] + board[k][j]

result = 'YES'
for i in range(1, m):
    if board[plan[i-1]][plan[i]] == 0:
        result = 'NO'

print(result)