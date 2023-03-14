def ways(coins, i, tar, dp):
    if i==0:
        return tar%coins[0]==0
    if dp[i][tar]!=-1:
        return dp[i][tar]

    nt = ways(coins, i-1, tar, dp)
    t = 0
    if coins[i]<=tar:
        t = ways(coins, i, tar-coins[i], dp)
    dp[i][tar] = nt+t
    return dp[i][tar]

def minCoins(coins, i, tar, dp):
    if i==0:
        return tar//coins[0] if tar%coins[0]==0 else int(1e9)
    if dp[i][tar]!=-1:
        return dp[i][tar]

    nt = minCoins(coins, i-1, tar, dp)
    t = int(1e9)
    if coins[i]<=tar:
        t = 1+minCoins(coins, i, tar-coins[i], dp)
    dp[i][tar]=min(t, nt)
    return dp[i][tar]

for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, input().split()))
    tar = int(input())
    dp = [[-1 for j in range(tar+1)] for i in range(n+1)]
    print(f"Ways to get {tar}:", ways(coins, n-1, tar, dp))
    dp = [[-1 for j in range(tar+1)] for i in range(n+1)]
    print(f"Minimum coins for {tar}:", minCoins(coins, n-1, tar, dp))
