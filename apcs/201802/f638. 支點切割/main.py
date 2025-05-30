#WA 我不知道哪裡錯 問老師
n, K = map(int, input().split())
p = list(map(int, input().split()))
prefix = [0]*n
prefix[0] = p[0]
for i in range(1, n):
    prefix[i] = prefix[i-1] + p[i]
ans = 0

def rec(left, right, k):
    #判斷能不能切
    if k==K or right-left<2:
        return
    global ans
    #初始化#選left當支點的時候
    temp = 0
    count = 1
    for i in range(left+1, right+1):
        temp += p[i]*count
        count += 1

    #找最佳切點
    m = (float("inf"), float("inf"))
    for i in range(left+1, right):
        if left==0:
            temp += prefix[i-1] - (prefix[right]-prefix[i-1])
        else:
            temp += (prefix[i-1]-prefix[left-1]) - (prefix[right]-prefix[i-1])
        m = min(m, (temp, i))
    ans += p[m[1]]
    
    #切下去
    rec(left, m[1]-1, k+1)
    rec(m[1]+1, right, k+1)

rec(0, n-1, 0)
print(ans)