#AC，學到了遞迴容易出錯
n = int(input())
friends = list(map(int, input().split()))
visit = set()

count = 0
for i in range(n):
    if i not in visit:
        visit.add(i)
        pos = friends[i]
        while pos != i:
            visit.add(pos)
            pos = friends[pos]
        count += 1
print(count)