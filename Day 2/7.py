import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

def fact(n, acc):
    if n==0:
        return acc;

    return fact(n-1, n*acc);

for _ in range(int(input())):
    n = int(input())
    print(fact(n, 1))
