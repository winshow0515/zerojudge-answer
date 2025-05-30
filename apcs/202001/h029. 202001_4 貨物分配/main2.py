import sys
sys.setrecursionlimit(100005)

class Node:
    def __init__(self, name):
        self.weight = 0
        self.l = None
        self.r = None
        self.parent = None
        self.name = name
    
    def dfs(self):
        if self.l is not None:
            if self.l.l is not None:
                self.l.weight += self.l.l.dfs()
            if self.l.r is not None:
                self.l.weight += self.l.r.dfs()
            self.weight+= self.l.weight
        if self.r is not None:
            if self.r.l is not None:
                self.r.weight += self.r.l.dfs()
            if self.r.r is not None:
                self.r.weight += self.r.r.dfs()
            self.weight+= self.r.weight
        return self.weight

n, m = map(int, input().split())
start_w = list(map(int, input().split()))
inp = list(map(int, input().split()))
nodes = []
for i in range(n*2):
    nodes.append(Node(i))

for i in range(n):
    nodes[n + i].weight = start_w[i]

for _ in range(n-1):
    p, s, t = map(int, input().split())
    nodes[p].l = nodes[s]
    nodes[p].r = nodes[t]
    nodes[s].parent = nodes[p]
    nodes[t].parent = nodes[p]

nodes[1].dfs()

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