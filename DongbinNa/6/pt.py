def solution(food_times, k):
    food = [i for i in range(len(food_times))]
    while True:
        if k < len(food_times):
            answer = food[k] + 1
            break
        if not food:
            answer = -1
            break
        min_time = min(min(food_times), k // len(food_times))
        min_idxs = []
        for i in range(len(food_times)):
            food_times[i] -= min_time
            if food_times[i] == 0:
                min_idxs.append(i)
        k -= len(food_times) * min_time
        min_idxs.reverse()
        for idx in min_idxs:
            food.remove(food[idx])
            food_times.remove(0)
    return answer


food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))