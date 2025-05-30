import bisect

N, K = map(int, input().split())
S = list(map(int, input().split()))
E = list(map(int, input().split()))
L = list(zip(E, S))
L.sort()

a = [-1]*K
ans = 0
for e, s in L:
    if a[0] < s:
        index = bisect.bisect_left(a, s)
        if index > 0:
            ans+=1
            a.pop(index-1)
            a.append(e)

print(ans)