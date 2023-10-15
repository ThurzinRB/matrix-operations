
def multiplyScalar(a , b):
    a = a.strip()
    b = b.strip()
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    return '((' +  a + ')*(' + b + '))'

def divideScalar(a , b):
    a = a.strip()
    b = b.strip()
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    return '((' +  a + ')/(' + b + '))'


def addScalar(a , b):
    a = a.strip()
    b = b.strip()
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a
    
    
    operationSign = '+'
    if (b[0] == '-'):
        operationSign = '-'
        b = b[1:]
        b = b.strip()

    return '(' +  a + operationSign + b + ')'

def subtractScalar(a, b):
    return addScalar(a, '-'+ b)

def getIndividualElement(A,B, i, j):
    m = len(A)
    n = len(B)
    cij = ''
    for k in range(n):
        print(k)
        cij = addScalar(cij, multiplyScalar(A[i][k], B[k][j]))
    return cij

def multiplyMatrix(A,B):
    m = len(A)
    p = len(B)
    C = [[0 for x in range(m)] for y in range(p)] 
    for i in range(m):
        for j in range(p):
            C[i][j] = getIndividualElement(A, B, i, j)
    
    return C


A = [['1' , '2', '3'],['4' , '5', '6'],['7' , '8', '9']]
B = A

# c12 = getIndividualElement(A,B, 0,1)
# print(c12)
C = multiplyMatrix(A,B)

print(C[2])


"""
A = [[1 , 2, 3],[4 , 5, 6],[7 , 8, 9]]
A = 
    [
        ['1' , '2', '3'],
        ['4' , '5', '6'],
        ['7' , '8', '9']
    ]
A = 
[['1' , '2', '3'],['4' , '5', '6'],['7' , '8', '9']]
"""
