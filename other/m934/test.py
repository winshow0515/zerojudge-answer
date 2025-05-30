n = 4
ary = [3, -1, 2, 5]
dp = [[None]*100 for _ in range(100)]
#前綴和

prefix = [ary[0]] + [0]*(n-1)
for i in range(1, n): 
    prefix[i] = prefix[i-1]+ary[i]
prefix = [0] + prefix
print(prefix)
r, l = 2, 1
print(prefix[r+1] - prefix[l])