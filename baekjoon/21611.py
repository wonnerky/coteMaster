
# n, m = map(int, input().split())
# board = []
# for _ in range(n):
#     board.append(list(map(int, input().split())))
# magics = []
# for _ in range(m):
#     magics.append(list(map(int, input().split())))
######
n, m = 7, 4
board = [[1, 1, 1, 2, 2, 2, 3], [1, 2, 2, 1, 2, 2, 3], [1, 3, 3, 2, 3, 1, 2], [1, 2, 2, 0, 3, 2, 2], [3, 1, 2, 2, 3, 2, 2], [3, 1, 2, 1, 1, 2, 1], [3, 1, 2, 2, 2, 1, 1]]
magics = [[1, 3], [2, 2], [3, 1], [4, 3]]
######
# 상1 하2 좌3 우4
mov = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
pos = []
r, c = (int((n)/2), int((n)/2))
di = [3, 2, 4, 1]
idx = 0
visit = [[0] * n for _ in range(n)]
visit[r][c] = 1
for i in range((n * n) - 1):
    r = r + mov[di[idx]][0]
    c = c + mov[di[idx]][1]
    pos.append((r, c))
    visit[r][c] = 1
    n_idx = (idx + 1) % 4
    if visit[r + mov[di[n_idx]][0]][c + mov[di[n_idx]][1]] == 0:
        idx = n_idx
print(pos)
shark_pos = (int((n)/2), int((n)/2))
result = [0, 0, 0, 0]
for magic in magics:
    # 마법
    d, s = magic
    for i in range(1, s + 1):
        r = shark_pos[0] + (mov[d][0] * i)
        c = shark_pos[1] + (mov[d][1] * i)
        board[r][c] = 0
    # 이동 & 폭발
    while True:
        # 이동
        c_i = 0
        n_i = 1
        while n_i < len(pos):
            c_r, c_c = pos[c_i]
            if board[c_r][c_c] == 0:
                while True:
                    n_r, n_c = pos[n_i]
                    if board[n_r][n_c] == 0:
                        n_i += 1
                        if n_i == len(pos):
                            break
                        continue
                    tmp = board[c_r][c_c]
                    board[c_r][c_c] = board[n_r][n_c]
                    board[n_r][n_c] = tmp
                    break
            c_i += 1
            n_i += 1
        # 폭발
        flag = True
        cnt = 1
        for i in range(len(pos)):
            c_r, c_c = pos[i]
            if i == len(pos) - 1:
                if cnt >= 4:
                    result[board[c_r][c_c]] += cnt
                    for j in range(cnt):
                        r, c = pos[i - j]
                        board[r][c] = 0
                cnt = 1
                continue
            n_r, n_c = pos[i + 1]
            if board[c_r][c_c] == board[n_r][n_c]:
                cnt += 1
            else:
                if cnt >= 4:
                    flag = False
                    result[board[c_r][c_c]] += cnt
                    for j in range(cnt):
                        r, c = pos[i-j]
                        board[r][c] = 0
                cnt = 1
        if flag:
            break

    for ele in board:
        print(ele)
    exit()










        # new_board = [[0] * n for _ in range(n)]


