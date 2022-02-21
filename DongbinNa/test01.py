n = 10
state = 23
print(bin(state))
print()
for i in range(n):
    print(bin(1 << i))
    # if state & (1 << i):
    #     print(bin(state & (1 << i)))
    if state | (1 << i):
        print(bin(state | (1 << i)))
