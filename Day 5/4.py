import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

def ways(n, m, x, dp):
    if (x<0) or (n==0 and x!=0) or (n!=0 and x==0):
        return 0
    if n==0 and x==0:
        return 1
        
    if dp[n][x]!=-1:
        return dp[n][x]
    
    ans = 0
    for i in range(1,m+1):
        ans += ways(n-1,m,x-i,dp)
    
    dp[n][x] = ans
    return dp[n][x]

for _ in range(int(input())):
    n, m, x = map(int, input().split())
    dp = [[-1 for _ in range(x+2)] for _ in range(n+1)]
    print(ways(n, m, x, dp))
