import copy
import sys
sys.setrecursionlimit(10 ** 5)

n, q = map(int, input().split())
board = []
for _ in range(2 ** n):
    board.append(list(map(int, input().split())))
L = list(map(int, input().split()))
mov = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def new_board(board, l):
    board_ = copy.deepcopy(board)
    # if l != 1:
    for i in range(0, len(board), l):
        for j in range(0, len(board), l):
            c = [k for k in range(i, i + l)]
            r = [k for k in range(j, j + l)]
            for a in range(len(c)):
                for b in range(len(c)):
                    board[c[b]][r[-a-1]] = board_[c[a]][r[b]]
    return board

def modify_ice(board):
    board_ = copy.deepcopy(board)
    length = len(board)
    t_ice = 0
    # 얼음 체크 후 유지 혹은 감소 결정
    for x in range(length):
        for y in range(length):
            cnt = 0
            for dx, dy in mov:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < length and 0 <= ny < length:
                    if board_[nx][ny] > 0:
                        cnt += 1
            if cnt < 3 and board[x][y] > 0:
                board[x][y] -= 1
            t_ice += board[x][y]
    return t_ice, board

def dfs(x, y, board):
    global mass
    global cnt
    global visit
    visit[x][y] = True
    if board[x][y] < 1:
        return None
    cnt += 1
    if mass < cnt:
        mass = cnt
    for dx, dy in mov:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < length and 0 <= ny < length:
            if visit[nx][ny]:
                continue
            dfs(nx, ny, board)

for l in L:
    # 격자 나누기
    l = 2 ** l
    board = new_board(board, l)
    # 얼음 체크
    t_ice, board = modify_ice(board)

mass = 0
length = len(board)
visit = [[False] * length for _ in range(length)]
for x in range(length):
    for y in range(length):
        if visit[x][y]:
            continue
        cnt = 0
        dfs(x, y, board)

print(t_ice)
print(mass)
