#AC
def main():
    n = int(input())
    tmp = list(map(int, input().split()))
    visit = set()
    ary = []
    for i, x in enumerate(tmp):
        if x in visit:
            ary.append((x, 1, i))
        else:
            visit.add(x)
            ary.append((x, 0, i))
    cnt = [0] * (2*n)
    
    def rec(L, R):
        if L+1 == R:
            return 
        M = (L + R) // 2
        rec(L, M)
        rec(M, R)
        r = M
        tmp = []
        for l in range(L, M):
            while r < R and ary[r] < ary[l]: 
                tmp.append(ary[r])
                r += 1
            tmp.append(ary[l])
            cnt[ary[l][2]] += r - M
        while r < R:
            tmp.append(ary[r])
            r += 1
        ary[L:R] = tmp
    
    
    rec(0, len(ary))
    ans = 0
    for (_, who, i) in ary:
        if who == 0:
            ans += cnt[i]
        else:
            ans -= cnt[i]
    print(ans)
main()