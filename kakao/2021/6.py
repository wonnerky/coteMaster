from collections import deque
from itertools import permutations
import copy

def solution(board, r, c):
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

    def move(r, c, nums, board_):
        board = copy.deepcopy(board_)
        q = deque()
        i = 0
        l = len(nums)
        t1, t2 = cards[nums[i]]
        q.append([(r, c), t1, t2, board, 0, i])
        q.append([(r, c), t2, t1, board, 0, i])
        step = 1e9

        while q:
            c_pos, t1_pos, t2_pos, board, t_step, i = q.popleft()
            t_step += bfs(c_pos, t1_pos, board) + 1
            t_step += bfs(t1_pos, t2_pos, board) + 1
            board[t1_pos[0]][t1_pos[1]] = 0
            board[t2_pos[0]][t2_pos[1]] = 0
            i += 1
            if i == l:
                step = min(step, t_step)
            else:
                t1, t2 = cards[nums[i]]
                q.append([t2_pos, t1, t2, board, t_step, i])
                q.append([t2_pos, t2, t1, board, t_step, i])
        return step

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
    step = 1e9
    # 상 하 좌 우
    for nums in numss:
        step = min(step, move(r, c, nums, board))
    return step




board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0
print(solution(board, r, c))