import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    curr=0; total=0
    for i in range(n):
        curr += arr[i]
        total = max(total, curr)
        if curr<0:
            curr=0
    if total==0:
        total = max(arr)
    print(total)
