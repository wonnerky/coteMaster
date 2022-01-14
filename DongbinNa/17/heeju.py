# 희주코드

from collections import deque

n, kk = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
target = list(map(int,input().split()))
dx = [0,0,1,-1]
dy = [1,-1,0,0]
virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append([i,j,0,graph[i][j]])
virus = sorted(virus, key = lambda x : x[3])
q = deque(virus)
while q:
    #print('v',virus)
    #print('g',graph)
    # for _ in q:
    i,j,t,v = q.popleft()
    if t == target[0]:
      break
    for k in range(4):
        nx = dx[k] + i
        ny = dy[k] + j
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == 0:
                graph[nx][ny]=v
                q.append([nx,ny,t+1,v])
print(graph[target[1]-1][target[2]-1])