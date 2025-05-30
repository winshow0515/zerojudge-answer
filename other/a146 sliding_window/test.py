import sys
while True:
    t1 = sys.stdin.readline().strip()
    if t1 == '':
        break
    n, k = t1.split()
    t2 = sys.stdin.readline().strip()
    
    print(n, k)
    print(t2.split())