n = int(input())
d = int(input())
graph = [input().split() for _ in range(n)]

row = n//2
colum = n//2
output = graph[row][colum]
# 0代表左 、1代表上 、2代表右 、3代表下
direction = [(0,-1),(-1,0),(0,1),(1,0)]

step = 1
running = 1
owntwo = 0
while running:#每走兩步，步數加一
    #走啊
    for i in range(step):
        row += direction[d][0]
        colum += direction[d][1]
        if not(0<=row<n and 0<=colum<n):
            running = 0
            break
        output += graph[row][colum]
    #轉
    d = (d+1)%4
    if owntwo==0:
        owntwo = 1
    else:
        step = step+1
        owntwo = 0
print(output)
#9123857324243421496834621
