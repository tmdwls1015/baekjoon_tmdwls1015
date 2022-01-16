def makeStar(mat,N,beginX,beginY):
    if N==3:
        mat[beginX+1][beginY+1]=' '
    else:
        nextN = N//3
        for r in range(0,3):
            for c in range(0,3):
                bx = beginX+(r*nextN)
                by = beginY+(c*nextN)

                if r==1 and c==1:
                    for i in range(bx,bx+nextN):
                        for j in range(by,by+nextN):
                            mat[i][j]=' '
                    continue
                makeStar(mat,nextN,bx,by)


N = int(input())
mat = [['*' for i in range(0, N)] for j in range(0,N)]

makeStar(mat,N,0,0)
for i in range(N):
    for j in range(N):
        print(mat[i][j],end='')
    print()