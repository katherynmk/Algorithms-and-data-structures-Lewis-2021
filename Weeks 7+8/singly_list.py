class ListEmpty(Exception):
    pass

class SinglyList:
    class _Node:
        def __init__(self, e, next):
            self._element = e
            self._next = next

    def __init__(self):
        self._head = self._tail = None
        self._size = 0

        self._current = None #needed to provide iterator suppor

    def is_empty(self):
        return self._size == 0

    def add_head(self, element):
        if self.is_empty():
            new_node = self._Node(element, None)
            self._head = self._tail = self._current = new_node
        else:
            new_node = self._Node(element, self._head)
            self._head = new_node

        self._size += 1

    def add_tail(self, element):
        if self.is_empty():
            self.add_head(element)
        else:
            new_node = self._Node(element, None)
            self._tail._next = new_node
            self._tail = new_node
            self._size += 1

    def delete_tail(self):
        if self.is_empty():
            raise ListEmpty()

        p = self._head
        while p._next is not self._tail:
            p = p._next

        self._tail = p
        self._tail._next = None

        self._size -= 1

    def delete_head(self):
        if self.is_empty():
            raise ListEmpty()

        p = self._head
        self._head = p._next
        p._next = None

        self._size -= 1

    def __len__(self):
        return self._size


    def __iter__(self):
        """needed to provide iterator support"""
        return self

    def __next__(self):
        """needed to provide iterator support,
        there are several other cases that needs
        to be handled when delete_head, delete_tail
        are interleaved with iterator, one classical
        way of overcomming this is to lock modification
        while iterator is in progress (e.g.: raise
        concurrent modification exception as in java).
        Handling these cases is beyond scope of this
        simple implementation"""  

        if self.is_empty():
            raise StopIteration()

        if self._current == None:
            # as a rough solution, start iterator over
            self._current = self._head
            raise StopIteration()

        e = self._current._element
        self._current = self._current._next
        return e

    def find_3rd_to_last(self):
        self._current = self._head
        z = self._head
 
        while z != None:
            x = self._current._element
            z = self._current._next._next._next
            self._current = self._current._next
        return x

    def __reverse__(self,pnode,cnode):
        self._current = cnode
        if self._current == None:
            self._head = pnode
            self._current = self._head
            return True
        else:
            x = self._current._next
            if self._current == self._head:
                self._current._next = None
            else:
                self._current._next = pnode
            return __reverse__(self,cnode,x)

    def reverse(self):
        return __reverse__(self,self._head,self._head)

    def compare_list(self,other):
        a = self._head
        b = other._head 
        while True:
            if a and b and a._element == b._element: 
                a = a._next
                b = b._next
            else: 
                break
        if not a and not b:
            return True

        else:
            return False


if __name__ == '__main__':
    l = SinglyList()
    
    for i in range(22):#here who show add tail
        l.add_tail(i)

    def find_median(self):
        #assume we have a sorted list (list in ascending order) 
        head, num, mid  = self._head, self._head, self._head #start by looking at the beginning 

        while num  and num._next : #while the current number and the the next number  exist 
            num = num._next._next #look ahead in the list, use this later to check if we need to divide the middle two numbers or return the regular middle number 
            mid = head #change your variable 
            head = head._next #set to new middle 
        if num: #if there is an odd amount of element 
            return head._element 
        else: #if there is an even
            return (head._element + mid._element)/2

print(find_median(l))
