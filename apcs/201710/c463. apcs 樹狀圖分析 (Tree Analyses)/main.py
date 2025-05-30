n = int(input())
tree = [None]
s = set()
for i in range(n):
    inp = list(map(int, input().split()))
    if inp == [0]:
        tree.append([0])
    else:
        tree.append(inp[1:])
        for j in inp[1:]:
            s.add(j)

#找root
root = list(set(range(1,n+1))-s)[0]
print(root)
#找高度總和
total = 0

def rec(root):
    if root == 0:
        return 0
    global total
    h = 0
    for nxt in tree[root]:
        if nxt == 0:
            return 0
        h = max(h, rec(nxt)+1)
    total += h
    return h
rec(root)
print(total)