# Multithreading in python
# Python provides a built-in module called `threading` to work with threads.
# A thread is a separate flow of execution. This means that your program will have two things happening at once.


import time
import random
from concurrent.futures import ThreadPoolExecutor #BEST FOR MULTITHREADING


tables = ["orders", "products", "customers","Reviews","Cancels"]

def my_func(i):
    wait=3
    # wait = random.randint(1,3)
    time.sleep(wait)
    print(f"I am {i} .I took {wait} secs")
        
# for i in tables:
#     my_func(i)


with ThreadPoolExecutor(max_workers=len(tables)) as executor:
    #futures  = executor.map(my_func, tables)

    for i in tables:# it will start for first and then go to next without waiting for first to complete
        future = executor.submit(my_func, i)