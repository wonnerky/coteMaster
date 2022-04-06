# dfs
from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
opers_ = list(map(int, input().split()))

opers = []
for i, ele in enumerate(opers_):
    opers += [i] * ele
del opers_

def dfs(opers, pre, idx):
    global max_num, min_num
    if not opers:
        max_num = max(max_num, pre)
        min_num = min(min_num, pre)
        return

    for oper in opers:
        opers.remove(oper)
        if oper == 0:
            dfs(opers, pre + numbers[idx], idx + 1)
        elif oper == 1:
            dfs(opers, pre - numbers[idx], idx + 1)
        elif oper == 2:
            dfs(opers, pre * numbers[idx], idx + 1)
        elif oper == 3:
            dfs(opers, int(pre / numbers[idx]), idx + 1)


min_num = 1e9
max_num = -1e9
for ele in permutations(opers, len(opers)):
    dfs(list(ele), numbers[0], 1)
print(max_num)
print(min_num)




