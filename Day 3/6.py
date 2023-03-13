import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

def lcs(i, j, s, t, dp):
    if i<0 or j<0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if s[i]==t[j]:
        dp[i][j] = 1+lcs(i-1, j-1, s, t, dp)
        return dp[i][j]
    dp[i][j] = max(lcs(i-1, j, s, t, dp), lcs(i, j-1, s, t, dp))
    return dp[i][j]

for _ in range(int(input())):
    s = input()
    t = "".join(reversed(s))
    dp = [[-1 for j in range(len(s)+1)] for i in range(len(s)+1)]
    print(lcs(len(s)-1, len(s)-1, s, t, dp))
