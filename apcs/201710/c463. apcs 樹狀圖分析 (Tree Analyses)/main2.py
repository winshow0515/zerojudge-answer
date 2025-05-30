n = int(input())
tree = [None]
s = set()
for i in range(n):
    inp = list(map(int, input().split()))
    if inp == [0]:
        tree.append([])
    else:
        tree.append(inp[1:])
        for j in inp[1:]:
            s.add(j)

# 找 root
root = list(set(range(1, n + 1)) - s)[0]
print(root)

# 非遞迴 DFS，計算每個節點高度
total = 0
height = [0] * (n + 1)  # height[i] 是節點 i 的高度
visited = [False] * (n + 1)
stack = []

stack.append((root, False))  # (節點, 是否已處理完子節點)

while stack:
    node, visited_flag = stack.pop()
    if visited_flag:
        # 子節點都處理完了，計算自己的高度
        h = 0
        for child in tree[node]:
            h = max(h, height[child] + 1)
        height[node] = h
        total += h
    else:
        # 還沒處理子節點，先把自己推回去，再推子節點
        stack.append((node, True))
        for child in tree[node]:
            if child != 0:
                stack.append((child, False))

print(total)