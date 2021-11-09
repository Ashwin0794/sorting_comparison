#!/usr/bin/python3

from helper import timer_decorator
from numpy import random
import matplotlib.pyplot as plt 
import numpy as np
import csv

#profiling runtime and memory usage with increasing dataset sizes for Bubble sort 
@timer_decorator
def bubbleSort( mylist ):
    length = len(mylist) - 1
    for i in range(length, 0, -1):
        for j in range(0, i):
            if (mylist[j] > mylist[j + 1]):
                temp = mylist[j]
                mylist[j] = mylist[j + 1]
                mylist[j + 1] = temp
size = 200
time = []
mem = []
dataset_size = []
while size <= 6400:
    time_secs = 0.0000
    mem_usage = 0
    dataset_size.append(size)
    for j in range(0,5):
        s = random.uniform(0,1,size)
        result = bubbleSort(s)
        time_secs = time_secs + result['elapsedTime']
        mem_usage = mem_usage + result['mem_consumed'] 
        #print(f'memory consumed for size {size} is {result["mem_consumed"]}')
    avg_time_secs = time_secs/5.0000
    avg_mem_usage = mem_usage/5
    time.append(avg_time_secs)
    mem.append(avg_mem_usage) 
    print(f'for size {size} time req is {avg_time_secs:.4f}')
    #break
    size = size * 2

time = [ '%.4f' % elem for elem in time]
print(f'time values are {time}')

#with open('runtime.csv', 'w') as csvfile: 
#    write = csv.writer(csvfile) 
#    write.writerow(time) 
    
xpoints = np.array(dataset_size)
y1points = np.array(time)
y2points = np.array(mem)

figure, axis = plt.subplots(2,1)

axis[0].plot(xpoints, y1points)
axis[0].set_title("dataset sizes vs runtime")

axis[1].plot(xpoints, y2points)
axis[1].set_title("dataset sizes vs memory usage")

plt.savefig('Bubble_sort_graphs.png')


#plt1.plot(xpoints, y1points)
#plt1.savefig('b_sort_1.png')
#plt1.title('Bubble sort - Time Complexity profiling(uniform dist)')
#plt1.xlabel('dataset sizes')
#plt1.ylabel('runtime in secs')

