#https://hackmd.io/@bangyewu/rJlvXNP81g#%E7%AC%AC%E4%B8%89%E9%A1%8C-%E9%87%8D%E7%B5%84%E5%95%8F%E9%A1%8C-ZeroJudge-q182
n = int(input())
delta = sorted(list(map(int, input().split())))


imax = [0]*n
imin = [float('inf')]*n


def dfs(points, dist, q):
    global imax, imin

    for v in points:
        mydist = abs(v-q)
        if mydist not in dist:
            return
        dist.remove(mydist)
    points.append(q)

    if not dist:
        points.sort()
        imax = max(imax, points)
        imin = min(imin, points)
        return
    
    q = dist[-1]
    dfs(points[:], dist[:], q)
    dfs(points[:], dist[:], last-q)

#main
if n == 1:
    print(0)
    print(0)
else:
    last = delta[-1]
    dfs([0], delta, last)
    print(*imin)
    print(*imax)