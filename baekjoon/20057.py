
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))


visit = [[False] * n for _ in range(n)]

tornado = {
    'l': [[(-1, 1), 0.01], [(1, 1), 0.01], [(-1, 0), 0.07], [(1, 0), 0.07], [(-2, 0), 0.02], [(2, 0), 0.02], [(-1, -1), 0.1], [(1, -1), 0.1], [(0, -2), 0.05]],
    'r': [[(-1, -1), 0.01], [(1, -1), 0.01], [(-1, 0), 0.07], [(1, 0), 0.07], [(-2, 0), 0.02], [(2, 0), 0.02], [(-1, 1), 0.1], [(1, 1), 0.1], [(0, 2), 0.05]],
    'u': [[(1, -1), 0.01], [(1, 1), 0.01], [(0, 1), 0.07], [(0, -1), 0.07], [(0, -2), 0.02], [(0, 2), 0.02], [(-1, -1), 0.1], [(-1, 1), 0.1], [(-2, 0), 0.05]],
    'd': [[(-1, -1), 0.01], [(-1, 1), 0.01], [(0, 1), 0.07], [(0, -1), 0.07], [(0, -2), 0.02], [(0, 2), 0.02], [(1, -1), 0.1], [(1, 1), 0.1], [(2, 0), 0.05]]
           }
next = {
    'l': (0, -1),
    'r': (0, 1),
    'u': (-1, 0),
    'd': (1, 0)
}
n_direc = {
    'l': 'd',
    'd': 'r',
    'r': 'u',
    'u': 'l'
}
direc = 'l'
x, y = n//2, n//2
visit[x][y] = True
result = 0
while True:
    # (0, 0) 도달 시 종료
    if x == 0 and y == 0:
        break
    # move next loc
    x += next[direc][0]
    y += next[direc][1]
    visit[x][y] = True

    # tornado
    remain = board[x][y]
    for (dx, dy), p in tornado[direc]:
        nx = x + dx
        ny = y + dy
        amount = int(board[x][y] * p)
        remain -= amount
        # 격자 안이면
        if 0 <= nx < n and 0 <= ny < n:
            board[nx][ny] += amount
        # 격자 밖이면
        else:
            result += amount
    nx = x + next[direc][0]
    ny = y + next[direc][1]
    if 0 <= nx < n and 0 <= ny < n:
        board[nx][ny] += remain
    else:
        result += remain

    # 다음 방향 결정
    nx = x + next[n_direc[direc]][0]
    ny = y + next[n_direc[direc]][1]
    if visit[nx][ny] == False:
        direc = n_direc[direc]


print(result)



