import sys
sys.setrecursionlimit(10000)

def dfs(r, c):
    global visit
    visit[r][c] = True
    mov = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for i in range(4):
        dr, dc = mov[i]
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == False and board[nr][nc] == 1:
            dfs(nr, nc)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    for _ in range(K):
        c, r = map(int, input().split())
        board[r][c] = 1
    visit = [[False] * M for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(M):
            if not visit[r][c] and board[r][c] == 1:
                cnt += 1
                dfs(r, c)
                for ele in visit:
                    print(ele)
                print()

    print(cnt)