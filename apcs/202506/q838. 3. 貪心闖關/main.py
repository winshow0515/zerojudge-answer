import heapq

def main():
    n, t = map(int, input().split())
    inp = list(map(int, input().split()))
    ans = 0

    #linked list
    right = [i for i in range(1, n+2)]
    left = [i for i in range(-1, n)]

    #heapq
    h = []
    for i in range(n):
        if inp[i] == 0:
            right[left[i]] = right[i]
            left[right[i]] = left[i]
        else:
            heapq.heappush(h, (inp[i], i))
    #print(right)
    #print(left)

    
    while h:
        v, i = heapq.heappop(h)
        if v > t: break
        if v != inp[i]: continue
        inp[i] = 0   # remove i from linked list
        ans += v
        # remove i from linked list
        right[left[i]] = right[i]
        left[right[i]] = left[i]
        if right[i] < n:
            inp[right[i]] += v
            heapq.heappush(h, (inp[right[i]], right[i]))
    print(ans)
main()