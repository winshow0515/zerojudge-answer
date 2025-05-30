#AC
#DP l,r 是合併區間l到r的最小成本
# #for 迴圈枚舉mid兩邊加起來的 min(dp l,mid + dp mid,r)
#做了記憶化應該就不會TLE

n = int(input())
a = list(map(int, input().split()))

#區間和
prefix = [0]*(n+1)
for i in range(n):
    prefix[i+1] = prefix[i]+a[i]


memo = {}#(l, r):l到r的最小成本
def dp(l, r):#左壁右開
    if (l, r) in memo:
        return memo[l, r]
    if l+1 == r:
        return 0
    if l+2 == r:
        return abs(a[l] - a[l+1])
    t = float("inf")
    for i in range(l, r-1):
        t = min(t, abs((prefix[r]-prefix[i+1]) - (prefix[i+1] - prefix[l]))+dp(l, i+1)+dp(i+1, r))
    memo[l, r] = t
    return t

print(dp(0, n))