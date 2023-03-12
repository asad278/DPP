import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

for _ in range(int(input())):
	n = int(input())
	mat = []
	for _ in range(n):
		row = list(map(int, input().split()))
		mat.append(row)

	for i in range(n):
		mat[i].reverse()

	for i in range(n):
		for j in range(i, n):
			mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

	print(mat)