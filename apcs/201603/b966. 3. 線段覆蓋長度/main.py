#AC
n = int(input())
A = []
for i in range(n):
    l, r = map(int, input().split())
    A.append((l, r))
A.sort()
total = 0
cur_r = -1
for l, r in A:
    if l > cur_r:
        cur_r = r
        total += r - l
    elif r > cur_r:
        total += r-cur_r
        cur_r = r
print(total)