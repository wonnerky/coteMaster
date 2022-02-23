import copy

n, m, k = map(int, input().split())
balls = []
for _ in range(m):
    li = list(map(int, input().split()))
    balls.append([li[0] -1, li[1] - 1, li[2], li[3], li[4]])

board = [[[] for _ in range(n)] for _ in range(n)]
for idx in range(len(balls)):
    r, c, m, s, d = balls[idx]
    board[r][c].append(idx)

dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def move(balls, board):
    board_ = copy.deepcopy(board)
    for i in range(n):
        for j in range(n):
            for idx in board_[i][j]:
                r, c, m, s, d = balls[idx]
                nr = r + (dir[d][0] * s)
                nc = c + (dir[d][1] * s)
                # 칸 밖으로 나가면
                if nr >= n or nr < 0:
                    nr %= n
                if nc >= n or nc < 0:
                    nc %= n
                # 파이어볼 옮기기
                balls[idx] = nr, nc, m, s, d
                board[i][j].remove(idx)
                board[nr][nc].append(idx)
    return board

# 2개 이상 체크
def check(balls, board):
    board_ = copy.deepcopy(board)
    balls_ = copy.deepcopy(balls)
    for i in range(n):
        for j in range(n):
            length = len(board_[i][j])
            if  length >= 2:
                t_m = 0
                t_s = 0
                n_d = [0, 0]
                for idx in board_[i][j]:
                    r, c, m, s, d = balls_[idx]
                    t_m += m
                    t_s += s
                    n_d[d % 2] += 1
                # 기존 파이어볼 합쳐짐
                board[i][j] = []
                n_m = int(t_m / 5)
                n_s = int(t_s / length)
                # 질량 0이면 소멸
                if not n_m == 0:
                    if n_d[0] * n_d[1] == 0:
                        for ele in [0, 2, 4, 6]:
                            board[i][j].append(len(balls))
                            balls.append([i, j, n_m, n_s, ele])
                    else:
                        for ele in [1, 3, 5, 7]:
                            board[i][j].append(len(balls))
                            balls.append([i, j, n_m, n_s, ele])
    return balls, board


for _ in range(k):
    board = move(balls, board)
    balls, board = check(balls, board)


result = 0
for i in range(n):
    for j in range(n):
        for idx in board[i][j]:
            r, c, m, s, d = balls[idx]
            result += m
print(result)

