class Fibonacci:
    def __init__(self, i1=0, i2=1):
        self.memo = {0: i1, 1: i2}

    def __call__(self, n):
        if n not in self.memo:
            self.memo[n] = self.__call__(n - 1) + self.__call__(n - 2)
        return self.memo[n]


# fib = Fibonacci()
# lucas = Fibonacci(2, 1)
# for i in range(1, 16):
#     print(fib(i), lucas(i))



def sum_of_number(n):
    if n <= 1:
        return n
    return n + sum_of_number(n-1)

print(sum_of_number(10000))