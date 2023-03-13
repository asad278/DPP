import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

def getmid(arr, n):
    if n&1:
        return arr[int(n/2)]
    return (arr[int(n/2)]+arr[int(n/2)-1])/2

def median(arr1, arr2, n):
    if n<=2:
        return (max(arr1[0], arr2[0])+min(arr1[1], arr2[1]))/2
    mid1 = getmid(arr1, n)
    mid2 = getmid(arr2, n)
    if mid1>mid2:
        return median(arr2, arr1, n)
    if n&1:
        return median(arr1[int(n/2):], arr2[0:int(n/2)+1], int(n/2)+1)
    return median(arr1[int(n/2-1):], arr2[:int(n/2+1)], int(n/2)+1)

for _ in range(int(input())):
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    print(median(arr1, arr2, len(arr1)))
