import bisect as bi
def lis_bs(arr):
    seq = []
    seq.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i]>seq[-1]:
            seq.append(arr[i])
        else:
            idx=bi.bisect_left(seq, arr[i], 0, len(seq))
            seq[idx] = arr[i]
    return len(seq)

def lis(i, prev, arr, dp):
    if i==len(arr):
        return 0
    if dp[i][prev+1]!=-1:
        return dp[i][prev+1]
    l = lis(i+1, prev, arr, dp)
    if prev==-1 or arr[i]>arr[prev]:
        l = max(l, 1+lis(i+1, i, arr, dp))
    dp[i][prev+1]=l
    return dp[i][prev+1]

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    dp = [[-1 for _ in range(len(arr)+1)] for _ in range(len(arr)+1)]
    print(lis(0, -1, arr, dp))
    print(lis_bs(arr))