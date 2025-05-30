#AC
import bisect

n, m = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
prefix = [0]*n*2
for i in range(n*2):
    prefix[i] = prefix[i-1]+P[i%n]

start = 0

for q in Q:
    if start == 0:
        start = (bisect.bisect_left(prefix, q)+1)%n
    else:
        start = (bisect.bisect_left(prefix, prefix[start-1]+q)+1)%n
print(start)