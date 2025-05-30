from collections import deque

def f(x):
    return 2*x - 3
def g(x, y):
    return 2*x + y - 7
def h(x, y, z):
    return 3*x - 2*y + z

def push_digit(a):
    if st and st[-1] == 'f':
        b = f(a)
        st.pop()
        push_digit(b)
    elif len(st)>= 2 and type(st[-1]) == int and st[-2] == 'g':
        b = g(st[-1], a)
        st.pop()
        st.pop()
        push_digit(b)
    elif len(st)>= 3 and type(st[-1]) == int and type(st[-2]) == int and st[-3] == 'h':
        b = h(st[-2], st[-1], a)
        for _ in range(3):
            st.pop()
        push_digit(b)
    else:
        st.append(a)

st = deque([])
inp = input().split()

for i in range(len(inp)):
    j = inp[i]
    if not j.isalpha():#是數字
        push_digit(int(j))
    else:
        st.append(j)
    
print(st[0])