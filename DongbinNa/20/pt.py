# S에서 T까지 도달하는 좌표 저장 ( S-T 바로 가는 건 바로 NO)
# 저장된 좌표들 개수 count
# 높은 순으로 정렬하여 3개까지 더하기
# 더한 숫자가 cord_list보다 높으면 Yes, 아니면 No

import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    matrix = []
    students = []
    for i in range(n):
        l = list(input().split())
        matrix.append(l)
        for j in range(n):
            if l[j] == "S":
                students.append((i, j))
    # 왼, 위, 오, 아
    dx = [0, -1, 0, 1]  # 위아래
    dy = [-1, 0, 1, 0]  # 왼오
    cord_cnt = [0 for _ in range(n*n)]
    cord_list = []
    for cord in students:
        x, y = cord
        for i in range(4):
            cord_list_ = []
            nx = x + dx[i]
            ny = y + dy[i]
            while 1:
                if 0 <= nx < n and 0 <= ny < n:
                    if matrix[nx][ny] == 'X':
                        cord_list_.append((nx, ny))
                        nx = nx + dx[i]
                        ny = ny + dy[i]
                    elif matrix[nx][ny] == 'T':
                        if cord_list_:
                            cord_list.append(cord_list_)
                            break
                        else:
                            return print('NO')
                    elif matrix[nx][ny] == 'S':
                        break
                else:
                    break
    for ele in cord_list:
        for x, y in ele:
            cord_cnt[x*n+y] += 1
    if sum(sorted(cord_cnt)[-3:]) >= len(cord_list):
        print('YES')
    else:
        print('NO')


solution()