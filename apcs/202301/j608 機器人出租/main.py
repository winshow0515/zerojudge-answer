import heapq
#出問題拉
N, K = map(int, input().split())
S = list(map(int, input().split()))
E = list(map(int, input().split()))
L = list(zip(E, S))
L.sort()
print(L)
a = [-1]*K
ans = 0
for e, s in L:
    if a[0] < s:
        heapq.heappop(a)
        heapq.heappush(a, e)
        ans+=1
    
    print(a)

print(ans)