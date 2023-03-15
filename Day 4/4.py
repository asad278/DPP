import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

def unKnapsack(wt, profit, i, w, dp):
    if i==0:
        return (w//wt[0])*profit[0]
    
    if dp[i][w]!=-1:
        return dp[i][w]
    
    nt = unKnapsack(wt, profit, i-1, w, dp)
    t = -int(1e9)
    if wt[i]<=w:
        t = profit[i]+unKnapsack(wt, profit, i, w-wt[i], dp)
    dp[i][w] = max(nt, t)
    return dp[i][w]

for _ in range(int(input())):
    n, w = map(int, input().split())
    profit = list(map(int, input().split()))
    wt = list(map(int, input().split()))
    dp = [[-1 for _ in range(w+1)] for _ in range(n+1)]
    print(unKnapsack(wt, profit, n-1, w, dp))
