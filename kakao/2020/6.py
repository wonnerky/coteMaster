import copy
from itertools import permutations

def solution(n, weak, dist):
    if n == 1:
        return 1
    max_ = weak[0] - weak[-1] + n
    cut_idx = 0
    for i in range(1, len(weak)):
        print(weak[i] - weak[i - 1])
        if weak[i] - weak[i - 1] > max_:
            max_ = weak[i] - weak[i - 1]
            cut_idx = i
    # weak 정보 cutting
    weak = weak[cut_idx:] + weak[:cut_idx]
    dist.sort(reverse=True)
    print(weak)
    for i in range(1, len(dist) + 1):
        weak_ = copy.deepcopy(weak)
        comb = list(permutations(dist[:i], len(dist[:i])))
        for c in comb:
            print(c)
            for ele in c:
                for j in reversed(range(1, len(weak_))):    # 큰 수부터 뒤로 돌아오기
                    d = weak_[j] - weak_[0]
                    if d < 0:
                        d += n
                    if ele >= d:
                        weak_ = weak_[j+1:]
                        break
                if not weak_:
                    return len(dist[:i])
    return -1



n = 1
weak = [0]
dist = [2]
print(solution(n, weak, dist))