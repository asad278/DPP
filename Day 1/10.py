import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

def msb(n):
    ndx = 0
    while(1<n):
        n >>= 1
        ndx += 1
    return ndx

for _ in range(int(input())):
    n = int(input())
    i = int(input())
    # Get i-th bit of a Number
    print(f"{i}-th bit:", 0 if n&(1<<i)==0 else 1)
    i = int(input())
    # Set i-th bit
    print(f"After Setting {i}-th bit:", n | (1<<i))
    i = int(input())
    # Clearing i-th bit
    print(f"After Clearing {i}-th bit:", n&~(1<<i))
    # clearing MSB
    print(f"After Clearing MSB of {n}:", n&~(1<<msb(n)))
    # MSB
    print(f"MSB's Number of {n}:", (1<<msb(n)))
