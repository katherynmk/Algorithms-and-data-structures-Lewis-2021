#Chapter 6 -Programming Project: using a stack, implement a function that takes in an arithmetic expression, and evaluates it, 
#supported operations are + and -, which have same precedence. This is a simplified version of the eval_expr function we built in lecture.
#Note: one way to do it is to scan the entire expr pushing numbers onto val-stack and operations on op-stack until tokens in expr are done. 
#Then, use a loop to pop two numbers from val-stack and one operation from op-stack, evaluate, and push results back to val-stack, until op-stack is empty.


def reverse_list(listy):#here is the backwards youre talking about
    #so this is the function for that
 
    stack = [] 
 

    for a in range(len(listy)): 

        stack.append(listy[a])
 

    for i in range(len(listy)):
        listy[i] = stack.pop()
 
    return listy



def simple(ops, test_exp):
    val_stack = [] #these are stacks
    op_stack = []

    tokens = test_exp.split()
    val_stack = reverse_list(val_stack)#and here is where we use that function at the beginning of everything
    op_stack = reverse_list(op_stack)

    for i in range(len(tokens)):
        if i %2 == 0:
            val_stack.append(int(tokens[i]))#yeah I just didnt personally try your code so I dont know if the errors I was 
            #getting would still be there 
            #so My code was very short
            #and then I was so happy i finished it
            #then i got the subtraction problem and doubled the length
        else:
            op_stack.append(tokens[i])
            #if someone else wants to help me code the version you did in class?
            #someone in the group here?



    while len(val_stack) >= 2 and len(op_stack) > 1:
        x = val_stack.pop()
        y = val_stack.pop()
        z = op_stack.pop()
        abc = op_stack.pop()

        if z == "+" and abc == "+":
            val_stack.append(x + y)
            op_stack.append("+")

        if z == "-" and abc == "-":
            val_stack.append(-x - y)
            op_stack.append("+")
        
        if z == "+" and abc == "-":
            val_stack.append(x - y)
            op_stack.append("+")

        if z == "-" and abc == "+":
            val_stack.append(-x + y)
            op_stack.append("+") #i kind of used opperator precedence to get correct answer
            #because i was getting like 50-100+50 would give me the wrong asnwer
            #so i had to put in these statements

    x = val_stack.pop()
    y = val_stack.pop()
    z = op_stack.pop() 

    if z == "+":
        return (x+y)
    if z == "-":
        return(y-x)


#burhan can you help me out
if __name__ == "__main__":
    ops = '+-'
    test_exp = '100 - 200'
    print(simple(ops,test_exp))