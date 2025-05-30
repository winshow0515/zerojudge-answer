#TLE 我自己寫的

n, m, p = map(int,input().split())
buses = []
buses.append(map(int,input().split()))
buses.append(map(int,input().split()))
buses = list(zip(buses[0],buses[1]))
#print(buses)[(0, 4), (4, 6), (0, 6), (3, 7), (5, 9)]
memo = [None]*(m+1)

def dp(cur):
    if memo[cur]:
        return memo[cur]
    if cur == m:
        return 1
    elif cur > m:
        return 0
    ans = 0
    for bus in buses:
        if bus[0] <= cur < bus[1]:
            ans += dp(bus[1])
    memo[cur] = ans
    return ans

print(dp(0)%p)