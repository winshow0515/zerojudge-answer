#a252. Another LCS
#https://zerojudge.tw/ShowProblem?problemid=a252
s1 = input()
s2 = input()
s3 = input()


s1_len = len(s1)
s2_len = len(s2)
s3_len = len(s3)

dp = []
for i in range(s1_len+1):
    dp.append([[0]*(s3_len+1) for j in range(s2_len+1)])

for i in range(1, s1_len+1):
	for j in range(1, s2_len+1):
		for k in range(1, s3_len+1):
			if s1[i-1] == s2[j-1] and s2[j-1] == s3[k-1]:
				dp[i][j][k] = dp[i-1][j-1][k-1] + 1
			else:
			    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
				
print(dp[s1_len][s2_len][s3_len])


'''TLE
def rec(i, j, k):
    if i == -1 or j == -1 or k == -1:
        return 0
    if dp[i][j][k]:
        return dp[i][j][k]
    
    if s1[i] == s2[j] and s2[j] == s3[k]:
        dp[i][j][k] = rec(i-1, j-1, k-1) + 1
    else:
        dp[i][j][k] = max(rec(i-1, j, k), rec(i, j-1, k), rec(i, j, k-1))
    return dp[i][j][k]
print(rec(len(s1)-1, len(s2)-1, len(s3)-1))'''