import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    xr=0
    for i in arr:
        xr ^= i
    num1=num2=0; msb=xr&~(xr-1)
    for i in arr:
        if i&msb:
            num1 ^= i
        else:
            num2 ^= i
    print(num1, num2)
