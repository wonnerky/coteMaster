import math

def solution(n, k):
    def primenumber(x):
        if x == 1:
            return False
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
    # candid = []
    # can = ''
    # for ele in num:
    #     if ele != '0':
    #         can += ele
    #     else:
    #         if can:
    #             candid.append(can)
    #             can = ''
    # if can:
    #     candid.append(can)
    candid = num.split('0')

    print(candid)
    answer = 0
    for ele in candid:
        if ele:
            if primenumber(int(ele)):
                answer += 1

    return answer


n = 211020101011004
k = 10

print(solution(n, k))