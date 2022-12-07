class StackPQ(SortedPQ, PriorityQueue):


    def __init__(self):
  
        self.counter = 0

        self.counter = 0

    # Stack ADT 

    def push(self, v):
        self.counter += 1 
        self.insert(Integer(-1*self.counter), v)

    def pop(self):
        self.counter -= 1
        return removeMin()
