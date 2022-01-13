# coin들의 조합을 통해서 만들 수 있는 수를 전부 찾는다
# 1부터 만들 수 있는 조합 안에 있는지 체크하여 아니면 그 값을 출력한다.

from itertools import combinations
n = int(input())
coins = list(map(int, input().split()))

comb = []
for i in range(1, n+1):
    comb_ = combinations(coins, i)
    for ele in comb_:
        comb.append(sum(ele))
comb = list(set(comb))

for num in range(1, int(1e8)):
    if num in comb:
        continue
    print(num)
    break