import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

def __gcd(a, b):
    if b==0:
        return a
    else:
        return __gcd(b, a%b)

def leftRotate(arr, n, d):
    gcd = __gcd(d, n)
    for i in range(gcd):
        tmp = arr[i]
        j=i
        while True:
            k = j+d
            if k>=n:
                k -= n
            if k==i:
                break
            arr[j] = arr[k]
            j=k
        arr[j] = tmp

for _ in range(int(input())):
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    d %= n
    leftRotate(arr, n, d)
    print(arr)
