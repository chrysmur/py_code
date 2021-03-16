#!/usr/bin/python3
import  _thread as thread 
import time

def counter(id, count):
    for i in range(count):
        print(f'[{id}] --> {i}\n')
        time.sleep(1)

# for i in range(5):
#     counter(i, 5)

for i in range(5):
    print(i)
    thread.start_new_thread(counter, (i, 5))
