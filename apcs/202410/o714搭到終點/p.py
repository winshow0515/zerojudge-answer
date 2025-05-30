#我的參考
#https://colab.research.google.com/drive/1jnX4JvDWejyQxpHHfX_EsA0_Hx0ENaiy?hl=en#scrollTo=x1_aJTNd7fLe

from sys import stdin
from bisect import bisect_left
from itertools import groupby
from operator import itemgetter
e = stdin.readline

n, m, p = map(int, e().split())
s, f = map(int, e().split()), map(int, e().split())
l = sorted(zip(f, s))  # 按照終點站升冪排序

# 紀錄當前綴和 (搭到第0站有1種方法)
prefix = 1
# prefixes: list[tuple[int, int]] 表示(終點站, 前綴和)
prefixes = [None] * (n + 2)  # 先開好 省時間
# 前綴和sentinel 方便計算
prefixes[0] = (-1, 0)
prefixes[1] = (0, 1)
# 窮舉終點站(相同終點站一起處理 才不會互相重複算到)
for i, (f, g) in enumerate(groupby(l, key=itemgetter(0)), start=2):
    idx = dp = 0  # 二分搜index(由0開始搜), 可以轉移到此終點站f的前置狀態總和
    for _, s in g:
        # 二分搜轉移點 (left most f >= s)
        # f相同時s升冪 因此可以從上一個搜到的index開始搜
        idx = bisect_left(prefixes, (s, ), lo=idx, hi=i)
        # 由前綴和 累計[s, f)的方法總和
        print('idx',idx)
        dp += prefix - prefixes[idx - 1][1]
        dp %= p
        print('dp', dp)
        
    # 更新前綴和
    prefix = (prefix + dp) % p
    print(prefix)
    prefixes[i] = (f, prefix)
    print(prefixes)
# 取最後一個終點站的值 如果最後一個終點站不是m的話就代表到不了
print(dp % p if f == m else 0)