
def multiplyScalar(a , b):
    a = a.strip()
    b = b.strip()
    return '((' +  a + ')*(' + b + '))'

def divideScalar(a , b):
    a = a.strip()
    b = b.strip()
    return '((' +  a + ')/(' + b + '))'


def addScalar(a , b):
    a = a.strip()
    b = b.strip()
    
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




A = [['1' , '2', '3'],['4' , '5', '6'],['7' , '8', '9']]
B = A

c12 = getIndividualElement(A,B, 0,0)
print(c12)


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
