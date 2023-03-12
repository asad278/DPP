import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

for _ in range(int(input())):
	s, t = input().split()
	iso = len(set(s))==len(set(zip(s, t)))==len(set(t))
	print("Isomorphic" if iso else "Not Isomorphic")
