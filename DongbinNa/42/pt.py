# cnt_dock 리스트 만들어서, 차례대로 비행기 배치
# 0은 없음 1은 있음
# 게이트 수보다 비행기의 도킹 게이트 넘버가 클 수 있기 때문에, 먼저 조건 체크. l19, idx <= g
# 38:14

g = int(input())
p = int(input())
dock = []
for _ in range(p):
    dock.append(int(input()))

cnt_dock = [0]*(g+1)

result = 0
for ele in dock:
    if sum(cnt_dock[:ele+1]) == ele:
        break
    idx = ele
    while idx > 0:
        if idx <= g and cnt_dock[idx] == 0 :
            cnt_dock[idx] = 1
            break
        else:
            idx -= 1
print(sum(cnt_dock))