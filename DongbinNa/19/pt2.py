# dfs

n = int(input())
numbers = list(map(int, input().split()))
opers = list(map(int, input().split()))

def dfs(depth, total, op0, op1, op2, op3):
    global max_num, min_num
    if depth == n:
        max_num = max(max_num, total)
        min_num = min(min_num, total)
        return

    if op0:
        dfs(depth+1, total + numbers[depth], op0-1, op1, op2, op3)
    if op1:
        dfs(depth+1, total - numbers[depth], op0, op1-1, op2, op3)
    if op2:
        dfs(depth+1, total * numbers[depth], op0, op1, op2-1, op3)
    if op3:
        dfs(depth+1, int(total / numbers[depth]), op0, op1, op2, op3-1)

min_num = 1e9
max_num = -1e9
dfs(1, numbers[0], opers[0], opers[1], opers[2], opers[3])
print(max_num)
print(min_num)




