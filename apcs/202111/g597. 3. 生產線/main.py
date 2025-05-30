#AC
n, m = map(int, input().split())

needs = [0]*n
for i in range(m):
    l, r, w = map(int, input().split())
    needs[l-1] += w
    if r != n:
        needs[r] -= w
#前綴和
for i in range(1, n):
    needs[i] += needs[i-1]
needs.sort(reverse=True)

#print(needs)
T = sorted(list(map(int, input().split())))
ans = 0
for i in range(n):
    ans += T[i]*needs[i]
print(ans)
