#a587. 祖靈好孝順 ˋˇˊ DP
#https://zerojudge.tw/ShowProblem?problemid=a587
#TLE


def f(n, w):
    if n == 0:
        return 0
    
    if w >= W[n]:
        return max(f(n-1, w-W[n])+V[n] ,f(n-1, w))
    return f(n-1, w)

N = int(input())
W = [0]
V = [0]
for i in range(N):
    w, v = list(map(int, input().split()))
    W.append(w)
    V.append(v)
limit = int(input())

print(f(N, limit))