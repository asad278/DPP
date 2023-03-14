def isPalin(x):
    return x==x[::-1]

def pp_recurr(s, i, j, dp):
    if i>=j or isPalin(s[i:j+1]):
        return 0
    
    if dp[i][j]!=-1:
        return dp[i][j]
    
    dp[i][j] = int(1e9)
    for k in range(i, j):
        cnt = 1+pp_recurr(s, i, k, dp)+pp_recurr(s, k+1, j, dp)
        dp[i][j] = min(dp[i][j], cnt)
    return dp[i][j]

def palindromePartition():
    s = input()
    dp = [[-1 for j in range(len(s))] for i in range(len(s))]
    print(pp_recurr(s, 0, len(s)-1, dp))

def k_recurr(i, wt, cost, w, dp):
    if i==0:
        return wt[0] if wt[0]<=w else 0
    
    if dp[i][w]!=-1:
        return dp[i][w]
    
    nt = k_recurr(i-1, wt, cost, w, dp)
    t = -int(1e9)
    if wt[i]<=w:
        t = cost[i]+k_recurr(i-1, wt, cost, w-wt[i], dp)
    dp[i][w] = max(nt, t)
    return dp[i][w]

def knapsack():
    wt = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    w = int(input())
    n = len(wt)
    dp = [[-1 for j in range(w+1)] for i in range(n+1)]
    print(k_recurr(n-1, wt, cost, w, dp))

for _ in range(int(input())):
    palindromePartition()
    knapsack()