def solution(food_times, k):
    answer = 0
    valid = False
    foods = [i for i in range(len(food_times))]
    while True:
        idxs = []
        for i in range(len(food_times)):
            if k < 0:
                valid = True
                break
            food_times[i] -= 1
            k -= 1
            if food_times[i] == 0:
                idxs.append(i)
            answer = foods[i] + 1
        print(food_times)
        print(idxs)
        idxs.reverse()
        for idx in idxs:
            foods.remove(foods[idx])
            food_times.remove(0)
        if not foods:
            break
        if valid:
            break
    return answer


food_times = [3, 1, 2]
k = 5

print(solution(food_times, k))