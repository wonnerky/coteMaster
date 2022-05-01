n, m, K = map(int, input().split())
shark = {}
board = [[None] * n for _ in range(n)]
for i in range(n):
    li = list(map(int, input().split()))
    for j in range(n):
        if li[j] != 0:
            shark[li[j]] = [(i, j)]
            board[i][j] = [li[j], K]
        else:
            board[i][j] = [li[j], 0]
shark = dict(sorted(shark.items()))
li = list(map(int, input().split()))
for i in range(m):
    shark[i+1].append(li[i])
direction = {}
for i in range(m):
    direction[i + 1] = []
    for _ in range(4):
        direction[i + 1].append(list(map(int, input().split())))

# 위 아래 왼 오
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 상어의 다음 위치를 찾는 함수
def next_shark(key, value, board):
    # loc = 상어 위치, direc = 방향
    loc, direc = value
    x, y = loc
    my = None
    for di in direction[key][direc-1]:
        nx = x + dx[di-1]
        ny = y + dy[di-1]
        # 격자를 벗어나지 않으면
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 빈칸이면
            if board[nx][ny][0] == 0:
                return (nx, ny), di
            # 빈칸은 아니지만 내 냄새가 나는 칸이면
            elif my == None and board[nx][ny][0] == key:
                my = [(nx, ny), di]
    # 빈칸이 없으면 내 냄새가 나는 칸으로
    return my[0], my[1]


second = 0
while second <= 1000:
    shark = dict(sorted(shark.items()))
    second += 1
    # 상어 다음 위치 찾기
    for k, v in shark.items():
        loc, direc = next_shark(k, v, board)
        shark[k] = [loc, direc]
    # 상어 겹치기 확인
    k = list(shark.keys())
    k.sort()
    pop_list = []
    for i in range(len(k)):
        for j in range(i+1, len(k)):
            # shark 위치가 겹치면, i가 작은 넘버
            if shark[k[i]][0] == shark[k[j]][0]:
                if k[j] not in pop_list:
                    pop_list.append(k[j])
    for ele in pop_list:
        shark.pop(ele)
    # board 냄새 감소
    for i in range(n):
        for j in range(n):
            if board[i][j][1] > 1:
                board[i][j][1] -= 1
            elif board[i][j][1] == 1:
                board[i][j] = [0, 0]
    # 상어 다음 위치 놓기
    for k, v in shark.items():
        x, y = v[0]
        board[x][y] = [k, K]
    if len(shark) == 1:
        break

if second <= 1000:
    print(second)
else:
    print(-1)