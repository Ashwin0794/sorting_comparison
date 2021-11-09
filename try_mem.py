#!/usr/bin/python3

#from numpy import random
#import time
#import matplotlib.pyplot as plt
#import numpy as np

from memory_profiler import profile,memory_usage

@profile(precision=4)
def my_func():
    a = [1]  * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

my_func()
#mem_use = memory_usage(my_func)
#print(mem_use)
#print(max(mem_use))
