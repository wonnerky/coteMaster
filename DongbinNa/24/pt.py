import sys

input = sys.stdin.readline

def solution():
    n = int(input())
    location = list(map(int, input().split()))

    def cal(cri):
        sum = 0
        for ele in location:
            sum += abs(ele-cri)
        return sum

    loc = 0
    location_set = sorted(list(set(location)))
    idx = location_set.index(location[int(len(location)/2)])
    dist = cal(location_set[idx])
    l_idx = idx-1
    if l_idx >= 0:
        l_dist = cal(location_set[l_idx])
    else:
        l_idx = idx
        l_dist = dist
    r_idx = idx+1
    if r_idx < len(location_set):
        r_dist = cal(location_set[r_idx])
    else:
        r_idx = idx
        r_dist = dist
    if l_dist < r_dist:
        while True:
            l_idx -= 1
            if l_idx >= 0:
                a = cal(location_set[l_idx])
                if a <= l_dist:
                    l_dist = a
                else:
                    return print(location_set[l_idx+1])
            else:
                return print(location_set[l_idx+1])
    else:
        while True:
            r_idx += 1
            if r_idx < len(location_set):
                a = cal(location_set[r_idx])
                if a < r_dist:
                    r_dist = a
                else:
                    return print(location_set[r_idx - 1])
            else:
                return print(location_set[r_idx - 1])

solution()