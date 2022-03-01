def solution(play_time, adv_time, logs):
    def conv_time(str):
        u_h = 3600
        u_m = 60
        t = list(map(int, str.split(':')))
        return t[0]*u_h + t[1]*u_m + t[2]
    logs_start_sec = []
    logs_end_sec = []
    for log in logs:
        start, end = log.split('-')
        logs_start_sec.append(conv_time(start))
        logs_end_sec.append(conv_time(end))
    play_time = conv_time(play_time)
    adv_time = conv_time(adv_time)
    total_time = [0 for _ in range(play_time + 1)]
    start_time = 0
    for i in range(len(logs_start_sec)):
        total_time[logs_start_sec[i]] += 1
        total_time[logs_end_sec[i]] -= 1
    print(total_time)
    for i in range(1, play_time):
        total_time[i] += total_time[i - 1]
    print(total_time)
    for i in range(1, play_time):
        total_time[i] += total_time[i - 1]
    print(total_time)
    max_time = 0
    for i in range(adv_time - 1, play_time + 1):
        m = max(max_time, total_time[i] - total_time[i - adv_time])
        if m > max_time:
            max_time = m
            start_time = i - adv_time + 1
    h = start_time // 3600
    m = (start_time - 3600 * h) // 60
    s = (start_time - 3600 * h - 60 * m)
    answer = f'{h:0>2}:{m:0>2}:{s:0>2}'
    return answer




play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution(play_time, adv_time, logs))