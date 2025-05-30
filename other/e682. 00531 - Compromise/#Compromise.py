#e682. 00531 - Compromise https://zerojudge.tw/ShowProblem?problemid=e682
#為什麼WA，明明範例過了啊｡ﾟ(ﾟ´ω`ﾟ)ﾟ｡
#太難了先放棄

def rec(i, j):
    if i == -1 or j == -1:
        return ''
    if dp[i][j]:
        return dp[i][j]
    if s1[i] == s2[j]:
        dp[i][j] = rec(i-1, j-1) + s1[i] + ' '
    else:
        if len(rec(i-1, j)) >= len(rec(i, j-1)):
            dp[i][j] = rec(i-1, j)
        else:
            dp[i][j] = rec(i, j-1)
    return dp[i][j]


flag = 0
s1 = []
s2 = []
while True:
    try:
        s = input()
    except:
        break

    if s == '#':
        flag += 1
    else:
        if flag == 0:#第1遍中
            s1.append(s)
        elif flag == 1:#第2遍中
            s2.append(s)
        else:#兩個都輸入完了
            dp = [[None]*(len(s2)) for _ in range(len(s1))]
            print(rec(len(s1)-1, len(s2)-1))
            flag = 0
            s1 = []
            s2 = []


'''
s = ['die', 'einkommen', 'der', 'landwirte',
'sind', 'fuer', 'die', 'abgeordneten', 'ein', 'buch', 'mit' 'sieben', 'siegeln',
'um', 'dem', 'abzuhelfen',
'muessen', 'dringend', 'alle', 'subventionsgesetze', 'verbessert', 'werden',
'#',
'die', 'steuern', 'auf', 'vermoegen', 'und', 'einkommen',
'sollten', 'nach', 'meinung', 'der', 'abgeordneten',
'nachdruecklich', 'erhoben', 'werden'
'dazu', 'muessen', 'die', 'kontrollbefugnisse', 'der', 'finanzbehoerden',
'dringend', 'verbessert', 'werden',
'#']'''