#Chapter 12 - Programming Project: write a function that takes in two lists (A and B) as parameters, 
# and an integer (sum). The function returns True if there are two numbers:
#  a in A, and b in B, where a + b = sum. The function must run in O(nlogn).

#Note: this is based of C12.45 on page 578

#malik tifah -- did not participate in group

#these are just ideas, continue down to commented section that says my final submission
def inversions(l, n):
    #give your code the length of the list
    count = 0 
    for i in range(n):
        for x in range(i + 1, n):
            if l[i] > l[x]:
                count = count + 1
    return count 

l = [8, 4, 2, 1]
n = len(l)
#on^2 (time)
#On(space)

import time
import random
import matplotlib.pyplot as plt
class Heap:
    def __init__(self):
        self._heap = []

    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def _last_idx(self):
        return len(self._heap) - 1

    def _left(self, i):
        return i * 2 + 1

    def _right(self, i):
        return i * 2 + 2

    def _parent(self, i):
        return (i - 1) // 2

    def _has_left(self, i):
        return self._left(i) < len(self._heap)

    def _has_right(self, i):
        return self._right(i) < len(self._heap)

    def empty(self):
        count = 0
        return len(self._heap) == 0

    def add(self, key):
        self._heap.append(key)

        j = self._last_idx()

        while j > 0 and self._heap[j] < self._heap[self._parent(j)]:
            count = count + 1
            self._swap(j, self._parent(j))
            j = self._parent(j)

        return count


    def remove_min(self):
        if self.empty():
            raise Exception()

        self._swap(0, self._last_idx())
        result = self._heap[-1]
        self._heap.pop()

        # push new element down the heap
        j = 0
        while True:
            min = j
            if self._has_left(j) and self._heap[self._left(j)] < self._heap[min]:
                min = self._left(j)

            if self._has_right(j) and self._heap[self._right(j)] < self._heap[min]:
                min = self._right(j)

            if min == j:
                #found right location for min, break
                break

            self._swap(j, min)
            j = min

        return result


def heap_sort(l):
    count = 0
    heap = Heap()
    #phase I: nlogn
    for e in l:
        heap.add(e)
        if heap.add(e) > 0:
            count = count + 1

    sorted_list = []
    #phase II: nlogn
    while not heap.empty():
        
        sorted_list.append(heap.remove_min())

    return count

#print(heap_sort(l))

##################################################################################
#this was done by Max Lewis, from our in class groups
#this is the final code im going with
#all of the others are ideas our groups had 

def __inversions(l): 
    p1 = 0
    p2 = len(l) - 1
    inversions = 0
    while p1 != p2:
        if l[p1] > l[p2]:
                inversions += 1
        if p1 + 1 == p2:
            p1 += 1
            p2 = len(l) - 1
        else:
            p2 -= 1
    return inversions

if __name__ == '__main__':
    
    print(__inversions(l))

