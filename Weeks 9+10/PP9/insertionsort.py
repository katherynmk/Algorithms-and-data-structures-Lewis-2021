# Python program for implementation of Insertion Sort
import time
import random 

import matplotlib.pyplot as plt

# Function to do insertion sort
def insertionSort(l):
  # This code is contributed by Mohit Kumra
    # Traverse through 1 to len(l)
    for i in range(1, len(l)):
  
        key = l[i]
  
        # Move elements of l[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < l[j] :
                l[j+1] = l[j]
                j -= 1
        l[j+1] = key
  
sumtime = 0 
x = 500
n = 500
c = 0
a = 1
averagetime = 0
xaxis = []
yaxis = []

while c < 10:
    
    listy = list(random.sample(range(0,x),n))
    for i in range(50):

        time1 = time.time()
        insertionSort(listy)
        time2 = time.time()
        averagetime = averagetime + (time2 - time1)
        averagetimeperlist = averagetime/10
        xaxis.append(averagetimeperlist)
        yaxis.append(n)
    print("List ", a, " time is ", averagetimeperlist, " the size is: ", n)
    sumtime = sumtime + averagetimeperlist

    x = x + 100000
    n = n + 5000
    c = c + 1
    a = a + 1

finaltime = sumtime/10
print("The average of all of the list times is ", finaltime)

plt.title('Insertion')
plt.plot(yaxis,xaxis)
plt.ylabel('Running Time')
plt.xlabel('Size')
plt.show()

