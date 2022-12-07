#C3.35
#assume all  the lists are sorted

def check(A,B,C,n,m,k): 

    if A[n] == B[m] and B[m] == C[k]:
        return "COMMON ELEMENT"

    elif A[n] == B[m] and B[m] < C[k]:
        if n == len(A)-1 or m == len(B)-1:
            return "No common element"
        return check(A,B,C, n+1, m+1, k)

    elif A[n] == B[m] and B[m] > C[k]:
        if k == len(C)-1:
            return "No common element"
        return check(A,B,C,n,m, k+1)

    elif A[n] < B[m] and B[m] == C[k]:
        if n == len(A)-1:
            return "No common element"
        return check(A,B,C, n+1, m, k)

    elif A[n] < B[m] and B[m] < C[k]:
        if n == len(A)-1 or m == len(B)-1:
            return "No common element"
        
        return check(A,B,C, n+1, m+1, k)

    elif A[n] < B[m] and B[m] > C[k]:
        if n == len(A)-1 or k == len(C)-1:
            return "No common element"
        
        return check(A,B,C, n+1, m, k+1)

    elif A[n] > B[m] and B[m] == C[k]:
        if m == len(B)-1 or k == len(C)-1:
            return "No common element"
        return check(A,B,C, n, m+1, k+1)

    elif A[n] > B[m] and B[m] < C[k] and A[n] > C[k]:
        if m == len(B)-1 or k == len(C)-1:
            return "No common element"
        return check(A,B,C, n, m+1, k+1)
    
    elif A[n] > B[m] and B[m] < C[k] and A[n] < C[k]:
        if m == len(B)-1 or n == len(A)-1:
            return "No common element"
        return check(A,B,C, n+1, m+1, k)


    elif A[n] > B[m] and B[m] < C[k] and A[n] == C[k]:
        if m == len(B)-1:
            return "No common element"
        return check(A,B,C, n, m+1, k)
 

    elif A[n] > B[m] and B[m] > C[k]:
        if m == len(B)-1 or k == len(C)-1:
            return "No common element"
        
        return check(A,B,C, n, m+1, k+1)
    

    
if __name__ == '__main__':
    print(check([1,3,8,9,10,15], [2,4,7,11,13], [5,6,12,14],0,0,0))
    print(check([1,3,8,9,11,15], [2,4,7,11,13], [5,6,11,14],0,0,0))






