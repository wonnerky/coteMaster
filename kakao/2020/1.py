def solution(s):
    min_str = len(s)
    if len(s) == 1:
        min_str = 1
    for i in range(1, int(len(s)/2) + 1):
        cnt = 1
        st = ''
        tmp = s[:i]
        for j in range(1, int(len(s)/i)):
            if s[j*i:(j+1)*i] == tmp:
                cnt += 1
            else:
                if cnt > 1:
                    st += f'{cnt}{tmp}'
                else:
                    st += tmp
                cnt = 1
                tmp = s[j*i:(j+1)*i]
        if cnt > 1:
            st += f'{cnt}{tmp}'
        else:
            st += tmp
        st += s[(j+1)*i:]
        min_str = min(min_str, len(st))
    return min_str


s = "abcabcdede"
print(solution(s))
