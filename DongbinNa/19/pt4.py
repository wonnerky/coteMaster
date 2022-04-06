n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

def dfs(now, i):
    global max_num, min_num, add, sub, mul, div
    if i == n:
        max_num = max(max_num, now)
        min_num = min(min_num, now)
    else:
        if add > 0:
            add -= 1
            dfs(now + numbers[i], i + 1)
            add += 1
        if sub > 0:
            sub -= 1
            dfs(now - numbers[i], i + 1)
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(now * numbers[i], i + 1)
            mul += 1
        if div > 0:
            div -= 1
            dfs(int(now / numbers[i]), i + 1)
            div += 1
min_num = 1e9
max_num = -1e9
dfs(numbers[0], 1)
print(max_num)
print(min_num)




