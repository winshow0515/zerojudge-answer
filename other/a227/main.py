#AC
def rec(n, start, target, temp):
    if n == 0:
        return
    rec(n-1, start, temp, target)
    print(f'Move ring {n} from {start} to {target}')
    rec(n-1, temp, target, start)

#循環測資
while True:
    try:
        n = int(input())
        rec(n, 'A', 'C', 'B')
        print()
    except:
        break