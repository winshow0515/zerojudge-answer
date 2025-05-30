#AC太神奇了加了main()就不會TLE了
def main():
    n = int(input())
    L = list(map(int, input().split()))#
    nums = []
    visit = set()
    for i in L:
        if i in visit:
            nums.append((i, 1))
        else:
            nums.append((i, 0)) 
            visit.add(i)


    def rec(L, R):
        if L+1 == R:
            return 0
        M = (L+R)//2
        #算出沒有交叉的逆對 rec(l, m), rec(m, r)
        ans = rec(L, M) + rec(M, R)

        #雙指針
        temp = []
        r = M
        for i in range(L, M):        
            while r != R and nums[i][0] > nums[r][0]:
                temp.append(nums[r])
                r += 1
            temp.append(nums[i])

            if nums[i][1] == 0:#起點
                ans += r - M
            else:
                ans -= r - M
        while r < R:
            temp.append(nums[r])
            r += 1
        nums[L:R] = temp
        return ans

    print(rec(0, 2*n))
main()