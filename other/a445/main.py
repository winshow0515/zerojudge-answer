n, m, q = list(map(int,input().split()))
boss = list(range(n+1))

def find_boss(x):
    if boss[x] == x:
        return x
    boss[x] = find_boss(boss[x])
    return boss[x]

def merge(x, y):
    boss[find_boss(y)] = find_boss(x)

for i in range(m):
    a, b = map(int,input().split())
    merge(a, b)

for j in range(q):
    a, b = map(int,input().split())

    if find_boss(a) == find_boss(b):
        print(":)")
    else:
        print(":(")