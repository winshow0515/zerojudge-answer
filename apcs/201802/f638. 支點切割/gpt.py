n, K = map(int, input().split())
p = list(map(int, input().split()))

# 計算前綴和
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + p[i]

ans = 0

def rec(left, right, k):
    # 若已達最大切割次數，或區間小於 3，則無法再切割
    if k == K or right - left < 2:
        return
    
    global ans

    # 計算加權和
    temp = 0
    for i in range(left + 1, right + 1):
        temp += (i - left) * p[i]  # i 相對於 left 的權重累加

    # 找最佳切割點
    best_cut = -1
    min_cost = float("inf")

    for i in range(left + 1, right):
        left_cost = prefix[i] - prefix[left]  # 左半部的總和
        right_cost = prefix[right + 1] - prefix[i + 1]  # 右半部的總和
        total_cost = left_cost + right_cost

        if total_cost < min_cost:
            min_cost = total_cost
            best_cut = i

    if best_cut == -1:  # 若找不到合法切割點，則直接返回
        return
    
    ans += p[best_cut]  # 加上切割點的值

    # 遞迴切割左右區間
    rec(left, best_cut - 1, k + 1)
    rec(best_cut + 1, right, k + 1)

rec(0, n - 1, 0)
print(ans)