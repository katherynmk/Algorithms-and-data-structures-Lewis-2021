def merge(A,B): 
    x = len(A)
    y = len(B)
    C = []
    n = A.pop(0)
    m = B.pop(0)
    i = 0
 
    while i <= (x+y-1):
    
        if A == []:
            C.append(m)
            if B != []:
                m = B.pop(0)
            i = i + 1
            #print(C)
 
        elif B == []:
            C.append(n)
            if A != []:
                n = A.pop(0)
            i = i + 1
            #print(C)
 
        elif n == m:
            C.append(n)
            C.append(m)
            i = i + 1
            i = i + 1
 
            if B != []:
                m = B.pop(0)
            if A != []:
                n = A.pop(0)
            #print(C)
 
 
        elif n < m:
            C.append(n)
            i = i + 1
            if A != []:
                n = A.pop(0)
            #print(C)
 
        elif n > m:
            C.append(m)
            i = i + 1
            if B != []:
                m = B.pop(0)
            #print(C)
 
    return C
 
    
if __name__ == '__main__':
    #print(merge([1,3,8,9,10], [2,4,7,11,13]))
    print(merge([1,3,8,9,10,15,17,19], [2,4,7,11,13,18]))
