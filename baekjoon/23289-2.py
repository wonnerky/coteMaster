from collections import deque

def wind():
    # 0: right, 1: left, 2: up, 3: down
    # [[(t1_r, t1_c), [check_walls]], [(t2_r, t2_c), [check_walls]]]
    mov = [
        [[(0, 1), [(0, 0, 0)]], [(-1, 1), [(-1, 0, 3), (-1, 0, 0)]], [(1, 1), [(1, 0, 2), (1, 0, 0)]]],
        [[(0, -1), [(0, 0, 1)]], [(-1, -1), [(-1, 0, 3), (-1, 0, 1)]], [(1, -1), [(1, 0, 2), (1, 0, 1)]]],
        [[(-1, 0), [(0, 0, 2)]], [(-1, 1), [(0, 1, 1), (0, 1, 2)]], [(-1, -1), [(0, -1, 0), (0, -1, 2)]]],
        [[(1, 0), [(0, 0, 3)]], [(1, 1), [(0, 1, 1), (0, 1, 3)]], [(1, -1), [(0, -1, 0), (0, -1, 3)]]]
    ]
    board = [[0] * C for _ in range(R)]
    for r, c, d in warmer:
        board_ = [[0] * C for _ in range(R)]
        if d == 0:
            c += 1
        elif d == 1:
            c -= 1
        elif d == 2:
            r -= 1
        else:
            r += 1
        q = deque()
        q.append((r, c, 5))
        while q:
            r, c, degree = q.popleft()
            board_[r][c] = degree
            if degree == 1:
                continue
            for (t_r, t_c), ws in mov[d]:
                if r+t_r < 0 or r+t_r >= R or c+t_c < 0 or c+t_c >= C:
                    continue
                flag = True
                for dr, dc, direc in ws:
                    if (r+dr, c+dc, direc) in walls:
                        flag = False
                if flag:
                    board_[r+t_r][c+t_c] = degree - 1
                    if (r+t_r, c+t_c, degree -1) not in q:
                        q.append((r+t_r, c+t_c, degree -1))
        for r in range(R):
            for c in range(C):
                board[r][c] += board_[r][c]
        # for ele in board_:
        #     print(ele)
        # print()
    return board

def degree_control(board):
    board_ = [[0] * C for _ in range(R)]
    # 오, 왼, 위, 아
    mov = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for r in range(R):
        for c in range(C):
            for i in range(4):
                if (r, c, i) in walls:
                    continue
                dr, dc = mov[i]
                if 0 <= r+dr < R and 0 <= c+dc < C:
                    if board[r][c] > board[r+dr][c+dc]:
                        d = (board[r][c] - board[r+dr][c+dc]) // 4
                        board_[r][c] -= d
                        board_[r+dr][c+dc] += d
    for r in range(R):
        for c in range(C):
            board[r][c] += board_[r][c]
    return board

R, C, K = map(int, input().split())
warmer = []
invest = []
for r in range(R):
    row = list(map(int, input().split()))
    for c in range(C):
        if row[c] == 0:
            continue
        elif row[c] == 5:
            invest.append((r, c))
        else:
            warmer.append((r, c, row[c] - 1))   # (row, col, direction), 0: r, 1: l, 2: u, 3: d
W = int(input())
walls = []
for _ in range(W):
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1
    if t == 0:
        walls.append((x, y, 2))
        walls.append((x-1, y, 3))
    if t == 1:
        walls.append((x, y, 0))
        walls.append((x, y+1, 1))

wind_board = wind()
board = [[0] * C for _ in range(R)]
choco = 0
print('wind')
for ele in wind_board:
    print(ele)
print()

while choco < 101:
    # 온풍기 바람 나옴
    for r in range(R):
        for c in range(C):
            board[r][c] += wind_board[r][c]
    print(choco)
    print('after wind')
    for ele in board:
        print(ele)
    print()

    # 온도 조절
    board = degree_control(board)
    print('after degree control 1')
    for ele in board:
        print(ele)
    print()

    # 바깥쪽 온도 조절
    for c in range(C):
        if board[0][c] >= 1:
            board[0][c] -= 1
        if board[R-1][c] >= 1:
            board[R-1][c] -= 1
    for r in range(1, R - 1):
        if board[r][0] >= 1:
            board[r][0] -= 1
        if board[r][C-1] >= 1:
            board[r][C-1] -= 1
    print('after degree control 2')
    for ele in board:
        print(ele)
    print()

    # 초코 먹기
    choco += 1

    # 온도 조사
    flag = True
    for r, c in invest:
        if board[r][c] < K:
            flag = False
    if flag:
        break


# for ele in board:
#     print(ele)
print(choco)