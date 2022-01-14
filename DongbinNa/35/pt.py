

n = int(input())

ugly_num = [1]
prime = [2, 3, 5]


def check_div(ori, num):
    global ugly_num
    if num == 1:
        ugly_num.append(ori)
    if num % 2 == 0:
        check_div(ori, num // 2)
    elif num % 3 == 0:
        check_div(ori, num // 3)
    elif num % 5 == 0:
        check_div(ori, num // 5)


for num in range(2, int(1e10)):
    check_div(num, num)
    if len(ugly_num) == n:
        print(ugly_num[-1])
        break