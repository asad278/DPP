import sys
sys.stdin = open('inputf.in', 'r')
sys.stdout = open('outputf.out', 'w')

for _ in range(int(input())):
    r, c = map(int, input().split())

    mat = []
    for _ in range(r):
        row = list(map(int, input().split()))
        mat.append(row)

    sp=[]
    k=0; l=0
    while k<r and l<c:
        i=l
        while i<c:
            sp.append(mat[k][i])
            i+=1
        k+=1

        i=k
        while i<r:
            sp.append(mat[i][c-1])
            i+=1
        c-=1

        if k<r:
            i=c-1
            while i>=l:
                sp.append(mat[r-1][i])
                i-=1
            r-=1
        if l<c:
            i=r-1
            while i>=k:
                sp.append(mat[i][l])
                i-=1
            l+=1
    print(sp)
