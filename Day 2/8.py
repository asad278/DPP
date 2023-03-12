import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

def func(s, t, n, m, dp):
    if n<0 or m<0:
        return 0
    
    if dp[n][m] != -1:
        return dp[n][m]

    if s[n] == t[m]:
        dp[n][m] = 1+func(s, t, n-1, m-1, dp)
        return dp[n][m]
    dp[n][m] = max(func(s, t, n, m-1, dp), func(s, t, n-1, m, dp))
    return dp[n][m]

for _ in range(int(input())):
    s, t = input().split()
    n = len(s); m = len(t)
    dp = [[-1 for j in range(m+1)] for i in range(n+1)]
    print(func(s, t, n-1, m-1, dp))
