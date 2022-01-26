# 계속 정렬해서 제일 적은 두 개를 더해 나가야 함


import heapq

n = int(input())
q = []
for _ in range(n):
    heapq.heappush(q, int(input()))

# 1개짜리 입력도 있음
if n == 1:
    print(0)
    exit()

result = 0
while True:

    a = heapq.heappop(q)
    b = heapq.heappop(q)
    result += a+b
    if not q:
        break
    heapq.heappush(q, a+b)
    print(a, b, result, q)

print(result)
