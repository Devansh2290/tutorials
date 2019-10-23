def foo(x, y):
    global a
    a = 42
    x, y = y, x
    b = 33
    b = 17
    c = 100

    print(a, b, x, y)