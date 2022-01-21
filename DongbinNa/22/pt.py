from collections import deque


def solution(board):
    n = len(board)
    visited = []
    # 오른쪽, 아래쪽, 왼쪽, 위쪽
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # 시계, 반시계
    rotat = []
    # (x1, y1), (x2, y2), horizon or vertical, cnt
    init = ((0, 0), (0, 1), 'h', 0)
    q = deque()
    q.append(init)
    while q:
        (x1, y1), (x2, y2), state, cnt = q.popleft()
        visited.append({(x1, y1), (x2, y2)})
        for dx, dy in move:
            nx1 = x1 + dx; ny1 = y1 + dy
            nx2 = x2 + dx; ny2 = y2 + dy
            if 0 <= nx1 < n and 0 <= nx2 < n and 0 <= ny1 < n and 0 <= ny2 < n:
                if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
                    if {(nx1, ny1), (nx2, ny2)} not in visited:
                        if nx1 == n-1 and ny1 == n-1 or nx2 == n-1 and ny2 == n-1:
                            return cnt+1
                        q.append(((nx1, ny1), (nx2, ny2), state, cnt+1))
        # rotate
        if state == 'h':
            if board[x1+1][y1] == 0 and board[x2+1][y1] == 0 and x1+1 < n and x2+1 <n:
                if {(x1, y1), (x2+1, y1)} not in visited:
                    q.append(((x1, y1), (x2+1, y1), 'v', cnt+1))
                if {(x2, y2), (x1 + 1, y2)} not in visited:
                    q.append(((x2, y2), (x1+1, y2), 'v', cnt+1))
            if board[x1-1][y1] == 0 and board[x2-1][y1] == 0 and x1-1 >= 0 and x2-1 >= 0:
                if {(x2 - 1, y1), (x1, y1)} not in visited:
                    q.append(((x2 - 1, y1), (x1, y1), 'v', cnt+1))
                if {(x1 - 1, y2), (x2, y2)} not in visited:
                    q.append(((x1 - 1, y2), (x2, y2), 'v', cnt+1))
        if state == 'v':
            if board[x1][y1+1] == 0 and board[x2][y2+1] == 0 and y1+1 < n and y2+1 < n:
                if {(x1, y1), (x2 - 1, y2 + 1)} not in visited:
                    q.append(((x1, y1), (x2 - 1, y2 + 1), 'h', cnt+1))
                if {(x2, y2), (x1 + 1, y1 + 1)} not in visited:
                    q.append(((x2, y2), (x1 + 1, y1 + 1), 'h', cnt+1))
            if board[x1][y1-1] == 0 and board[x2][y2-1] == 0 and y1-1 >= 0 and y2-1 >= 0:
                if {(x1, y2 - 1), (x1, y1)} not in visited:
                    q.append(((x1, y2 - 1), (x1, y1), 'h', cnt+1))
                if {(x2, y1 - 1), (x2, y2)} not in visited:
                    q.append(((x2, y1-1), (x2, y2), 'h', cnt+1))



solution()