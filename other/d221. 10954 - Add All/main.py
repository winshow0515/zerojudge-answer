import heapq

while True:
    n = int(input())
    if n == 0:
        break
    nums = list(map(int, input().split()))
    heapq.heapify(nums)

    cost = 0
    while len(nums) > 1:
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        cost += a+b
        heapq.heappush(nums, a+b)
    print(cost)