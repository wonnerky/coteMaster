# 처음 숫자를 기준으로 하나씩 비교하면서 다른게 나오면 기준을 바꾸고, 집합 개수를 하나 올린다.
# 0과 1 집합 개수 중 min 값 출력한다.

number = input().count
print(number('01'))
exit()

cnt = [0] * 2
cri = number[0]
for idx in range(1, len(number)):
    if number[idx] != cri:
        cnt[int(cri)] += 1
        cri = number[idx]
cnt[int(cri)] += 1

print(min(cnt))