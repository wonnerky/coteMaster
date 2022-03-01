from collections import deque
from itertools import permutations
import copy
s = 0
def solution(board, r, c):
    global s
    def bfs(c_pos, t_pos, board_):
        board = copy.deepcopy(board_)
        mov = ((-1, 0), (1, 0), (0, -1), (0, 1))
        q = deque()
        step = 0
        r, c = c_pos
        visit = [(r, c)]
        q.append([(r, c), step, visit])
        while q:
            (r, c), step, visit = q.popleft()
            if (r, c) == t_pos:
                break
            for ele in mov:
                # 한 칸 움직이기
                n_r = r + ele[0]
                n_c = c + ele[1]
                if 0 <= n_r < n and 0 <= n_c < n and (n_r, n_c) not in visit:
                    visit.append((n_r, n_c))
                    q.append([(n_r, n_c), step + 1, visit])
                # ctrl 움직이기
                i = 1
                while True:
                    n_r = r + (i * ele[0])
                    n_c = c + (i * ele[1])
                    if 0 <= n_r < n and 0 <= n_c < n:
                        if board[n_r][n_c] == 0:
                            i += 1
                        else:
                            if (n_r, n_c) not in visit:
                                visit.append((n_r, n_c))
                                q.append([(n_r, n_c), step + 1, visit])
                            break
                    else:
                        n_r = r + ((i - 1) * ele[0])
                        n_c = c + ((i - 1) * ele[1])
                        if (n_r, n_c) not in visit:
                            visit.append((n_r, n_c))
                            q.append([(n_r, n_c), step + 1, visit])
                        break
        return step
    def dfs(nums, c_pos, idx, step, board):
        global s
        if step >= min_step:
            return
        if step >= s:
            return
        if idx == len(nums):
            s = min(s, step)
            return
        b1 = copy.deepcopy(board)
        b2 = copy.deepcopy(board)
        t1, t2 = cards[nums[idx]]
        idx += 1
        m1 = bfs(c_pos, t1, b1) + 1
        m1 += bfs(t1, t2, b1) + 1
        b1[t1[0]][t1[1]] = 0
        b1[t2[0]][t2[1]] = 0
        dfs(nums, t2, idx, step + m1, b1)
        m2 = bfs(c_pos, t2, b2) + 1
        m2 += bfs(t2, t1, b2) + 1
        b2[t1[0]][t1[1]] = 0
        b2[t2[0]][t2[1]] = 0
        dfs(nums, t1, idx, step + m2, b2)
    n = len(board)
    cards = [[], [], [], [], [], [], []]
    numss = []
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                cards[board[i][j]].append((i, j))
                numss.append(board[i][j])
    numss = set(numss)
    numss = list(permutations(numss, len(numss)))
    min_step = 1e9
    for nums in numss:
        s = 1e9
        dfs(nums, (r, c), 0, 0, board)
        min_step = min(min_step, s)
    return min_step


board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0
print(solution(board, r, c))