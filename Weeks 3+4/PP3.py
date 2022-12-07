#Chapter 3 -Programming Project [P-3.57]: Perform experimental analysis to test the hypothesis that Python’s sortedmethod runs in O(nlog n) time on average.
# 10 different lists
# run 50 times to get the average of each data point on x-axis

import time
import random 


sumtime = 0 
x = 500
n = 500
c = 0
a = 1
averagetime = 0

while c < 10:

    listy = list(random.sample(range(0,x),n))


    for i in range(50):

        time1 = time.time()
        sorted(listy)
        time2 = time.time()
        averagetime = averagetime + (time2 - time1)
        averagetimeperlist = averagetime/10

    print("List ", a, " time is ", averagetimeperlist)
    sumtime = sumtime + averagetimeperlist

    x = x + 100000
    n = n + 50000
    c = c + 1
    a = a + 1

finaltime = sumtime/10
print("The average of all of the list times is ", finaltime)



