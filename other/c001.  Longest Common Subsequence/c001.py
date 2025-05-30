#c001. 10405 - Longest Common Subsequence
#https://zerojudge.tw/ShowProblem?problemid=c001

'''TLE啦
def f(i, j):
    if i < 0 or j < 0:
        return 0
    if dp[i][j]:
        return dp[i][j]
    if s1[i] == s2[j]:
        dp[i][j] = f(i-1, j-1) + 1
    else:
        dp[i][j] = max(f(i-1, j), f(i, j-1))
    return dp[i][j]

while True:
    try:
        s1 = input()
        s2 = input()
        dp = [[None]*len(s2) for _ in range(len(s1))]

        print(f(len(s1)-1, len(s2)-1))
    except:
        break
'''
#別人的解答 是bottom up 作者joccc014@gmail.com
while True:
	try:
		s1 = input()
		s2 = input()
		# 初始化 dp
		s1_len, s2_len = len(s1), len(s2)
	
		# 讓dp長寬多一格 先預設0
		dp=[[0]*(s2_len+1) for _ in range(s1_len+1)]
	
		# LCS
		for i in range(1, s1_len+1):
			for j in range(1, s2_len+1):
				if s1[i-1] == s2[j-1]: # 從 index = 0 的位置開始比對字串
					dp[i][j] = dp[i-1][j-1] + 1 # 從 dP[1][1]的位置開始計算
				else:
					dp[i][j] = max(dp[i-1][j], dp[i][j-1])
	
		print(dp[s1_len][s2_len])
	except:
		break
'''
#別人的解答2 用了Rolling 比上面又更快 作者BensonDC 
while True:
    try:
        s1 = input()
        s2 = input()
    except:
        break
    n1 = len(s1)
    n2 = len(s2)
    dp = [0]*(n2+1)
    for i in range(1, n1+1):
        dp_prev = dp[:]
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                dp[j] = dp_prev[j-1] + 1
            else:
                dp[j] = max(dp[j-1], dp[j])
    print(dp[n2])
'''