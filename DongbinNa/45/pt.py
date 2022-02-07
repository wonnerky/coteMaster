import copy


def solution(n, t, change):
    result = copy.deepcopy(t)

    for ele in change:
        a, b = ele
        idx_a = t.index(a)
        idx_b = t.index(b)
        if idx_a < idx_b:
            return 'IMPOSSIBLE'
        t = result[:idx_b] + result[idx_b+1:idx_a+1] + [result[idx_b]] + result[idx_a+1:]
        print(t)


case = int(input())

for _ in range(case):
    n = int(input())
    t = list(map(int, input().split()))
    m = int(input())
    change = []
    for _ in range(m):
        change.append(list(map(int, input().split())))

    print(t)
    solution(n, t, change)
    # print(solution(n, t, change))