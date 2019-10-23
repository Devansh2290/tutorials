import functools
import time
import math

def do_twise(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        return value
    return wrapper


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"Finished {func.__name__} in {runtime} sec")
        return value
    return wrapper_timer


def debug(func):

    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")

        value = func(*args, **kwargs)

        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug


math.factorial = debug(math.factorial)


@do_twise
def say_whee():
    print ("Whee!!!")


@do_twise
def greet(name):
    print(f"Hello {name}!!")


@do_twise
def return_greet(name):
    return f"Hello {name}"



@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i ** 2 for i in range(100000)])


@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"


def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))