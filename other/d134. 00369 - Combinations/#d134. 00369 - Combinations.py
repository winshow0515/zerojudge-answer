#d134. 00369 - Combinations DP
#https://zerojudge.tw/ShowProblem?problemid=d134
dp = {}
def f(n, m):
    if m == 0 or m == n:
        return 1
    if (n, m) in dp:
        return dp[(n, m)]
    dp[(n, m)] = f(n-1, m-1) + f(n-1, m)
    return dp[(n, m)]

while True:
    N, M = list(map(int, input().split()))
    if N == 0 and M == 0:
        break
    C = f(N, M)
    print(f"{N} things taken {M} at a time is {C} exactly.")