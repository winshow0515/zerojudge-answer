dp = [1, 2, 4, 7] + [None]*1000
def rec(n):
    if dp[n] != None:
        return dp[n]
    dp[n] = rec(n-1) + rec(n-2) + rec(n-3)
    return dp[n]

while True:
    n = int(input())
    if n == 0:
        break
    
    print(2**n - rec(n))