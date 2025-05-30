from collections import deque

class Gate:
    def __init__(self):
        self.in_deg = 0
        self.type = None
        self.out = None #計算完的輸出結果
        self.inp = [] #接收到的輸入訊號
        self.nxt = [] #輸出端連到的閘
        self.delay = 0 #該gate的延遲


p, q, r, m = map(int, input().split())#輸入數量，邏輯閘數量，輸出數量，接線數量
gates = [Gate() for _ in range(p+q+r+1)] #編號從1開始，0號是空的
#輸入端
for i, in_signal in enumerate(map(int, input().split())):
    gates[i+1].out = in_signal
#邏輯閘種類
for i, gatetype in enumerate(map(int, input().split())):
    gates[p+i+1].type = gatetype
#接線
for _ in range(m):
    start, end = map(int, input().split())
    gates[start].nxt.append(gates[end])
    gates[end].in_deg += 1

Q = deque([gates[i] for i in range(1, p+1)])#先從輸入開始

while Q:
    cur = Q.popleft()
    print('cur =', gates.index(cur))
    #如果是邏輯閘則計算結果
    if cur.type == 1:#AND
        cur.out = cur.inp[0] and cur.inp[1]
    elif cur.type == 2:#OR
        cur.out = cur.inp[0] or cur.inp[1]
    elif cur.type == 3:#XOR
        cur.out = int(cur.inp[0] != cur.inp[1])
    elif cur.type == 4:#NOT
        cur.out = 1 - cur.inp[0]
    print(f'{gates.index(cur)}.out = {cur.out}')
    #將結果放到下游
    for nxt in cur.nxt:
        nxt.inp.append(cur.out)
        print(f'{gates.index(nxt)}.inp = {nxt.inp}')
        nxt.in_deg -= 1
        #更新下游延遲
        nxt.delay = max(nxt.delay, cur.delay+1) #輸出的時候記得-1，因為輸入端不算進延遲
        #如果下游gate的in_deg == 0，放進queue
        if nxt.in_deg == 0:
            Q.append(nxt)

#輸出最大delay和結果
max_delay = 0
output = []
for i in range(p+q+1, p+q+r+1):
    max_delay = max(max_delay, gates[i].delay)
    output.append(gates[i].inp[0])
print(max_delay-1)
print(*output)