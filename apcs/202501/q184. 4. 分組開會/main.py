#AC
n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

prefix = [0]*(n+1)
for i in range(n):
    prefix[i+1] = prefix[i] + l[i]

cost = []

for r in range(k, n+1):
    c = r-(k//2)
    right = prefix[r]-prefix[c]
    if k%2 == 1:
        left = prefix[c-1] - prefix[r-k]
    else:
        left = prefix[c] - prefix[r-k]
    cost.append(right-left)

#A右到左的區間最小值
A = [float('inf')]*(len(cost)-1) +[cost[-1]]
for i in range(len(cost)-2, -1, -1):
    A[i] = min(A[i+1], cost[i])

ans = float('inf')
for i in range(len(cost)-k):
    ans = min(ans, cost[i]+A[i+k])
print(ans)