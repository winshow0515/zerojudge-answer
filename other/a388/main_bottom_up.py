dp = [1, 2, 4, 7] + [None]*1000
for i in range(4, 1000):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

while True:
    n = int(input())
    if n == 0:
        break
    print(2**n - dp[n])