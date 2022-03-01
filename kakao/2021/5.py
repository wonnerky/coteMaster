from datetime import datetime
import time
def solution(play_time, adv_time, logs):
    def conv_time(str):
        u_h = 3600
        u_m = 60
        t = list(map(int, str.split(':')))
        return t[0]*u_h + t[1]*u_m + t[2]
    def cal_time(t, times, mode):
        t_time = 0
        k = list(times.keys())
        s_idx = k.index(t)
        cnt = 1
        if mode == 'start':
            start_time = t
            end_time = t + adv_time
            if end_time > play_time:
                return t_time, start_time
            while True:
                if s_idx == len(k) - 1:
                    break
                a = cnt * (k[s_idx + 1] - k[s_idx])
                if adv_time < (t_time + a):
                    t_time += cnt * (adv_time - t_time)
                    break
                t_time += a
                if times[k[s_idx + 1]] == 'start':
                    cnt += 1
                else:
                    cnt -= 1
                s_idx += 1
        else:   # mode == 'end'
            start_time = t - adv_time
            if start_time < 0:
                return t_time, start_time
            while True:
                if s_idx == 0:
                    break
                a = cnt * (k[s_idx] - k[s_idx - 1])
                if adv_time < (t_time + a):
                    t_time += cnt * (adv_time - t_time)
                    break
                t_time += a
                if times[k[s_idx - 1]] == 'end':
                    cnt += 1
                else:
                    cnt -= 1
                s_idx -= 1

        return t_time, start_time
    logs.sort()
    times = {}
    for log in logs:
        start, end = [conv_time(i) for i in log.split('-')]
        times[start] = 'start'
        times[end] ='end'
    times = dict(sorted(times.items(), key=lambda x: x[0]))
    play_time = conv_time(play_time)
    adv_time = conv_time(adv_time)
    # 누적 시간 찾기
    max_time = 0
    start_time = 0
    for k, v in times.items():
        print(k, v)
        t_t, s_t = cal_time(k, times, v)
        if max_time < t_t:
            max_time = t_t
            start_time = s_t
        elif max_time == t_t and s_t < start_time and s_t >= 0:
            start_time = s_t
        print(t_t, s_t)
        print(max_time)
        print()


    h = start_time // 3600
    m = (start_time - 3600 * h) // 60
    s = (start_time - 3600 * h - 60 * m)
    answer = f'{h:0>2}:{m:0>2}:{s:0>2}'
    return answer




play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution(play_time, adv_time, logs))