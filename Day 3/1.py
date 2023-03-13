import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

def josephus(n, k):
	if n==1:
		return 1
	return (josephus(n-1, k) + k-1)%n+1

def towerofhanoi(n, src, dest, helper):
	if n==0:
		return
	towerofhanoi(n-1, src, helper, dest)
	print(f"Move disk {n} from {src} to {dest}")
	towerofhanoi(n-1, helper, dest, src)

n, k = map(int, input().split())
print(f"Josephus Problem\nFor n={n} & k={k}:", josephus(n, k))

n = int(input())
print(f"\nTower of Hanoi\nFor n={n}:")
towerofhanoi(n, 'A', 'C', 'B')