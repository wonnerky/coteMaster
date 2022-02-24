from itertools import combinations, permutations

def solution(orders, course):
    answer = []
    for dish in course:
        tmp = {}
        for order in orders:
            for ele in combinations(order, dish):
                c = ''
                for i in sorted(ele):
                    c += i

                if c not in tmp.keys():
                    tmp[c] = 1
                else:
                    tmp[c] += 1
        if tmp:
            tmp = sorted(tmp.items(), key=lambda x: x[1], reverse=True)
            max = tmp[0][1]
            if max >= 2:
                for ele in tmp:
                    if ele[1] == max:
                        answer.append(ele[0])
    return sorted(answer)




orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
print(solution(orders, course))