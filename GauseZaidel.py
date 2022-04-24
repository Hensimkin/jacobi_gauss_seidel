def append1(matrix1,vec1):
    newmat=[]
    for i in range(len(matrix1)):
        temp = []
        for j in range(len(matrix1[0])):
            temp.append(matrix1[i][j])
        temp.append(vec1[i][0])
        newmat.append(temp)
    print(newmat)
    return newmat


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def chechdominat2(matrix):
    count=0
    for i in range(len(matrix)):
        sum1=sum(matrix[i])
        if matrix[i][i]>sum1-matrix[i][i]:
            count+=1
    if count==len(matrix):
        print("The matrix has dominance")
    else:
        print("The matrix has no dominance")


def checkdominat(newmat,mat):
    for i in range(len(newmat)):
        sum1=sum(mat[i])
        if newmat[i][i]<sum1-newmat[i][i]:
            num=i+1
            raw=0
            count = 0
            while num!=len(newmat):
                sum2 = sum(mat[num])
                if newmat[num][i] > sum2 - newmat[num][i]:
                    raw=num
                    count+=1
                num+=1
            if count==1:
                newmat=swapPositions(newmat, i, raw)
                mat=swapPositions(mat, i, raw)
    return newmat


def f1(x,y,z):
    k=new[0][3] - (new[0][1] * y) - (new[0][2] * z)
    return k/new[0][0]

def f2(x,y,z):
    k=new[1][3] - (new[1][0] * x) - (new[1][2] * z)
    return k/new[1][1]


def f3(x,y,z):
    k = new[2][3] - (new[2][0] * x) - (new[2][1] * y)
    return k / new[2][2]

def final(matrix):
    count=1
    e=0.001
    x, y, z = 0, 0, 0
    k1, k2, k3 = 0, 0, 0
    condition=True
    while condition:
        x1 = f1(x, y, z)
        y1 = f2(x, y, z)
        z1 = f3(x, y, z)
        print('%d\t%0.4f\t%0.4f\t%0.4f\n' %(count, x1,y1,z1))
        count+=1
        k1 = abs(x - x1)
        k2 = abs(y - y1)
        k3 = abs(z - z1)
        x = x1
        y = y1
        z = z1
        condition = k1 > e and k2 > e and k3 > e
    print('\nThe solution for the matrix is: ')
    print('x=%0.3f, y=%0.3f , z = %0.3f' % (x1, y1, z1))



"""""
matrix2=[[2,10,4],[0,4,5],[4,2,0]]
matrix=[[4,2,0],[2,10,4],[0,4,5]]
vectorB=[[2],[6],[5]]
"""""
matrix2=[[4,2,0],[2,10,4],[0,4,5]]
vectorB=[[2],[6],[5]]
new=append1(matrix2,vectorB)

print(checkdominat(new,matrix2))
chechdominat2(matrix2)
final(new)