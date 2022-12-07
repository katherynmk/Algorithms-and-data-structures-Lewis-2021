#Chapter 11 - Programming Project: Implement folloring binary-search tree functions:
#- search(key)
#- insert(key)
#- print_in_order(): prints the keys in the binary tree in ascending order.
import queue

class LinkedBinaryTree:
    class _Node:
        __slots__ = '_element', '_left', '_right'

        def __init__(self, element, parent = None, left = None, right = None):
            self._element = element
            self._left = left
            self._right = right

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def height(self):
        return self._height(self._root)

    def _height(self, p):
        if not p:
            return 0
        return 1 + max(self._height(p._left), self._height(p._right))


    def in_order(self):
        for e in self._in_order(self._root):
            yield e

    def _in_order(self, p):
        if p is not None:
            for other in self._in_order(p._left):
                yield other

            yield p._element
            for other in self._in_order(p._right):
                yield other


    def pre_order(self):
        for e in self._pre_order(self._root):
            yield e

    def _pre_order(self, p):
        if p:
            yield p._element
            for other in self._pre_order(p._left):
                yield other

            for other in self._pre_order(p._right):
                yield other

    def post_order(self):
        for e in self._post_order(self._root):
            yield e

    def _post_order(self, p):
        if p:
            for other in self._post_order(p._left):
                yield other

            for other in self._post_order(p._right):
                yield other

            yield p._element

    def breadth_first(self):
        q = queue.Queue()
        q.put(self._root)
        rhile not q.empty():
            p = q.get()
            print(p._element)
            if p._left:
                q.put(p._left)
            if p._right:
                q.put(p._right)

    def bst_insert(self, key):

        if self is None: 
                return key
        else: 
                if self._element == key: 
                        return self 
                elif self._element < key: 
                     self._right = bst_insert(self._right, key) 
                else: 
                     self._left = bst_insert(self._left, key) 
        return self 

    def bst_search(self, key):
        
        if self is None or self._element == key: 
                return self 

        if self._element < key: 
                return bst_search(self._right,key) 

        return bst_search(self._left, key) 


    def print_in_order (self): 
            if self: 
                print_in_order(self._left) 
                print(self._element) 
                print_in_order(self._right) 
            
