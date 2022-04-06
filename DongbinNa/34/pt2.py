# 거꾸로 가서 더 작은 거 만나면, 그 뒤에 cnt를 통해서 결정
N = int(input())
powers = list(map(int, input().split()))
powers.reverse()
result = [powers[0]]

for i in range(1, N):
    f = powers[i]
    r = powers[i - 1]
    if f <= r:
        f_cnt = 0
        r_cnt = 0
        for idx in range(i - 1):
            if f <= powers[idx]:
                f_cnt += 1
            if r <= powers[idx]:
                r_cnt += 1
        if f_cnt == r_cnt:
            result = result[:-1] + [f]
    else:
        result.append(f)

print(N - len(result))




