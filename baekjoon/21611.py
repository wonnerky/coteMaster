
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
            if board[c_r][c_c] == 0:
                break
            # 앞의 루프에서 현재와 이전 칸의 구슬 번호가 같은 경우
            # 마지막 연속된 것 폭발은 flag 필요없이 이동이 완료된 상태가 됨
            if i == len(pos) - 1:
                if cnt >= 4:
                    result[board[c_r][c_c]] += cnt
                    for j in range(cnt):
                        r, c = pos[i - j]
                        board[r][c] = 0
                cnt = 1
                break
            n_r, n_c = pos[i + 1]
            if board[c_r][c_c] == board[n_r][n_c]:
                cnt += 1
            else:
                if cnt >= 4:
                    flag = False
                    result[board[c_r][c_c]] += cnt
                    for j in range(cnt):
                        r, c = pos[i - j]
                        board[r][c] = 0
                cnt = 1
        if flag:
            break
    # 변화
    g = []
    ball = board[pos[0][0]][pos[0][1]]
    cnt = 1
    # board가 전부 0인 경우 check
    if ball != 0:
        for c_i in range(len(pos)):
            n_i = c_i + 1
            c_r, c_c = pos[c_i]
            if n_i == len(pos):
                g.append((cnt, board[c_r][c_c]))
                break
            n_r, n_c = pos[n_i]
            if board[n_r][n_c] == 0:
                g.append((cnt, board[c_r][c_c]))
                break
            if board[c_r][c_c] == board[n_r][n_c]:
                cnt += 1
            else:
                g.append((cnt, board[c_r][c_c]))
                cnt = 1
        new_board = [[0] * n for _ in range(n)]
        new_idx = 0
        for ele in g:
            if new_idx >= len(pos):
                break
            cnt, ball = ele
            new_board[pos[new_idx][0]][pos[new_idx][1]] = cnt
            new_board[pos[new_idx + 1][0]][pos[new_idx + 1][1]] = ball
            new_idx += 2
        board = new_board

print(result[1]*1 + result[2]*2 + result[3]*3)




















