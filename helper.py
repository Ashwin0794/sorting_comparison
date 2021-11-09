#!/usr/bin/python3

from numpy import random
import time
import matplotlib.pyplot as plt
import numpy as np
import os
import psutil

def get_process_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss

def timer_decorator(func):
    def timer(*args, **kwargs):
        mem_before = get_process_memory()
        t1 = time.perf_counter()
        
        func(*args, **kwargs)
        
        t2 = time.perf_counter()
        mem_after = get_process_memory()
        
        elapsedTime = t2 - t1
        mem_consumed = mem_after - mem_before
        
        profiler = {}
        profiler['elapsedTime'] = elapsedTime
        profiler['mem_consumed'] = mem_consumed
        
        return profiler
    return timer

