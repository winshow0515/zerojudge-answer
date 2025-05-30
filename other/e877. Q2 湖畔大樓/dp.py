#太厲害了
n = int(input())
L = []
for _ in range(n):
    h, l = map(int, input().split())
    L.append((h, l))

L.sort(key=lambda x: x[0] + x[1])
DP = [0] + [float('inf')] * n
ans = 0
print(f'L = {L}')
for h, l in L:
    print(f'h, l = {h}, {l}')
    for k in range(n, 0, -1):
        print(k)
        if DP[k-1] <= l:
            DP[k] = min(DP[k], DP[k-1]+h)
            ans = max(ans, k)
    print(DP)
print(ans)