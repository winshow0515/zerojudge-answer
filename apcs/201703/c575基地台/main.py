#AC

N, K = map(int, input().split())
P = sorted(list(map(int, input().split())))

def trail(d):
    if d == 0:
        return False

    line = P[0]+d
    quota = K-1
    for i in P[1:]:
        
        if line < i:
            if quota != 0:
                line = i+d
                quota -= 1
            else:
                return False
    return True

#對答案二分搜
L = 0
R = P[-1]

while L < R:
    mid = (L+R)//2
    if trail(mid):
        R = mid
    else:
        L = mid+1
print(L)