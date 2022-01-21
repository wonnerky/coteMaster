import sys
input=sys.stdin.readline

def parse_line(line):
    name, kor, eng, math = line.split(' ')
    kor, eng, math = int(kor), int(eng), int(math)
    return -kor, eng, -math, name

N = int(input())
data = [parse_line(input()) for _ in range(N)]
print(data)
print(sorted(data))
print(*map(lambda x:x[3], sorted(data)),sep='\n')