#AC
"""
選的高度越低越有可能貼上，有單調性所以用二分搜找高度
關鍵函式是貪心檢查能否貼上
"""
#輸入
n, k = map(int, input().split())
H = list(map(int, input().split()))
poster = list(map(int, input().split()))

def check(h):#檢查高度h時是否能貼上
    j = 0
    l = 0   #連續寬度
    for i in range(n):
        if H[i] >= h:
            l += 1
            if l >= poster[j]:#達到足夠寬度
                j += 1
                l = 0
                if j == k:#所有海報都貼上了
                    return True
        else:#高度不足斷掉了
            l = 0
    return False #沒能貼上所有海報
                
low, hi = 1, max(H)+1#hi用max(H)會WA
while low<hi:
    mid = (low+hi)//2
    a = check(mid)
    #print(f"mid = {mid}, {a}")
    if a:#可以更高
        low = mid+1
    else:#要更矮
        hi = mid
#low-1是答案
print(low-1)