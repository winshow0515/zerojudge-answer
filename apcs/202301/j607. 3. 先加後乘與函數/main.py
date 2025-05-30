S = input()
idx = 0

def get_number():
    global idx
    if S[idx].isdigit():
        cur_digit = 0
        while idx < len(S) and S[idx].isdigit():
            cur_digit = cur_digit*10 + int(S[idx])
            idx += 1
        return cur_digit
    
    elif S[idx] == 'f':
        idx += 2
        L = []
        while True:
            L.append(rec())
            if S[idx] == ',':
                idx += 1
            else:
                idx += 1
                break
        return max(L) - min(L)

def rec():
    global idx
    ans = 1
    tmp = get_number()
    while idx<len(S):
        if S[idx] == "+":
            idx += 1
            tmp += get_number()
        elif S[idx] == "*":
            idx += 1
            ans *= tmp
            tmp = get_number()
        else:
            break
    return ans*tmp
print(rec())