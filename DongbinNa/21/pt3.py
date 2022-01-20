# queue 사용
# 최대 2500번 재귀 사용.. maximum 1000
# dfs 함수 사용 안하는 방법으로 진행...?
# queue로 search list 만들어서 search i,j 전부 돌 필요가 없다.
# 인구가 바뀌는 도시는 다시 search list에 넣어서 확인한다.
# search list는 어차피 상하좌우 보기 때문에 한 칸씩 띄어서 확인해도 된다.

import sys
from collections import deque


def solution():
    input = sys.stdin.readline
    n, l, r = map(int, input().split())

    A = []
    for i in range(n):
        A.append(list(map(int, input().split())))

    # 좌 위 우 아래
    dx = [0, -1, 0, 1]  # 위 아래
    dy = [-1, 0, 1, 0]  # 좌 우

    search_list = deque([(i, j) for i in range(n) for j in range(i%2, n, 2)])
    visited = [[-1] * n for _ in range(n)]
    days = 0

    while search_list:
        flag = True
        for _ in range(len(search_list)):
            i, j = search_list.popleft()
            if visited[i][j] != days:
                q = deque()
                q.append((i, j))
                union = []
                visited[i][j] = days
                union.append((i, j))
                total_pop = A[i][j]
                while q:
                    x, y = q.popleft()
                    for idx in range(4):
                        nx = x + dx[idx]
                        ny = y + dy[idx]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != days:
                            if l <= abs(A[x][y] - A[nx][ny]) <= r:
                                total_pop += A[nx][ny]
                                union.append((nx, ny))
                                q.append((nx, ny))
                                visited[nx][ny] = days
                                flag = False
                if len(union) > 1:
                    new_pop = total_pop // len(union)
                    for x, y in union:
                        A[x][y] = new_pop
                        search_list.append((x,y))
        if flag:
            return print(days)

        days += 1


solution()
