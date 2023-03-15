import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

mp={}
def isScramble(s: str, t: str):
    if (s == t) or (not len(s)):
        return True
    if (len(s) != len(t)) or (sorted(s) != sorted(t)):
        return False
    if s+' '+t in mp:
        return mp[s+' '+t]
    flag=False
    for i in range(1, len(s)):
        if (isScramble(s[:i], t[:i]) and isScramble(s[i:], t[i:])) or (isScramble(s[-i:], t[:i]) and isScramble(s[:-i], t[i:])):
            flag=True
            return True
    mp[s+' '+t]=Flag
    return False

for _ in range(int(input())):
    s, t = input().split()
    print("Yes" if (isScramble(s, t)) else "No")
