import heapq


T = int(input())
for _ in range(T):
    N = int(input())
    L = []
    for i in range(N):
        h, l = map(int, input().split())
        L.append((h, l))
    L.sort(key = lambda x: x[0]+x[1])

    pq = []
    ans, cur_h = 0, 0

    for h, l in L:
        if l >= cur_h:
            cur_h += h
            heapq.heappush(pq, -h)
            ans += 1
        elif -pq[0] > h:
            cur_h += h - (-pq[0])
            heapq.heappop(pq)
            heapq.heappush(pq, -h)
    print(ans)