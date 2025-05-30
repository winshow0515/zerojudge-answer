n = int(input())
ary = list(map(int,input().split()))
dp = [[None]*100 for _ in range(100)]
#前綴和
prefix = [ary[0]] + [0]*(n-1)
for i in range(1, n): 
    prefix[i] = prefix[i-1]+ary[i]
prefix = [0] + prefix
#3 -1 2 5
#[0, 3, 2, 4, 9]

def rec(l, r):
    if l+1 == r:#只剩一個合併完的數
        return (0, ary[l])
    if r == n:
        merged = prefix[r]-prefix[l]
    else:
        merged = prefix[r+1] -prefix[l]
    if dp[l][r] != None:
        return (dp[l][r], merged)
    
    
    dp[l][r] = float("inf")
    for k in range(l+1, r):
        L = rec(l, k)
        R = rec(k, r)
        dp[l][r] = min(dp[l][r], L[0]+R[0]+abs(L[1]-R[1]))
    return (dp[l][r], merged)

print(rec(0, n)[0])