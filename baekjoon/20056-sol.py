import copy
from collections import defaultdict

n, m, k = map(int, input().split())
balls = []
for _ in range(m):
    li = list(map(int, input().split()))
    balls.append([li[0] - 1, li[1] - 1, li[2], li[3], li[4]])
dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for _ in range(k):
    if not balls:
        break

    balls_out = []
    tmp = defaultdict(list)
    for idx in range(len(balls)):
        r, c, m, s, d = balls[idx]
        nr = r + (dir[d][0] * s)
        nc = c + (dir[d][1] * s)
        # 칸 밖으로 나가면
        if nr >= n or nr < 0:
            nr %= n
        if nc >= n or nc < 0:
            nc %= n
        # 파이어볼 정보 업데이트
        balls_out.append([nr, nc, m, s, d])
        tmp[(nr, nc)].append(idx)
    balls = balls_out
    # 2개이상 파이어볼 찾기
    dup_list = []
    for k, v in tmp.items():
        if len(v) >= 2:
            dup_list.append(v)

    if dup_list:
        balls_ = copy.deepcopy(balls)
        # ele는 2개 이상의 balls index
        for ele in dup_list:
            length = len(ele)
            t_m = 0
            t_s = 0
            n_d = [0, 0]
            for idx in ele:
                r, c, m, s, d = balls_[idx]
                t_m += m
                t_s += s
                n_d[d % 2] += 1
                # 무조건 합쳐지니깐 제거
                balls.remove(balls_[idx])
            # 새로운 파이어볼
            n_m = int(t_m / 5)
            n_s = int(t_s / length)
            # 질량 0이면 전부 소멸
            if not n_m == 0:
                if n_d[0] * n_d[1] == 0:
                    for ele in [0, 2, 4, 6]:
                        balls.append([r, c, n_m, n_s, ele])
                else:
                    for ele in [1, 3, 5, 7]:
                        balls.append([r, c, n_m, n_s, ele])

result = 0
for ele in balls:
    r, c, m, s, d = ele
    result += m
print(result)

