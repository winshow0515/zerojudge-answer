from collections import defaultdict
#遞迴過深
n = int(input())
D = defaultdict(list)#每一個點的子孫
boss = [None]*(n)#每一個點的祖先

while True:
    try:
        a, b = list(map(int, input().split()))
        D[a].append(b)
        boss[b] = a
    except EOFError:
        break



def rec(root):
    if len(D[root]) == 0:
        return 1, 1#h, d
    height = []
    diameter = []
    for i in D[root]:
        h, d = rec(i)
        height.append(h)
        diameter.append(d)
    height.sort(reverse=True)
    diameter.sort(reverse=True)
    if len(height) > 1:
        two_h_sum = height[0]+height[1]
    else:
        two_h_sum = height[0]

    return 1+max(height), max(max(diameter),1+two_h_sum)

print(rec(boss.index(None))[1] - 1)