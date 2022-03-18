def solution(p):
    def right_str(p):
        cnt = 0
        for ele in p:
            if ele == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                return False
        return True

    def div_uv(p):
        cnt = 0
        idx = 1
        for ele in p:
            if ele == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                u = p[:idx]
                v = p[idx:]
                break
            idx += 1
        return u, v

    def recursion(p):
        if not p:
            return ''
        u, v = div_uv(p)
        if right_str(u):
            return u + recursion(v)
        else:
            return '(' + recursion(v) + ')' + u[1:-1].replace('(', 'a').replace(')', '(').replace('a', ')')
    return recursion(p)

p = ")(()"
print(solution(p))