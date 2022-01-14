
n = int(input())

n2, n3, n5 = 2, 3, 5

ugly_list = [1] * n

i2, i3, i5 = 0, 0, 0

for i in range(1, n):
    key = min(n2, n3, n5)
    ugly_list[i] = key
    if key == n2:
        i2 += 1
        n2 = ugly_list[i2] * 2
    if key == n3:
        i3 += 1
        n3 = ugly_list[i3] * 3
    if key == n5:
        i5 += 1
        n5 = ugly_list[i3] * 5

print(ugly_list[n-1])