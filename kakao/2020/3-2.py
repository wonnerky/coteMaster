def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 4번 회전
    for _ in range(4):
        # board 전부 탐색하며 더하기
        for r in range(n + m - 1):
            for c in range(n + m - 1):
                board = [[0] * (n + (2 * m) - 2) for _ in range(n + (m * 2) - 2)]
                # board에 key 넣기
                for i in range(m):
                    for j in range(m):
                        board[r+i][c+j] += key[i][j]
                # board에 lock 넣고, 1인지 확인
                flag = True
                for i in range(n):
                    for j in range(n):
                        board[m - 1 + i][m - 1 + j] += lock[i][j]
                        if not board[m - 1 + i][m - 1 + j] == 1:
                            flag = False
                            break
                    if not flag:
                        break
                # 자물쇠 열렸으면 True 리턴
                if flag:
                    return True
        # key 90도 회전
        key_ = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                key_[j][m-1-i] = key[i][j]
        key = key_
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = 	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))