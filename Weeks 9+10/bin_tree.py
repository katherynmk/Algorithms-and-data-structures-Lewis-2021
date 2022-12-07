class BinaryTree:

    class _Node:
        def __init__(self, e, left = None, right = None):
            self._left = left
            self._right = right
            self._element = e


    def __init__(self):
        self._root = None
        self._size = 0

    def is_empty(self):
        return self._root == None

    def add_root(self, e):
        if self._root:
            return None

        self._root = self._Node(e)
        return self._root

    def add_left(self, e, p):
        p._left = self._Node(e)
        return p._left

    def add_right(self, e, p):
        p._right = self._Node(e)

        return p._right

    def _height(self, v):
        if not v:
            return -1

        x = self._height(v._left)
        y = self._height(v._right)
        return 1 + max(x, y)


    def height(self):
        return self._height(self._root)

    def _inOrder(self, p):
        if p:
            self._inOrder(p._left)
            print(p._elemet)
            self._inOrder(p._right)

    def inOrder(self):
        self._inOrder(self._root)

    def _preOrder(self, p):
        if p:
            print(p._elemet)
            self._preOrder(p._left)
            self._preOrder(p._right)

    def preOrder(self):
        self._preOrder(self._root)


    def _postOrder(self, p):
        if p:
            self._postOrder(p._left)
            self._postOrder(p._right)
            print(p._elemet)

    def postOrder(self):
        self._postOrder(self._root)
    
 
    def countK(self, num):
        current = self._root  
        stack = [] 
        count = 0 

        while True: 
 
            if current != None: 
   
                stack.append(current) 
            
                current = current._left  

            elif(stack): 
                current = stack.pop() 

                if current._element == num:
                    count = count + 1
      
                current = current._right  

            else: 
                break

        return count

    def _equal(self, root1, root2):

        if root1 == None and root2 == None: 
            return True 

        if root1 != None and root2 != None: 
            return ((root1._element == root2._element),  self._equal(root1._left, root2._left), self._equal(root1._right, root2._right)) 
 
        return False

    def equal(self, other):
        return self._equal(self._root, other._root)


        
