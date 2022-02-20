# dfs
import copy

result = []

def solution(board, aloc, bloc):
    global result
    # mode 0: 'a', mode 1: 'b'
    def game(aloc, bloc, board_, is_a, step):
        global result
        # 상 하 좌 우
        mov = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if is_a:
            x, y = aloc
        else:
            x, y = bloc
        board = copy.deepcopy(board_)
        if board[x][y] == 0:
            return

        can_move = False
        for i in range(4):
            nx = x + mov[i][0]
            ny = y + mov[i][1]
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 1:
                board[x][y] = 0
                if is_a:
                    can_move = True
                    step += 1
                    game([nx, ny], bloc, board, not is_a, step)
                else:
                    can_move = True
                    step += 1
                    game(aloc, [nx, ny], board, not is_a, step)
        if not can_move:
            if is_a:
                print('b', board, step)
                result.append(step)
            else:
                print('a', board, step)
                result.append(step)

    game(aloc, bloc, board, True, 0)
    return min(result)

board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
aloc = [1, 0]
bloc = [1, 2]

print(solution(board, aloc, bloc))