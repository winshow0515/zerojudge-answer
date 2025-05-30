#AC

import sys
sys.setrecursionlimit(10**6)

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
prefix = [0]
s = 0
for i in nums:
    s += i
    prefix.append(s)

m = [(x, i) for i, x in enumerate(nums)]
m.sort(reverse=True)
L = [(0, n)]
while L:
    l, r = L.pop()
    if l+1 == r:
        print(nums[l])
        break
    #找最小
    min_num = m.pop()[1] 
    while not(l <= min_num < r):
        min_num = m.pop()[1]
    
    #m = nums.index(min(nums[l:r]))#O(n^2)


    #區間和
    if prefix[r]-prefix[min_num+1] >= prefix[min_num]-prefix[l]:
        L.append((min_num+1, r))
    else:
        L.append((l, min_num))