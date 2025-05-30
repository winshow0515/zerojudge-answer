import sys
from collections import defaultdict
n, k = map(int, input().split())
A = list(map(int, sys.stdin.readline().split()))
last = defaultdict(lambda: -1)
ans, DP0 = 0, 0
DP = [[0]*(k+1) for _ in range(n)]

for cur_n, x in enumerate(A):
    DP0 = min(DP0+1, cur_n-last[x])
    last[x] = cur_n
    for cur_k in range(1, k+1):
        DP[cur_n][cur_k] = max(
            DP[cur_n-1][cur_k],
            DP[cur_n-DP0][cur_k-1]+DP0
        )
        ans = max(ans, DP[cur_n][cur_k])
print(ans)