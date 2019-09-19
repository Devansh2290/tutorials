from nose.tools import assert_equal
from collections import defaultdict


def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
    return arr1[-1]


def finder2(arr1, arr2):
    d = defaultdict(int)

    for num in arr2:
        d[num] += 1
    
    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1


def finder3(arr1, arr2):
    result = 0

    # perform an XOR between the numbers in the arrays.
    for num in arr1 + arr2:
        result ^= num
    return result

       
class FindMissingElement:
    def test(self, sol):
        assert_equal(sol([1, 2, 3, 4, 5, 6, 7], [3, 5, 7, 1, 2, 6]), 4)
        assert_equal(sol([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]), 6)
        assert_equal(sol([5, 5, 7, 7], [5, 5, 7]), 7)
        print('ALL TEST CASES PASSED')

obj = FindMissingElement()
obj.test(finder)
obj.test(finder2)
obj.test(finder3)
