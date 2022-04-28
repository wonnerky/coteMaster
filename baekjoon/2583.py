import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    mov = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    global cnt_
    global board
    board[y][x] = 1
    cnt_ += 1
    for i in range(4):
        nx = x + mov[i][1]
        ny = y + mov[i][0]
        if 0 <= nx < N and 0 <= ny < M:
            if board[ny][nx] == 0:
                dfs(nx, ny)



M, N, K = map(int, input().split())
board = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            board[y][x] = 1
for ele in board:
    print(ele)
print()
cnt = 0
result = []
for x in range(N):
    for y in range(M):
        if board[y][x] == 0:
            cnt_ = 0
            dfs(x, y)
            cnt += 1
            result.append(cnt_)
result.sort()
print(cnt)
for ele in result:
    print(ele, end=' ')