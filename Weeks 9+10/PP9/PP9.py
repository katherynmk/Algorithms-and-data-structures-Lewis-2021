import time
import random 
import matplotlib.pyplot as plt
#On^2 time


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
        listy.sort()
        time2 = time.time()
        averagetime = averagetime + (time2 - time1)
        averagetimeperlist = averagetime/10
        xaxis.append(averagetimeperlist)
        yaxis.append(n)

    print("List ", a, " time is ", averagetimeperlist, " the size is: ", n)
    sumtime = sumtime + averagetimeperlist

    x = x + 100000
    n = n + 50000
    c = c + 1
    a = a + 1

finaltime = sumtime/10
print("The average of all of the list times is ", finaltime)

plt.title('On^2')
plt.plot(yaxis,xaxis)
plt.ylabel('Running Time')
plt.xlabel('Size')
plt.show()
