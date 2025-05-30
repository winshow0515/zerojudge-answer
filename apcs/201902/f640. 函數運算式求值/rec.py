S = input().split()
idx = 0
# 從 idx 往後看的運算式數值是多少
def rec():
    global idx
    if S[idx] == 'f':
        idx += 1
        x = rec()
        return 2*x - 3
    elif S[idx] == 'g':
        idx += 1
        x = rec()
        y = rec()
        return 2*x + y - 7
    elif S[idx] == 'h':
        idx += 1
        x = rec()
        y = rec()
        z = rec()
        return 3*x - 2*y + z
    else:
        val = int(S[idx])
        idx += 1
        return val

print(rec())