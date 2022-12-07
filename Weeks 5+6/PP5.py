#Chapter 5 -Programming Project: Implement a function that takes in two sorted lists and merges them into one list, the new list must be sorted. 
#The function MUST run in O(m+n), where m is the length of list 1 and n the length of list 2.
#In other words, the function cannot do more than one pass on list 1 and list 2.


# c is smallest to largest
def merge(A,B): 
    x = len(A)
    y = len(B)
    C = []
    Billy = True
    i = 0
    j = 0

    while Billy is True:
    
        if i < x:

            if j < y:
            

                if A[i] == B[j]:
                    C.append(A[i])
                    C.append(B[j])
                    i = i + 1
                    j = j + 1
                    
                elif A[i] < B[j]:
                    C.append(A[i])
                    i = i + 1

                elif A[i] > B[j]:
                    C.append(B[j])
                    j = j + 1

            else:
                C.append(A[i])
                i = i + 1

        elif j < y:
            C.append(B[j])
            j = j + 1

        else: 
            Billy = False

    return C

 
    
if __name__ == '__main__':
    print(merge([1,3,8,9,10], [2,4,7,11,13]))
    print(merge([1,3,8,9,10,15,17,19], [2,4,7,11,13,18]))
# this works but its not singly linked
#that may be an easy change
