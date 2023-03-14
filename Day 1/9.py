import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

for _ in range(int(input())):
    n = int(input())
#     print("Player 1 won" if n%4 else "Player 2 won")
    arr = list(map(int, input().split()))
    xor=0
    for i in range(n):
        xor ^= arr[i]
    print("Player 1 won" if xor else "Player 2 won")
