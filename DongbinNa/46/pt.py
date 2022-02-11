from collections import deque


def search_fish(li):
    li.sort()
    return li[0]


n = int(input())
board = []
shark_loc = None
shark_size = 2
num_fish = 0
for i in range(n):
    a = list(map(int, input().split()))
    if 9 in a:
        shark_loc = (i, a.index(9))
    board.append(a)

mov = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우
result = 0
cnt = 0
while True:
    q = deque()
    q.append((shark_loc, 0))
    cur_step = 0
    li = []
    valid = [[False] * n for _ in range(n)]
    # bfs
    while q:
        (x, y), step = q.popleft()
        if cur_step != step:
            if li:
                board[shark_loc[0]][shark_loc[1]] = 0
                shark_loc = search_fish(li)
                board[shark_loc[0]][shark_loc[1]] = 9
                result += step
                num_fish += 1
                if shark_size == num_fish:
                    shark_size += 1
                    num_fish = 0
                break
            cur_step = step
        valid[x][y] = True
        for dx, dy in mov:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] > shark_size or valid[nx][ny] == True:
                continue
            if 0 < board[nx][ny] < shark_size and (nx,ny) not in li:
                li.append((nx, ny))
            q.append(((nx, ny), step+1))

    # 먹을 고기가 없다
    if not li:
        print(result)
        break



