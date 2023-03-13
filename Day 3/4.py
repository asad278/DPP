import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

def func(arr, i, j, dp):
    if i==j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    mn = int(1e9)
    for k in range(i, j):
        steps = arr[i-1]*arr[k]*arr[j] + func(arr, i, k, dp) + func(arr, k+1, j, dp)
        mn = min(mn, steps)
    return mn

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    dp = [[-1 for j in range(len(arr)+1)] for i in range(len(arr)+1)]
    print(func(arr, 1, len(arr)-1, dp))
