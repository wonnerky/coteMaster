import copy

def shark_mov(loc, path, num_fish, visited):
    global max_fish, results

    if len(path) == 3:
        if num_fish == max_fish:
            results.append(path)
        elif num_fish > max_fish:
            max_fish = num_fish
            results = [path]
        return None

    r, c = loc
    visited[r][c] = True
    for i in range(1, 5):
        nr, nc = r + s_mov[i][0], c + s_mov[i][1]
        if 0 <= nr < 4 and 0 <= nc < 4 and not visited[nr][nc]:
            n_path = path + str(i)
            tmp_fish = num_fish + len(board[nr][nc])
            shark_mov((nr, nc), n_path, tmp_fish, visited)

M, S = map(int, input().split())
board = [[[] for _ in range(4)] for _ in range(4)]
for _ in range(M):
    r, c, d = map(int, input().split())
    board[r - 1][c - 1].append(d - 1)
smell = [[0] * 4 for _ in range(4)]
r, c = map(int, input().split())
shark = (r - 1, c - 1)
smell[r - 1][c - 1] = 1

# 0 ~ 7, 좌 좌상 상 상우 우 우하 하 좌하, 시계 방향
mov =[(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
# 상 1 좌 2 하 3 우 4
s_mov = [(0, 0), (-1, 0), (0, -1), (1, 0), (0, 1)]
for _ in range(S):
    # 복제
    board_ = copy.deepcopy(board)
    # 물고기 이동
    for r in range(4):
        for c in range(4):
            for d in board_[r][c]:
                for i in range(8):
                    dr, dc = mov[(d - i) % 8]
                    if 0 <= r + dr < 4 and 0 <= c + dc < 4 and smell[r + dr][c + dc] == 0:
                        board[r][c].remove(d)
                        board[r+dr][c+dc].append((d - i) % 8)
                        break
    print('smell')
    for ele in smell:
        print(ele)
    print()
    print('move')
    for ele in board:
        print(ele)
    print()
    # 상어 이동
    max_fish = 0
    results = []
    visited = [[False] * 4 for _ in range(4)]
    shark_mov(shark, '', 0, visited)     # 초기 상어 위치의 물고기는 사라지지 않는다
    results.sort()
    paths = results[0]
    for path in paths:
        r, c = shark[0] + s_mov[int(path)][0], shark[1] + s_mov[int(path)][1]
        shark = (r, c)
        if board[r][c]:
            smell[r][c] = 3
            board[r][c] = []
    print('shark move')
    for ele in board:
        print(ele)
    print()
    # 냄새 정리
    for r in range(4):
        for c in range(4):
            if smell[r][c] > 0:
                smell[r][c] -= 1
    if smell[shark[0]][shark[1]] == 0:
        smell[shark[0]][shark[1]] = 1

    # 복제
    for r in range(4):
        for c in range(4):
            board[r][c] += board_[r][c]
    print('copy')
    for ele in board:
        print(ele)
    print()

    print('smell')
    for ele in smell:
        print(ele)
    print()

out = 0
for r in range(4):
    for c in range(4):
        out += len(board[r][c])
print(out)