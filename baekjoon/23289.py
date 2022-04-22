from collections import deque

R, C, K = map(int, input().split())
warmers = []
invest = []
for r in range(R):
    b = input().split()
    for c in range(C):
        if b[c] == '0':
            continue
        elif b[c] == '5':
            invest.append((r, c))
        else:
            warmers.append([(r, c), int(b[c])])
W = int(input())
wall = []
# 위, 오, 왼, 아
mov = [(-1, 0), (0, 1)]
for _ in range(W):
    r, c, t = map(int, input().split())
    wall.append([(r - 1, c - 1), t])
    nr = r - 1 + mov[t][0]
    nc = c - 1 + mov[t][1]
    if 0 <= nr < R and 0 <= nc < C:
        if t == 0:
            wall.append([(nr, nc), 3])
        else:
            wall.append([(nr, nc), 2])
# 온풍기 위치에 따른 벽 체크
# 0: 오, 1: 왼, 2: 위, 3: 아
# 벽 정보 : [(dr, dc), 벽 위치 (0: 위, 1: 오, 2: 왼, 3: 아)]
# checks = [온풍 타겟 위치, [[벽1], [벽2]]]
checks =[[[(0, 1), [[(0, 0), 1]]], [(-1, 1), [[(0, 0), 0], [(-1, 0), 1]]], [(1, 1), [[(0, 0), 3], [(1, 0), 1]]]],
         [[(0, -1), [[(0, 0), 2]]], [(-1, -1), [[(0, 0), 0], [(-1, 0), 2]]], [(1, -1), [[(0, 0), 3], [(1, 0), 2]]]],
         [[(-1, 0), [[(0, 0), 0]]], [(-1, -1), [[(0, 0), 2], [(0, -1), 0]]], [(-1, 1), [[(0, 0), 1], [(0, 1), 0]]]],
         [[(1, 0), [[(0, 0), 3]]], [(1, 1), [[(0, 0), 1], [(0, 1), 3]]], [(1, -1), [[(0, 0), 2], [(0, -1), 3]]]]]
mov = [(0, 1), (0, -1), (-1, 0), (1, 0)]
d_degree = [[0] * C for _ in range(R)]
for (r, c), direc in warmers:
    board = [[0] * C for _ in range(R)]
    r += mov[direc - 1][0]
    c += mov[direc - 1][1]
    board[r][c] = 5
    q = deque()
    # [(r, c), degree]
    q.append([(r, c), 5])
    d = 1
    while q:
        (r, c), degree = q.popleft()
        if degree == 1:
            continue
        check = checks[direc - 1]
        for t_pos, ele in check:
            flag = True
            for (dr, dc), di in ele:
                if [(r+dr, c+dc), di] in wall:
                    flag = False
            if flag:
                t_r = r + t_pos[0]
                t_c = c + t_pos[1]
                if 0 <= t_r < R and 0 <= t_c < C:
                    if [(t_r, t_c), degree - 1] not in q:
                        board[t_r][t_c] = degree - 1
                        q.append([(t_r, t_c), degree - 1])
    for i in range(R):
        for j in range(C):
            d_degree[i][j] += board[i][j]

board = [[0] * C for _ in range(R)]
choco = 0
while choco < 101:
    # 온풍기에서 바람이 나옴
    for r in range(R):
        for c in range(C):
            board[r][c] += d_degree[r][c]

    # 온도조절
    # 벽 정보 : [(r, c), 벽 위치 (0: 위, 1: 오, 2: 왼, 3: 아)]
    # 위, 오, 왼, 아
    mov = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    c_degree = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            for i in range(4):
                if [(r, c), i] in wall:
                    continue
                nr = r + mov[i][0]
                nc = c + mov[i][1]
                if 0 <= nc < C and 0 <= nr < R and (board[r][c] - board[nr][nc]) >= 4:
                    v = (board[r][c] - board[nr][nc]) // 4
                    c_degree[r][c] -= v
                    c_degree[nr][nc] += v
    for r in range(R):
        for c in range(C):
            board[r][c] += c_degree[r][c]

    # 바깥 온도 감소
    for c in range(C):
        if board[0][c] > 0:
            board[0][c] -= 1
        if board[R-1][c] > 0:
            board[R-1][c] -= 1
    for r in range(R):
        if board[r][0] > 0:
            board[r][0] -= 1
        if board[r][C-1] > 0:
            board[r][C-1] -= 1

    choco += 1  # 초콜릿 먹기

    # 칸 조사하기
    flag = True
    for r, c in invest:
        if board[r][c] < K:
            flag = False
    if flag:
        break


print(choco)


