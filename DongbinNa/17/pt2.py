# NxN 시험관, 바이러스 매 초 상하좌우로 증식, 낮은 번호의 바이러스부터 우선순위
# 시간동안(for) 낮은 번호부터 증식 시작. 바이러스가 있거나 matrix 범위 이상이면 stop.
# 바이러스 종류별 좌표 추가

n, k = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
s, x, y = map(int, input().split())

# 상 하 좌 우
dx = [-1, 1, 0, 0]  # 위아래
dy = [0, 0, -1, 1]  # 좌우

# 바이러스 좌표 dict. initial
no_virus = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 0:
            no_virus.append((i, j))

def move(cord):
    x, y = cord
    v_num = k+1
    for i in range(4):
        n_x = x+dx[i]
        n_y = y+dy[i]
        if n_x == n or n_y == n or n_x < 0 or n_y < 0:
            continue
        if matrix[n_x][n_y] != 0:
            if v_num > matrix[n_x][n_y]:
                v_num = matrix[n_x][n_y]
    if v_num != k+1:
        matrix[x][y] = v_num
        no_virus.remove(cord)


for _ in range(s):
    for cord in no_virus:
        move(cord)

# answer. initial cord = (1,1)
print(matrix[x-1][y-1])