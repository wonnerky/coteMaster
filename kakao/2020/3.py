def solution(key, lock):
    def rotation(key):
        return list(zip(*key[::-1]))

    def addMatrix(bg_size, lock, key, row, column, c_start, c_end):
        bg = [[0] * bg_size for _ in range(bg_size)]

        # put key in background
        for i in range(len(key)):
            for j in range(len(key)):
                bg[row+i][column+j] += key[i][j]

        # put lock in background
        for i in range(c_start, c_end):
            for j in range(c_start, c_end):
                bg[i][j] += lock[i-c_start][j-c_start]
                # if not (lock_key) == 1 , return False
                if bg[i][j] != 1:
                    return False
        return True

    _M = len(key)
    _N = len(lock)
    c_start = _M - 1
    c_end = c_start + _N
    bg_size = _N + (2 * c_start)
    for _ in range(4):
        for i in range(0,c_end):
            for j in range(0,c_end):
                if addMatrix(bg_size, lock, key, i, j, c_start, c_end) is True: return True
        key = rotation(key)
    return False


if __name__ == "__main__":
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]

    print(solution(key, lock))