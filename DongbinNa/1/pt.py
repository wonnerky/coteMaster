# 공포도가 높은 순서로 정렬하고, 차례대로 지워나가기 전략 -> 하나가 엄청나게 크면 문제가 생김
# 최대값부터 하나씩 만들어서 최대 큰 모임의 숫자를 고른다?

n = input()
x = list(map(int, input().split()))
group = [0 for _ in range(len(x))]

# 내림차순 정렬
x.sort(reverse=True)

for i in range(len(x)):
    idx = i
    cnt = 0
    while True:
        fear = x[idx]
        tail = idx+fear
        # group 인원을 넘으면 break
        if tail > len(x):
            break
        elif tail == len(x):
            cnt += 1
            break
        idx = tail
        cnt += 1

    group[i] = cnt

print(max(group))

