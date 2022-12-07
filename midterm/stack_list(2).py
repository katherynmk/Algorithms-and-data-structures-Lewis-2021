class Empty(Exception):
    pass

class Stack:
    # Straight forward use of adapter patter, re-use Python List
    def __init__(self):
        self._data = [] # list as underlying storage

    def is_empty(self):
        """is stack empty"""
        return len(self._data) == 0

    def len(self):
        return len(self._data)

    def top(self):
        if self.is_empty():
            raise Empty()

        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty()

        return self._data.pop()

    def push(self, element):
        self._data.append(element)

    

if __name__ == '__main__':
    
    def is_valid_expr(exp):
        expr = list(exp)#turn string into list
        
        stack = [] #using a regular list but acting like its a stack

        for element in range (len(expr)):#go through the string 

            if expr[element]== "(":
                stack.append(element) #using append as push 
   
            if expr[element]==")": 
                try: stack.pop()
                except: return False
            
        if len(stack) == 0:
            return True
        if len(stack) != 0:
            return False


  
    