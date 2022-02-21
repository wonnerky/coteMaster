import math
def solution(fees, records):
    def convMin(str):
        hh, mm= map(int, str.split(':'))
        return mm + 60 * hh
    def cal_fee(fees, time):
        if time <= fees[0]:
            return fees[1]
        time = time - fees[0]
        n = math.ceil(time / fees[2])
        return fees[1] + (n * fees[3])
    data = {}
    for ele in records:
        time, car, state = ele.split()
        if car not in data.keys():
            data[car] = []
        data[car].append(time)
    car_fee = {}
    for k, v in data.items():
        car_fee[k] = 0
        if len(v) % 2 != 0:
            data[k].append('23:59')
    print(data)
    for k, v in data.items():
        time = 0
        for i in range(0, len(v), 2):
            time += convMin(v[i+1]) - convMin(v[i])
        car_fee[k] += cal_fee(fees, time)
    car_fee = sorted(car_fee.items())
    answer = []
    for ele in car_fee:
        answer.append(ele[1])
    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))