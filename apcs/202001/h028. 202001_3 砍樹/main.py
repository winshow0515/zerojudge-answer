n, l = map(int, input().split())
tree = list(map(int, input().split()))
h = list(map(int, input().split()))
tree = list(zip(tree, h))+[(l, float('inf'))]

ans = [0, 0]
stack = [(0, float('inf'))]
for idx, h in tree:
    while idx-stack[-1][0] >= stack[-1][1]:    
        ans[0] += 1
        ans[1] = max(ans[1], stack[-1][1])
        stack.pop()

    if idx-stack[-1][0] >= h:
        ans[0] += 1
        ans[1] = max(ans[1], h)
    else:
        stack.append((idx, h))
print(ans[0])
print(ans[1])