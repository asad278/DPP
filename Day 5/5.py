import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

def ogs(arr, i, j, dp):
    if i>j or i>=len(arr) or j<0:
        return 0;
    if dp[i][j]!=-1:
        return dp[i][j]
    front = arr[i]+min(ogs(arr, i+1, j-1, dp), ogs(arr, i+2, j, dp))
    back = arr[j]+min(ogs(arr, i+1, j-1, dp), ogs(arr, i, j-2, dp))
    dp[i][j] = max(front, back)
    return dp[i][j]

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    dp = [[-1 for _ in range(len(arr)+1)] for _ in range(len(arr)+1)]
    print(ogs(arr, 0, len(arr)-1, dp))
