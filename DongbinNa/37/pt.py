# Floyd Marshall 알고리즘...

def solution():
    INF = int(1e9)
    n = int(input())
    board = [[INF] * n for _ in range(n)]
    m = int(input())
    for _ in range(m):
        info = list(map(int, input().split()))
        if board[info[0]-1][info[1]-1] != 0:
            if board[info[0] - 1][info[1] - 1] > info[2]:
                board[info[0] - 1][info[1] - 1] = info[2]
        else:
            board[info[0]-1][info[1]-1] = info[2]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    board[i][j] = 0
                if board[i][k] + board[k][j] < board[i][j] and k != i and k != j:
                    board[i][j] = board[i][k] + board[k][j]


    for ele in board:
        for char in ele:
            if char == INF:
                print(0, end=' ')
            else:
                print(char, end=' ')
        print()

solution()