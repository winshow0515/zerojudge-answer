#參考https://www.youtube.com/watch?v=jASSa3w7rHU

import bisect
n = int(input())
points = []
for i in range(n):
    points.append(tuple(map(int,input().split())))
points.sort()
#print(points)


dp = [] #裝y座標
for i in range(n):  #因為x座標由小到大一定是合理的
    index = bisect.bisect_right(dp, points[i][1])     #points[i][1]是y座標
    if index >= len(dp):
        dp.append(points[i][1])
    else:                   #愈小的y座標明顯是更有機會的
        dp[index] = points[i][1]
    #print(dp)
print(len(dp))


#print(points) [(1,1),(2,5),(3,2)]
# LIS + 二分搜, bisect 優化


'''
def bin_search(v):  #回傳這個y座標應被插入的位置
    left, right, mid = 0, len(dp), 0
    while left != right:
        mid = left + (right - left) // 2
        if v >= dp[mid]:
            left = mid + 1
        else:
            right = mid
    return left
'''