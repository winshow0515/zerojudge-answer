#AC
while True:
    try:
        n = int(input())
        L = []
        w = list(map(int, input().split()))
        f = list(map(int, input().split()))
        for i in range(n):
            if f[i] == 0:
                L.append((1001, w[i], f[i]))
            else:
                L.append((w[i]/f[i], w[i], f[i]))
        
        L.sort()
        #print(L)
        total = 0
        w_sum = L[0][1]
        for i in range(1, n):
            total += L[i][2] * w_sum
            w_sum += L[i][1]
        print(total)
    except EOFError:
        break