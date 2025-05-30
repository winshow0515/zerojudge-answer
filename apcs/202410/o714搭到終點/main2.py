#AC
#所以它哪裡有離散化
import bisect
from collections import defaultdict
n, m, p = map(int,input().split())
startlist =  list(map(int,input().split()))
endlist = list(map(int,input().split()))
buses = sorted(list(zip(endlist, startlist)))#[(4, 0), (6, 0), (6, 4), (7, 3), (9, 5)](終站, 起站)

endlist = sorted(set(endlist))
stations = defaultdict(list)
for i,j in buses:
    stations[i].append(j)

prefixs = [(-1,0), (0, 1)]
prefix = 1 #搭到第0站的方法有1種


for end in endlist:
    dp = 0
    for start in stations[end]:
        idx = bisect.bisect_left(prefixs, (start, )) #(start, )原來可以空著喔
        dp += prefix - prefixs[idx-1][1]
        dp %= p
    prefix = (prefix + dp)%p
    prefixs.append((end, prefix))

print(dp if prefixs[-1][0] == m else 0)