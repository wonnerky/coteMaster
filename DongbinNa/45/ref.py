from sys import stdout

tc = int(input())
count = None
initialize = lambda n: [0 for _ in range(n + 1)]
for _ in range(tc):
    n = int(input())
    temp = list(map(int, input().split()))
    m, count = int(input()), initialize(n)
    for i in range(n):
        count[temp[i]] = i

    temp = count[:]
    for i in range(m):
        c = list(map(int, input().split()))
        a, b = c[0], c[1]
        if temp[a] < temp[b]:
            count[a], count[b] = count[a] + 1, count[b] - 1
        else:
            count[a], count[b] = count[a] - 1, count[b] + 1

    result, valid = [], True
    temp = sorted(map(lambda i: (count[i], i), range(1, n + 1)))
    for i in range(n - 1):
        if temp[i][0] == temp[i + 1][0]:
            valid = False
            break
        result.append(temp[i][1])
    result.append(temp[-1][1])
    stdout.write((" ".join(map(str, result)) if valid else "IMPOSSIBLE") + "\n")