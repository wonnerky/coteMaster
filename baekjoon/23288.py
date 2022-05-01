import sys

def dfs(r, c, b):
    global cnt
    global visit
    for i in range(4):
        nr = r + mov[i][0]
        nc = c + mov[i][1]
        if 0 <= nr < N and 0 <= nc < M and not visit[nr][nc] and board[nr][nc] == b:
            cnt += 1
            visit[nr][nc] = True
            dfs(nr, nc, b)

def dice_direc(idx):
    global dice
    if idx == 0:    # 동
        tmp = dice[0]
        dice[0] = dice[2]
        dice[2] = dice[1]
        dice[1] = dice[3]
        dice[3] = tmp
    elif idx == 1:  # 남
        tmp = dice[0]
        dice[0] = dice[4]
        dice[4] = dice[1]
        dice[1] = dice[5]
        dice[5] = tmp
    elif idx == 2:  # 서
        tmp = dice[0]
        dice[0] = dice[3]
        dice[3] = dice[1]
        dice[1] = dice[2]
        dice[2] = tmp
    else:           # 북
        tmp = dice[0]
        dice[0] = dice[5]
        dice[5] = dice[1]
        dice[1] = dice[4]
        dice[4] = tmp

N, M, K = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

# 동(오) 남(아) 서(왼) 북(위), 시계방향
mov = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# 주사위, 아래 위 동 서 남 북
dice = [6, 1, 3, 4, 5, 2]

idx = 0
r = 0
c = 0
score = 0
for _ in range(K):
    # 주사위 움직이기
    nr = r + mov[idx][0]
    nc = c + mov[idx][1]
    if nr < 0 or nr >= N or nc < 0 or nc >= M:
        idx = (idx + 2) % 4
        nr = r + mov[idx][0]
        nc = c + mov[idx][1]
    r, c = nr, nc
    dice_direc(idx)
    # 주사위 점수
    visit = [[False] * M for _ in range(N)]
    visit[r][c] = True
    b = board[r][c]
    cnt = 1
    dfs(r, c, b)
    score += (cnt * b)
    # 방향 정하기
    # 주사위 결정
    if dice[0] > board[r][c]:
        idx = (idx + 1) % 4
    elif dice[0] < board[r][c]:
        idx = (idx - 1) % 4

print(score)
