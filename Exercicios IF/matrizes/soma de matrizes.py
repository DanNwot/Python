a= [[1,2],[5,7]]
b= [[7,8],[10,11]]
c= [[0,0], [0,0]]
for i in range (len(b)):
    for j in range(len (b[0])):
        c[i][j] = a[i][j] + b[i][j]
       # c[1][0] = a[1][0] + b[1][0]
       # c[1][1] = a[1][1] + b[1][1]
for i in c:
    print(i)

