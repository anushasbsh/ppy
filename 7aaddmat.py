def add(m1,m2):
    res = []
    if(len(m1)==len(m2) and len(m1[0])==len(m2[0])):
        for i in range(len(m1)):
            row =[]
            for j in range(len(m1[0])):
                row.append(m1[i][j]+m2[i][j])
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
r = int(input())
c = int(input())
print("Matrix 1:")
m1 = ipmat(r,c)
print("Matrix 2:")
m2 = ipmat(r,c)
print("Result:")
res = add(m1,m2)
for row in res:
    print(row)