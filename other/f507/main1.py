#TLE
#編輯距離
s1_len, s1 = input().split()
s2_len, s2 = input().split()
s1_len = int(s1_len)
s2_len = int(s2_len)
def rec(i, j):
    if i == -1:
        return j+1
    elif j == -1:
        return i+1
    if s1[i] == s2[j]:
        return rec(i-1, j-1)
    else:
        return min(rec(i-1, j), rec(i, j-1), rec(i-1, j-1))+1

print(rec(s1_len-1, s2_len-1))