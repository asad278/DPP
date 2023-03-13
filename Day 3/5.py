import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

def func(e, f, dp):
    if f<=1 or e==1:
        return f

    if dp[e][f] != -1:
        return dp[e][f]

    mn = int(1e9);
    for k in range(1, f+1):
        mn = min(mn, max(func(e-1, k-1, dp), func(e, f-k, dp)))
    dp[e][f] = mn+1
    return dp[e][f]

for _ in range(int(input())):
    egg, floor = map(int, input().split())
    dp = [[-1 for j in range(floor+1)] for i in range(egg+1)]
    print(func(egg, floor, dp))
