#TLE
#c++ 才能 AC
import sys
while True:
    try:
        s1_len, s1 = sys.stdin.readline().split()
        s2_len, s2 = sys.stdin.readline().split()
        s1_len = int(s1_len)
        s2_len = int(s2_len)
    except:
        break
    dp = [[0]*(s2_len+1) for _ in range(s1_len+1)]
    for i in range(s1_len+1):
        dp[i][0] = i
    for j in range(s2_len+1):
        dp[0][j] = j

    for i in range(1, s1_len+1):
        for j in range(1, s2_len+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1
    print(dp[s1_len][s2_len])