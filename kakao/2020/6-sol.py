# 파이썬
def solution(n, weak, dist):

    W, F = len(weak), len(dist)
    repair_lst = [()]  # 현재까지 고칠 수 있는 취약점들 저장 (1,2,3)
    count = 0  # 투입친구 수
    dist.sort(reverse=True) # 움직일 수 있는 거리가 큰 친구 순서대로

    # 고칠 수 있는 것들 리스트 작성
    for can_move in dist:
        repairs = []  # 친구 별 고칠 수 있는 취약점들 저장
        count += 1

        # 수리 가능한 지점 찾기
        for i, wp in enumerate(weak):
            start = wp  # 각 위크포인트부터 시작
            ends = weak[i:] + [n+w for w in weak[:i]]  # 시작점 기준 끝 포인트 값 저장
            can = [end % n for end in ends if end -
                   start <= can_move]  # 가능한 지점 저장
            repairs.append(set(can))

        # 수리 가능한 경우 탐색
        cand = set()
        print('can_move: ', can_move)
        print('repairs: ', repairs)
        for r in repairs:  # 새친구의 수리가능 지점
            print(repair_lst)
            for x in repair_lst:  # 기존 수리가능 지점
                new = r | set(x)  # 새로운 수리가능 지점
                print('new: ', new)
                if len(new) == W:  # 모두 수리가능 한 경우 친구 수 리턴
                    return count
                cand.add(tuple(new))
        print('cand: ', cand)
        repair_lst = cand
    return -1





n = 14
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

print(solution(n, weak, dist))