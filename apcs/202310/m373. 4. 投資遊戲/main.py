def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [[0]*n for _ in range(k+1)]
    ans = 0

    #k=0
    t = 0
    for i in range(n):
        t += A[i]
        dp[0][i] = max(0, t)
        if t < 0:
            t = 0
        ans = max(ans, dp[0][i])

    for i in range(1, k+1):
        for j in range(n):
            if j < i:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i][j-1]+A[j], dp[i-1][j-1])
            ans = max(ans, dp[i][j])

    print(ans)
main()