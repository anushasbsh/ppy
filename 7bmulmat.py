def mul(m1,m2):
    res = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m2[0])):
            element = 0
            for k in range(len(m2)):
                element += m1[i][k]*m2[k][j]
            row.append(element)
        res.append(row)
    return res
def ipmat(r,c):
    mat = []
    for i in range(r):
        row = []
        for j in range(c):
            e = int(input(f"Enter element at pos ({i+1},{j+1}) :"))
            row.append(e)
        mat.append(row)
    return mat
r1=int(input())
c1 = int(input())
r2=int(input())
c2=int(input())
if(c1!=r2):
    print("They she be equal!")
else:
    print("Matrix 1:")
    m1 = ipmat(r1,c1)
    print("Matrix 2:")
    m2 = ipmat(r2,c2)
    print("Result:")
    res = mul(m1,m2)
    for row in res:
        print(row)
