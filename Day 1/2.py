import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr[:] = arr[-1:] + arr[:-1]
    print(arr)
