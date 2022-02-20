# 누적합

def solution(board, skill):
    for ele in skill:
        t, r1, c1, r2, c2, d = ele
        if t == 1:
            d = -d
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                board[r][c] += d
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1
    return answer


board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill))