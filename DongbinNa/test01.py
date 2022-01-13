from itertools import permutations

n = 2
opers_ = [0, 1, 0, 0]
opers = []
for i, ele in enumerate(opers_):
    opers += [i] * ele
opers = list(permutations(opers, 1))

print(opers)
for ele in opers:
    cnt = 0
    for  i, j in enumerate(ele):
        print(i)
        print(j)