# Decoratorsa are the callable python objects which is use to modify 
# the behaviour of functions or class wihout modify it parmanently.
# Two types of decoratore we can define in python.
# 1. class based decorators
# 2. funcation based decorators


# 1. class based decorator: when we define a class based decorator we need 
# to define a __call__ method


class MyDecoratore:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        # We can add some code
        # before function call
        print ("before function call")
        self.func() 
        print ("after function call")
        # We can also add some code 
        # after function call. 


@MyDecoratore
def func():
    print ("I am wapped function.")


func()


def f(x):
    def g(y):
        return x * y + 3
    return g


nf1 = f(10)
print (nf1(2))

