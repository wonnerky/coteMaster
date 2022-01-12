# + - * /
# 모든 케이스 찾아보기?
from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
opers_ = list(map(int, input().split()))

opers = []
for i, ele in enumerate(opers_):
    opers += [i] * ele
opers = list(permutations(opers, n-1))

min = 2e10
max = 2e-10
for oper in opers:
    result = numbers[0]
    for i in range(n-1):
        if oper[i] == 0:
            result += numbers[i + 1]
        elif oper[i] == 1:
            result -= numbers[i + 1]
        elif oper[i] == 2:
            result *= numbers[i + 1]
        elif oper[i] == 3:
            if result >= 0:
                result //= numbers[i + 1]
            else:
                result = -(-result // numbers[i + 1])
    if result > max:
        max = result
    if result < min:
        min = result

print(max)
print(min)





