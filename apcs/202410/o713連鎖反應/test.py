def ANS(sr,sc,graph):
    visited,distance,queue={(sr,sc)},defaultdict(list),deque([(sr,sc,0)])#初始走訪過、距離、BFS queue
    while queue:#計算距離
        sr,sc,r=queue.popleft()
        visited.add((sr,sc))
        distance[r].append((sr,sc))
        for cr,cc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr,nc=sr+cr,sc+cc
            if 0<=nr<row and 0<=nc<col and (nr,nc) not in visited and graph[nr][nc]>-1:
                visited.add((nr,nc))
                queue.append((nr,nc,r+1))
    #print(distance)
    visited={(sr,sc):0}#初始化引爆該格炸彈曾經的最大半徑
    for ans in range(1,max(distance)+1):#窮舉答案
        Q=deque(distance[ans])#取出達到測試半徑可以多引爆的炸彈
        print(Q)
        while Q:#每個點查看
            Q2=deque()
            x,y=Q.popleft()
            Q2.append((x,y,graph[x][y]))
            while Q2:#BFS
                x,y,r=Q2.popleft()
                if ((x,y) not in visited or visited[(x,y)]<r) and r>=0:
                    visited[(x,y)]=r#記錄引爆該格最大半徑
                    if r>0:
                        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                            nx,ny=x+dx,y+dy
                            if 0<=nx<row and 0<=ny<col and graph[nx][ny]>-1:
                                Q2.append((nx,ny,r-1))
                                if graph[nx][ny]>0:Q.append((nx,ny))#半徑>=，1可以繼續連鎖反應
        print(visited)
        if len(visited)>=q:return ans#引爆q個



from collections import deque,defaultdict
row,col,q=map(int,input().split())
maze=[]
for r in range(row):
    line=list(map(int,input().split()))
    if -2 in set(line):sr,sc=r,line.index(-2)
    maze.append(line)
print(ANS(sr,sc,maze))
