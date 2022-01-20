from collections import deque

n = 10

cand = deque([(i,j) for i in range(n) for j in range(i%2,n,2)])

print(len(cand))
print(cand)

print(3%2)