from nose.tools import assert_equal

# Given an array of positive and negative numbers,
# find if there is a subarray (of size at-least one) 
# with 0 sum.

def isSubArrayExistsWithZero(arr, n):
    curr_sum = 0
    seen_map = set()

    for i in range(n):
        curr_sum += arr[i]

        if curr_sum == 0 or curr_sum in seen_map:
            return True
        seen_map.add(curr_sum)
    return False


def maxLengthOfSubArray(arr, n):
    curr_sum = 0
    max_length = 0
    sum_map = {}

    for i in range(n):
        curr_sum += arr[i]
        if curr_sum == 0:
            max_length = 1
        if curr_sum in sum_map:
            max_length = max(max_length, i - sum_map[curr_sum])
        else:
            sum_map[curr_sum] = i
    return max_length


class TestSubArrayExists:
    def test(self, sol):
        assert_equal(sol([23, 6, 2, -4, -4, 5, -5, 15], 8), True)
        assert_equal(sol([23, 6, 2], 3), False)
        assert_equal(sol([0], 1), True)
        assert_equal(sol([], 0), False)
        print("ALL TEST CASE PASSED FOR {}".format(self.__class__.__name__))


class TestMaxLength:
    def test(self, sol):
        assert_equal(sol([23, 6, 2, -4, -4, 5, -5, 15], 8), 6)
        assert_equal(sol([23, 6, 2], 3), 0)
        assert_equal(sol([0], 1), 1)
        assert_equal(sol([], 0), 0)
        print("ALL TEST CASE PASSED FOR {}".format(self.__class__.__name__))


obj = TestSubArrayExists()
obj.test(isSubArrayExistsWithZero)

obj = TestMaxLength()
obj.test(maxLengthOfSubArray)


def generator_m(x):
    for i in range(x):
        yield i * 5