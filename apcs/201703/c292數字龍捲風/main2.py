N = int(input())
d = int(input())
l = [input().split() for i in range(N)]

row = N//2
column = N//2
ans = l[row][column]

running = True
a = 1 #該走的長度
d_flag = 0 #每轉兩次a+=1
while running:
    if a == N:
        a -= 1
        running = False
    for i in range(a):
        if d == 0:      #laft
            column -= 1
        elif d == 1:    #up
            row -= 1
        elif d == 2:    #right
            column += 1
        else:           #down
            row += 1
        ans += l[row][column]
    d = (d + 1) % 4
    d_flag += 1
    if d_flag == 2:
        a += 1
        d_flag = 0
print(ans)