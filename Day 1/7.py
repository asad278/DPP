import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    subs = [{arr[j] for j in range(n) if 1<<j&i} for i in range(1, 1<<n)]
    print(subs)
