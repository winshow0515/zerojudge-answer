n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
#5 2 0 6 9 6
print(l)

def f(x, l):#x是選擇的開會座標，l是能選座標，選k個
    a = []
    for i in l:
        a.append((abs(i-x), i))
    a.sort()
    print(a)
    #要回傳最小移動距離總和，和剩下能選的座標
    return sum([d for d, x in a[:k]]), [x for d, x in a[k:]]
    

ans = 0
for i in range(n):#選第一個開會位置
    first_sum, l2 = f(i, l)
    for j in range(i, n):#選第二個開會位置
        second_sum, _ = f(j, l2)
        ans = min(ans, first_sum+second_sum)
print(ans)
