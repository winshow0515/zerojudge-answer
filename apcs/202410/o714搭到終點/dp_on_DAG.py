#NA 20% 老師教的
n, m, p = map(int,input().split())
s, t = list(map(int,input().split())), list(map(int,input().split()))

#車班根據終點排序，就會出現單調性，即可更新區間和
buses = sorted(list(zip(t, s)))#[(4, 0), (6, 0), (6, 4), (7, 3), (9, 5)](終站, 起站)
l = s+t
l = sorted(list(set(l)))
d = {x:i for i, x in enumerate(l)} #離散化
dp = [1]+[0]*(len(l)-1)
prefix_sum = []


for end, start in buses:
    end = d[end]
    start = d[start]
    #同餘定理
    dp[end] = (dp[end]%p + sum(dp[start:end])%p) % p

print(dp[d[m]])