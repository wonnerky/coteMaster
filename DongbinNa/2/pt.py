# 왼쪽부터 더하기나 곱하기를 해서 큰 수를 선택

numbers = input()

pre_num = int(numbers[0])
for idx in range(1, len(numbers)):
    cur_num = int(numbers[idx])
    sum_op = pre_num+cur_num
    prod_op = pre_num*cur_num
    if sum_op > prod_op:
        pre_num = sum_op
    else:
        pre_num = prod_op

print(pre_num)
