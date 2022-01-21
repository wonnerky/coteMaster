import sys

input = sys.stdin.readline

def solution():
    n = int(input())
    location = list(map(int, input().split()))

    location.sort()
    print(location[(n - 1) // 2])

solution()