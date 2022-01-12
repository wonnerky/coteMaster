# 뒤에서부터 max 점수를 저장

n = int(input())

t_p = []
for _ in range(n):
    t_p.append(list(map(int, input().split())))


max_score = [0 for _ in range(n+1)]
for idx in reversed(range(n)):
    t, p = t_p[idx]
    if idx + t > n:
        score = max_score[idx+1]
    else:
        score = p + max_score[idx+t]
    if score > max_score[idx+1]:
        max_score[idx] = score
    else:
        max_score[idx] = max_score[idx+1]

print(max_score[0])









