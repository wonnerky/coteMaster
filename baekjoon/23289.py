

R, C, K = map(int, input().split())
warmer = []
invest = []
for r in range(R):
    b = list(map(int, input().split()))
    for c in range(C):
        if b[c] == 5:
            invest.append((r, c))
        elif b[c] == 0:
            continue
        else:
            warmer.append([(r, c), b[c]])
W = int(input())
wall = []
# 위, 오
mov = [(-1, 0), (0, 1)]
for _ in range(W):
    r, c, t = map(int, input().split())
    r -= 1
    c -= 1
    wall.append([(r, c), t])
    nr = r + mov[t][0]
    nc = c + mov[t][1]
    if 0 <= nr < R and 0 <= nc < C:
        if t == 0:
            wall.append([(nr, nc), 3])
        else:
            wall.append([(nr, nc), 2])

# 온풍기 위치에 따른 벽 체크
# 1: 오, 2: 왼, 3: 위, 4: 아
# (dr, dc), 벽 위치 (0: 위, 1: 오, 2: 좌, 3: 아)
checks =[[[[[(0, 0), 1]], ()],[[(0, 0), 0], [(-1, 0), 1]], [[(0, 0), 3], [(1, 0), 1]]],
         [[[(0, 0), 2]], [[(0, 0), 0], [(-1, 0), 2]], [[(0, 0), 3], [(1, 0), 2]]],
         [[[(0, 0), 0]], [[(0, 0), 2], [(0, -1), 0]], [[(0, 0), 1], [(0, 1), 0]]],
         [[[(0, 0), 3]], [[(0, 0), 1], [(0, 1), 3]], [[(0, 0), 2], [(0, -1), 3]]]]
mov = [(0, 1), (0, -1), (-1, 0), (1, 0)]
dbs = []
for (r, c), direc in warmer:
    board = [[0] * C for _ in range(R)]
    r += mov[direc - 1][0]
    c += mov[direc - 1][1]
    board[r][c] = 5
    d = 1
    while True:
        flag = False
        nr = r + mov[direc - 1][0]
        nc = c + mov[direc - 1][1]
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            break
        check = checks[direc - 1]
        for ele in check:
            flag = True
            for ele_ in ele:
                if ele_ in wall:
                    flag = False
            if flag:






board = [[0] * C for _ in range(R)]
choco = 0
while choco < 101:
    pass
