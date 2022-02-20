# 누적합

def solution(board, skill):
    cum_board = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for ele in skill:
        t, r1, c1, r2, c2, d = ele
        if t == 1:
            d = -d
        cum_board[r1][c1] += d
        cum_board[r2+1][c2+1] += d
        cum_board[r1][c2+1] -= d
        cum_board[r2+1][c1] -= d
    for j in range(len(board[0])):
        for i in range(1, len(board)):
            cum_board[i][j] += cum_board[i-1][j]
    for i in range(len(board)):
        for j in range(1, len(board[0])):
            cum_board[i][j] += cum_board[i][j-1]

    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += cum_board[i][j]
            if board[i][j] > 0:
                answer += 1
    print(board)
    return answer


board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill))