# 전투력이 내림차순이 되도록 정렬
# Longest Increase Subsequence 문제

n = int(input())
powers = list(map(int, input().split()))
powers.reverse()
print(powers)
d = [1] * n
for i in range(1, n):
    for j in range(i):
        if powers[j] < powers[i]:
            d[i] = max(d[i], d[j]+1)

print(d)
print(n-max(d))

