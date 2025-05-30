#東東爬樓梯#DP
#https://zerojudge.tw/ShowProblem?problemid=d212

from sys import stdin

def f(n):
    if n == 0 or n == 1:
        return 1
    if not dp[n]:
        dp[n] = f(n-1) + f(n-2)
    return dp[n]

dp = [None] * 100

for i in stdin:
    print(f(int(i)))