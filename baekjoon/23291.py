import sys

N, K = map(int, sys.stdin.readline().split())
board = list(map(int, sys.stdin.readline().split()))

result = 0
while True:
    result += 1
    idxs = list(filter(lambda x: board[x] == min(board), range(N)))
    # 물고기 넣기
    for idx in idxs:
        board[idx] += 1
    # 어항 쌓기


