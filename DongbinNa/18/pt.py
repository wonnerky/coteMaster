def solution(p):
    def recursion(text):
        if text == '':
            return ''
        cnt = 0
        idx = 0
        for ele in text:
            if ele == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                break
            idx += 1
        u = text[:idx + 1]
        v = text[idx + 1:]

        cnt = 0
        for ele in u:
            if ele == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                result = '(' + recursion(v) + ')'
                for i in range(1, len(u) - 1):
                    if u[i] == '(':
                        result += ')'
                    else:
                        result += '('
                return result
            else:
                return u + recursion(v)

    answer = recursion(p)
    return answer