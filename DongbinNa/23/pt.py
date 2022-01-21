import sys

input = sys.stdin.readline

def solution():
    def sort_math(names, grades):
        group = {}
        for name in names:
            group[grades[name][2]] = []
        for name in names:
            group[grades[name][2]].append(name)
        group = sorted(group.items(), reverse=True)
        result = []
        for ele in group:
            result += sorted(ele[1])
        return result

    def sort_eng(names, grades):
        group = {}
        for name in names:
            group[grades[name][1]] = []
        for name in names:
            group[grades[name][1]].append(name)
        group = sorted(group.items())
        result = []
        for ele in group:
            result += sort_math(ele[1], grades)
        return result

    def sort_kor(grades):
        group = {}
        for ele in grades.values():
            group[ele[0]] = []
        for k, v in grades.items():
            group[v[0]].append(k)

        group = sorted(group.items(), reverse=True)
        result = []
        for ele in group:
            result += sort_eng(ele[1], grades)
        return result

    n = int(input())
    grades = {}
    for _ in range(n):
        a = list(input().split())
        grades[a[0]] = list(map(int, (a[1:])))
    for ele in sort_kor(grades):
        print(ele)


solution()