# 완전 탐색, 벽을 세울 수 있는 곳에 모두 세워본 뒤 안전 영역 찾기, max 값 저장
# depth first search
import copy

def spread_(cord, board):
    # 상 하 좌 우
    mov = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for k in range(4):
        ni = cord[0] + mov[k][0]
        nj = cord[1] + mov[k][1]
        if 0 <= ni < N and 0 <= nj < M:
            if board[ni][nj] == 0:
                board[ni][nj] = 2
                board = spread_((ni, nj), board)
    return board


def spread(cords):
    global max_safe
    board_ = copy.deepcopy(board)
    # 벽 세우기
    for cord in cords:
        i, j = blank[cord]
        board_[i][j] = 1
    # 전염병 퍼저나가기
    for cord in virus:
        board_ = spread_(cord, board_)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board_[i][j] == 0:
                cnt += 1

    max_safe = max(max_safe, cnt)


N, M = map(int, input().split())
board = []
blank = []
virus = []
for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(M):
        if board[i][j] == 0:
            blank.append((i, j))
        elif board[i][j] == 2:
            virus.append((i, j))

max_safe = 0
for i in range(len(blank) - 2):
    for j in range(i + 1, len(blank) - 1):
        for k in range(j + 1, len(blank)):
            spread([i, j, k])

print(max_safe)

