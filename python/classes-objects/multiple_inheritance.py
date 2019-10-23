class A:
    def func(self):
        print("Class A's func()")

    pass


class B(A):
    # def func(self):
    #     print("Class B's func()")
    pass


class C(A):
    # def func(self):
    #     print("Class C's func()")
    pass

class D(B, C):
    # def func(self):
    #     print("Class D's func()")
    pass

c_obj = D()

c_obj.func()