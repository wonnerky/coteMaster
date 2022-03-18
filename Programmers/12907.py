answer = 0
def solution(n, money):
    def dfs(n, idx):
        global answer
        if n == 0:
            answer += 1
            return
        if idx < 0 or n < 0:
            return
        d = n // money[idx]
        if d == 0:
            dfs(n, idx - 1)
        else:
            for i in reversed(range(d + 1)):
                r = n - (i * money[idx])
                dfs(r, idx - 1)
    div_num = 1000000007
    idx = len(money) - 1
    dfs(n, idx)
    return answer % div_num


def solution2(n, money):
    dp = [1] + [0] * n
    for coin in money:
        for price in range(coin, n + 1):
            if price >= coin:
                dp[price] += dp[price - coin]
    return dp[n] % 1000000007


n = 5
money = [1, 2, 5]
print(solution2(n, money))