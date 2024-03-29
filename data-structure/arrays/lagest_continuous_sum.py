from nose.tools import assert_equal

def largest_continuous_sum(arr):
    if len(arr) == 0:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum


class LargestContinuousSum:
    def test(self, sol):
        assert_equal(sol([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
        assert_equal(sol([1, 2, -1, 3, 4, -1]), 9)
        assert_equal(sol([1,-1]), 1)
        assert_equal(sol([]), 0)
        assert_equal(sol([1, -10, -11, -15]), 1)
        print('ALL TEST CASES PASSED')

obj = LargestContinuousSum()
obj.test(largest_continuous_sum)