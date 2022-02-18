import math

def solution(n, k):
    def primenumber(x):
        for i in range(2, int(math.sqrt(x) + 1)):
            if x % i == 0:
                return False
        return True
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    num = rev_base[::-1]
    print(num)
    candid = []
    s = -1
    for idx in range(len(num)):
        if s == -1:
            if num[idx] != '0':
                s = idx
        else:
            if num[idx] == '0':
                if num[s:idx] != '1':
                    candid.append(num[s:idx])
                s = -1
    if s != -1:
        if num[s:] != '1':
            candid.append(num[s:])
    print(candid)
    answer = 0
    for ele in candid:
        if primenumber(int(ele)):
            answer += 1
    if answer == 0:
        return -1
    else:
        return answer




n = 1
k = 10

print(solution(n, k))