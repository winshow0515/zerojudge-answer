r, c, n = map(int, input().split())
warehouse = [[0]*c for _ in range(r)]

shapes = {'A':[(0,0),(1,0),(2,0),(3,0)],
          'B':[(0,0),(0,1),(0,2)],
          'C':[(0,0),(1,0),(1,1),(0,1)],
          'D':[(0,2),(1,0),(1,1),(1,2)],
          'E':[(1,0),(2,0),(0,1),(1,1),(2,1)]}
height = {'A':4, 'B':1, 'C':2, 'D':2, 'E':3}
width = {'A':1, 'B':3, 'C':2, 'D':3, 'E':2}
abandon = 0

for i in range(n):
    shape, h = input().split()
    h = int(h)
    start = c - width[shape]
    if h+height[shape] > r and start < 0:#高度、寬度限制
        abandon += 1
        continue

    flag = 1
    while flag:
        for dx, dy in shapes[shape]:
            if start<0 or warehouse[dx+h][dy+start] == 1:#碰到了
                start += 1#往右一步
                if start + width[shape] > c:#到底但是右邊超出範圍了
                    abandon += 1
                    flag = 0
                    break
                for x, y in shapes[shape]:
                    warehouse[x+h][y+start] = 1   #畫上去
                start = start + width[shape]
                flag = 0
                break
        else:
            start -= 1

count = 0
for i in warehouse:
    count += i.count(0)
print(count, abandon)