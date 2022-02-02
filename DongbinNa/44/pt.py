# 크루스칼 알고리즘 사용
# 메모리 초과

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def cal_cost(a, b):
    return min(min(abs(a[0]-b[0]), abs(a[1]-b[1])), abs(a[2]-b[2]))


n = int(input())
planet = []
for _ in range(n):
    planet.append(list(map(int, input().split())))

edges = []
for i in range(n):
    for j in range(i, n):
        if i == j:
            continue
        edges.append((cal_cost(planet[i], planet[j]), i, j))
edges.sort()
parent = [0] * n
for i in range(n):
    parent[i] = i
result = 0
for ele in edges:
    cost, a, b = ele
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)