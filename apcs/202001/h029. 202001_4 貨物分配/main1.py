import sys
sys.setrecursionlimit(3000)

class Node:
    def __init__(self, name):
        self.weight = 0
        self.l = None
        self.r = None
        self.parent = None
        self.name = name
    
    def updata(self, w):
        node = self
        while node != None:
            node.weight += w
            node = node.parent

n, m = map(int, input().split())
start_w = list(map(int, input().split()))
inp = list(map(int, input().split()))
nodes = []
for i in range(n*2):
    nodes.append(Node(i))

for _ in range(n-1):
    p, s, t = map(int, input().split())
    nodes[p].l = nodes[s]
    nodes[p].r = nodes[t]
    nodes[s].parent = nodes[p]
    nodes[t].parent = nodes[p]

for i in range(n):
    nodes[i+n].updata(start_w[i])

def push(cur_node, w):
    while cur_node.l != None and cur_node.r != None:
        cur_node.weight += w
        if cur_node.l.weight <= cur_node.r.weight:
            cur_node = cur_node.l
        else:
            cur_node = cur_node.r
    cur_node.weight += w
    return cur_node.name

ans = []
for i in range(m):
    ans.append(push(nodes[1], inp[i]))
print(*ans)