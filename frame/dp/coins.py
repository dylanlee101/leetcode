'''
凑零钱
'''

# 暴力
def coinChange(coins,amout):
    def dp(n):
        # base case
        if n == 0: return 0
        if n < 0: return -1
        res = float('INF')

        for coin in coins:
            subproblem = dp(n - coin)
            if subproblem == -1:continue
            res = min(res,subproblem)
        return res if res != float('INF') else -1
    return dp(amout)

# 备忘录
def coinChange2(coins,amout):
    memo = dict()

    def dp(n):
        if n in memo: return memo[n]
        if n == 0:return 0
        if n <0 :return -1
        res = float('INF')
        for coin in coins:
            subproblem = dp(n - coin)
            if subproblem == -1 : continue
            res = min(res,1 + subproblem)
        memo[n] = res if res != float('INF') else -1
        return memo
    return dp(amout)
# 迭代解法

def coinChange3(coins,amout):
    dp = dict()

    dp[0] = 0

    for i in range(amout + 1):
        for coin in coins:
            if (i - coin) < 0: continue
            dp[i] = min(dp[i],1+dp[i-coin])

    return -1 if (dp[amout] == amout + 1) else dp[amout]
