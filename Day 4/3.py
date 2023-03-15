import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

def rodcut(rods, i, n, dp):
    if i==0:
        return n*rods[0]

    if dp[i][n]!=-1:
        return dp[i][n]

    nt = rodcut(rods, i-1, n, dp)
    t = -int(1e9)
    if i+1<=n:
        t = rods[i]+rodcut(rods, i, n-i-1, dp)
    dp[i][n]=max(t, nt)
    return dp[i][n]

for _ in range(int(input())):
    n = int(input())
    rods = list(map(int, input().split()))
    dp = [[-1 for j in range(n+1)] for i in range(n+1)]
    print(rodcut(rods, n-1, n, dp))
