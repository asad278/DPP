import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

def subsetEqualK(i, tar, arr, dp):
    if tar==0:
        return True
    if i==0:
        return arr[i]==tar

    if dp[i][tar]!=-1:
        return dp[i][tar]
    nt = subsetEqualK(i-1, tar, arr, dp)
    t = False
    if arr[i]<=tar:
        t = subsetEqualK(i-1, tar-arr[i], arr, dp)
    dp[i][tar] = t or nt
    return dp[i][tar]

for _ in range(int(input())):
    n, tar = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [[-1 for _ in range(tar+1)] for _ in range(n+1)]
    print("Possible" if subsetEqualK(n-1, tar, arr, dp) else "Not Possible")
