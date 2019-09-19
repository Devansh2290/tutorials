class Example:
    @classmethod
    def classmenthod1(cls):
        return f'class methid , {cls!r}'

    def insmenthod1(self):
        return f'instance methid , {self!r}'

print (Example.classmenthod1())
obj = Example()
print (Example.insmenthod1(obj))