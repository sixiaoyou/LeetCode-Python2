a=[[1,2,3],[4,5,6],[7,8,9]]
b=len(a[0])
c = len(a)
d =[[0 for i in range(c)] for j in range(b)]
print d
for i in range(b):
    for j in range(c):
        d[i][j] = a[j][i]
print d
