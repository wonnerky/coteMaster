import copy
def solution(n, build_frame):
    def install(x, y, a, board):
        if a:   # 보
            if x == 0 or y == l - 1:    # 바닥이거나 board의 젤 오른쪽이면
                return False
            if board[x - 1][y][0] or board[x - 1][y + 1][0]:  # 왼쪽과 오른쪽에 기둥이 있으면
                return True
            if y - 1 >= 0 and board[x][y - 1][1] and board[x][y + 1][1]: # 양 쪽에 보가 있으면
                return True
            return False
        else:   # 기둥
            if x == l - 1:  # board를 넘어가면
                return False
            if x == 0:  # 바닥일 때
                return True
            if board[x - 1][y][0]:    # 밑에 기둥 있을 때
                return True
            if y - 1 >= 0 and board[x][y-1][1]:   # 왼쪽에 보가 있을 때
                return True
            if board[x][y][1]:  # 그 자리에 보가 있을 때
                return True
            return False
    def delete(x, y, a, board_):
        board = copy.deepcopy(board_)
        board[x][y][a] = 0  # 삭제
        if a:   # 보
            if board[x][y][0]:  # 왼쪽에 기둥이 있는 경우
                if not install(x, y, 0, board):
                    return False
            if board[x][y+1][0]:   # 오른쪽에 기둥이 있는 경우
                if not install(x, y+1, 0, board):
                    return False
            if y - 1 >= 0 and board[x][y - 1][1]:   # 왼쪽에 보가 있는 경우
                if not install(x, y-1, 1, board):
                    return False
            if y + 1 < l and board[x][y + 1][1]:    # 오른쪽에 보가 있는 경우
                if not install(x, y+1, 1, board):
                    return False
            return True
        else:   # 기둥
            if x + 1 < l and board[x+1][y][0]:  # 위에 기둥이 있는 경우
                if not install(x+1, y, 0, board):
                    return False
            if x + 1 < l and y - 1 >= 0 and board[x+1][y - 1][1]:   # 왼쪽위에 보가 있는 경우
                if not install(x+1, y-1, 1, board):
                    return False
            if x + 1 < l and board[x+1][y][1]:  # 위에 보가 있는 경우
                if not install(x+1, y, 1, board):
                    return False
            return True
    board = [[[0, 0] for _ in range(n + 1)]  for _ in range(n + 1)]
    l = len(board)
    for order in build_frame:
        x, y, a, b = order
        if b:   # 설치
            if install(y, x, a, board):
                board[y][x][a] = 1
                print('install success')
            else:
                print('install fail')
        else:   # 삭제
            if delete(y, x, a, board):
                board[y][x][a] = 0
                print('delete success')
            else:
                print('delete fail')
    answer = []
    for y in range(l):
        for x in range(l):
            if board[y][x][0]:
                answer.append([x, y, 0])
            if board[y][x][1]:
                answer.append([x, y, 1])
    return sorted(answer)


n = 5
build_frame = 	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame))