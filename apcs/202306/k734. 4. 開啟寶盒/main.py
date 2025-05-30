from collections import deque, defaultdict

def main():
    n, m, k = map(int, input().split())
    t = list(map(int, input().split()))
    if t == [0]:
        return 
    
    Q = deque([*t[1:]])
    lock = [0]*n        #寶箱的鎖被解鎖的數量
    keys = defaultdict(list)#鑰匙能開的寶箱
    box = [None]*n      #寶箱裡的鑰匙 list or dict
    for i in range(n):
        inp = list(map(int, input().split()))
        for j in inp:
            keys[j].append(i)
    for i in range(n):
        box[i] = list(map(int, input().split()))
    visit = [False]*m#已經用過的鑰匙

    ans = 0

    while Q:
        cur_key = Q.popleft()
        
        if visit[cur_key]:
            continue
        visit[cur_key] = True
        for i in keys[cur_key]:
            lock[i] += 1
            if lock[i] == k:
                for j in box[i]:
                    if not visit[j]:
                        Q.append(j)
                ans += 1
    print(ans)

main()