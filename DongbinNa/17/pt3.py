# BFS를 사용
# virus 정보 : 시간, 위치, 바이러스종류
# virus 정보를 Queue에 넣어서 낮은 바이러스부터 꺼내서 주변 체크 후 바이러스 업데이트
# 뒤에 쌓이는거는 시간이 +1 되는데, 예를 들어 +4가 나오기 시작하면 그 뒤는 모두 +4임 (4초가 흘렀다는 거임)
# python3에서 시간초과...!! pypy3에서 돌아감!!

from collections import deque

n, k = map(int, input().split())
matrix = []
# (virus, time, x, y)
virus = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
    for j in range(n):
        if matrix[i][j] != 0:
            virus.append((matrix[i][j], 0, i, j))
target_s, target_x, target_y = map(int, input().split())

virus.sort()
q = deque(virus)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    v_num, s, x, y = q.popleft()
    if s == target_s:
        break
    if matrix[target_x-1][target_y-1] != 0:
        break
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if n > nx >= 0 and n > ny >= 0:
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = v_num
                q.append((v_num, s+1, nx, ny))

print(matrix[target_x-1][target_y-1])




