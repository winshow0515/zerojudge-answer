#AC
n = input()
odd = 0
even = 0
for i in range(len(n)-1, -1, -1):
    if i%2 == 0:#奇數位
        odd += int(n[i])
    else:
        even += int(n[i])
print(abs(odd-even))