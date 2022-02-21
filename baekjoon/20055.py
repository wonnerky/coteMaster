n, k = map(int, input().split())
A = list(map(int, input().split()))

step = 0
cnt = 0
# robot 위치
robot = []

while True:
    step += 1
    # 벨트 한 칸 이동
    A = [A[-1]] + A[:-1]
    for i in range(len(robot)):
        robot[i] += 1
    # 로봇 내리는 위치 확인
    if (n - 1) in robot:
        robot.remove(n - 1)

    # 로봇 이동
    for i in range(len(robot)):
        if A[robot[i] + 1] >= 1 and (robot[i] + 1) not in robot:
            A[robot[i] + 1] -= 1
            robot[i] += 1
    # 로봇 내리는 위치 확인
        if (n - 1) in robot:
            robot.remove(n - 1)
    if A[0] != 0:
        robot.append(0)
        A[0] -= 1

    cnt = A.count(0)
    if cnt >= k:
        break

print(step)




