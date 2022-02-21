import copy

def solution(n, info):
    def cal_score(li):
        score = [i for i in reversed(range(1,11))]
        result_li = 0
        result_ap = 0
        for i in range(10):
            if li[i] > info[i]:
                result_li += score[i]
            elif li[i] < info[i]:
                result_ap += score[i]
        return result_li - result_ap
    def dfs(idx, n, lis, c):
        li = copy.deepcopy(lis)
        if n == 0:
            if li not in result:
                result.append(li)
            return
        if idx > 10:
            return
        elif idx == 10:
            li[idx] = n
            if li not in result:
                result.append(li)
            return
        if c:
            dfs(idx+1, n, li, 0)
            dfs(idx+1, n, li, 1)
        else:
            if n > info[idx]:
                n -= (info[idx] + 1)
                li[idx] = (info[idx] + 1)
                dfs(idx+1, n, li, 0)
                dfs(idx+1, n, li, 1)
    def discri(lis):
        for i in reversed(range(11)):
            out = []
            m = 0
            for ele in lis:
                if ele[i] > m:
                    out.append(ele)
                    m = ele[i]
            if out:
                if len(out) == 1:
                    return out[0]
                lis = out
    result = []
    li = [0] * 11
    dfs(0, n, li, 0)
    li = [0] * 11
    dfs(0, n, li, 1)
    print(result)
    max_num = 1
    result_ = []
    for ele in result:
        if cal_score(ele) > max_num:
            result_ = [ele]
            max_num = cal_score(ele)
        elif cal_score(ele) == max_num:
            result_.append(ele)
    if not result_:
        return [-1]
    elif len(result_) == 1:
        return result_[0]
    else:
        return discri(result_)




n = 10
info = [0,0,0,0,0,0,0,0,3,4,3]
print(solution(n, info))