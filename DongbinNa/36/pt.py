# Longest Common Substring 구하면 양쪽으로 나눠서 다시 찾는다
# 그렇게 계속 찾다가 LCS가 없으면 남은 문자열의 큰 길이가 수정할 수

def find_lcs(a, b):
    global result
    lcs = [[0] * len(b) for _ in range(len(a))]
    max_v = 0
    idx = (-1, -1)
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                if i > 0 and j > 0:
                    lcs[i][j] = lcs[i - 1][j - 1] + 1
                else:
                    lcs[i][j] += 1
                if lcs[i][j] > max_v:
                    max_v = lcs[i][j]
                    idx = (i, j)

    a_l = a[:idx[0] - max_v + 1]
    a_r = a[idx[0] + 1:]
    b_l = b[:idx[1] - max_v + 1]
    b_r = b[idx[1] + 1:]

    if max_v == 0:
        result += max(len(a_r), len(b_r))
    else:
        find_lcs(a_l, b_l)
        find_lcs(a_r, b_r)

a = input().rstrip()
b = input().rstrip()
result = 0

find_lcs(a, b)

print(result)

