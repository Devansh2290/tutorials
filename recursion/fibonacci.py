def fib(num):
    if num <= 1:
        return num
    return fib(num-1) + fib(num-2)


def print_fibonacci(num):
    print (fib(num))


import time 
s = time.time()
print_fibonacci(1500)
print(f'Time taken: {time.time() - s}')