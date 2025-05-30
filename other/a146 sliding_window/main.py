#TLE 
import sys
from collections import deque
#循環測資輸入
while True:
    t1 = sys.stdin.readline()
    if t1 == '':
        break

    n, k = list(map(int, t1.split()))
    l = list(map(int,sys.stdin.readline().split()))


    ans = []
    dp = deque([])
    #minimum
    for i in range(n):
        while dp and dp[0] <= i-k:
            dp.popleft()
        while dp and l[dp[-1]] > l[i]:
            dp.pop()
        dp.append(i)
        if i >= k-1:
            ans.append(l[dp[0]])
    print(*ans)

    ans = []
    dp = deque([])
    for i in range(n):
        while dp and dp[0] <= i-k:
            dp.popleft()
        while dp and l[dp[-1]] < l[i]:
            dp.pop()
        dp.append(i)
        if i >= k-1:
            ans.append(l[dp[0]])
    print(*ans)



'''
while True:
    try:
        minimum = []
        maximum = []
        n, k = map(int,input().split())
        l = list(map(int,input().split()))
        for i in range(n-k+1):
            #print(l[i:i+k])
            minimum.append(str(min(l[i:i+k])))
            maximum.append(str(max(l[i:i+k])))
        print(' '.join(minimum))
        print(' '.join(maximum))
    except EOFError:
        break'''