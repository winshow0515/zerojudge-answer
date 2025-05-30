s,t,n,m,r = map(int,input().split())
a_sum = 0
A=[]
for i in range(s):
    inp = list(map(int,input().split()))
    A.append(inp)
    a_sum += sum(inp)
B=[]
for i in range(n):
    B.append(list(map(int,input().split())))
'''輸入成功
print("s,t,n,m,r = ",s,t,n,m,r)
print("A =", A)
print("B =", B)'''

margin = float("inf")
count = 0
for i in range(n-s+1):#這兩層是來跑能把A放進B位置
    for j in range(m-t+1):#(i,j)左上角
        diff = 0
        b_sum = 0
        for a in range(s):
            for b in range(t):
                #紀錄有幾個不合，需小於r
                if A[a][b] != B[i+a][j+b]:
                    diff += 1
                    if diff > r:
                        break
                #加總框住的B
                b_sum += B[i+a][j+b]
            if diff > r:
                break
        else:#沒被break，符合條件
            count += 1
            margin = min(abs(a_sum - b_sum), margin)
print(count)
if margin == float("inf"):
    print(-1)
else:
    print(margin)