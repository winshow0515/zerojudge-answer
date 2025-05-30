#https://judge.tcirc.tw/submission/2371
#AC

n, m = map(int, input().split())
g = []
for i in range(n):
    g.append(input().split())
#print(g)
visit = {} #(x1, x2, y1, y2): cost

def count_cost(x1, x2, y1, y2):
    up = min(g[x1][y1:y2+1].count('0'), g[x1][y1:y2+1].count('1'))
    down = min(g[x2][y1:y2+1].count('0'), g[x2][y1:y2+1].count('1'))
    zero = one = 0
    for i in range(x1, x2+1):
        if g[i][y1] == '0':
            zero += 1
        else:
            one += 1
    left = min(zero, one)
    zero = one = 0
    for i in range(x1, x2+1):
        if g[i][y2] == '0':
            zero += 1
        else:
            one += 1
    right = min(zero, one)
    return up, down, left, right


def rec(x1, x2, y1, y2):
    if (x1, x2, y1, y2) in visit:
        return visit[(x1, x2, y1, y2)]
    if x1 == x2 or y1 == y2:
        visit[(x1, x2, y1, y2)] = 0
        return 0

    min_cost = float('inf')
    up, down, left, right = count_cost(x1, x2, y1, y2)
    min_cost = min(min_cost, 
                    rec(x1+1, x2, y1, y2)+up,
                    rec(x1, x2-1, y1, y2)+down,
                    rec(x1, x2, y1+1, y2)+left,
                    rec(x1, x2, y1, y2-1)+right)
    visit[(x1, x2, y1, y2)] = min_cost
    return min_cost
#print(count_cost(0, n-1, 0, m-1))

print(rec(0, n-1, 0, m-1))