import sys
import bisect as bi
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    pref = [sum(arr[:i+1]) for i in range(n)]
    q = int(input())
    while q:
        e = int(input())
        idx = bi.bisect_left(arr, e, lo=0, hi=n)
        print(idx+1 if idx<n else n, end=" ")
        print(pref[idx] if idx<n else pref[n-1])
        q-=1
