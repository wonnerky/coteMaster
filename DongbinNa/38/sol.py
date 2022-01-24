INF = int(1e9)

n, m = map(int, input().split())
grades = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            grades[i][j] = 0
for _ in range(m):
    i, j = map(int, input().split())
    grades[i][j] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            grades[i][j] = min(grades[i][j], grades[i][k]+grades[k][j])

result = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if grades[i][j] != INF or grades[j][i] != INF:
            count += 1
    if count == n:
        result += 1
print(result)