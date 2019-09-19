from nose.tools import assert_equal


def pair_sum(arr, value):
    if len(arr) < 2:
        return

    # set for tracking
    seen = set()
    output = set()

    for num in arr:
        target = value - num
        if num not in seen:
            seen.add(target)
        else:
            output.add((target, num))
    return len(output)

def pair_sum_generator(arr, value):
    if len(arr) < 2:
        return
    seen = set()

    for item in arr:
        if item in seen:
            yield value - item, item
        else:
            seen.add(value - item)


class TestPairSum:
    def test(self, sol):
        assert_equal(sol([1, 9, 2, 8, 3, 7, 4, 5, 6, 5, 13, 14, 11, 13, -1], 10), 6)
        assert_equal(sol([1, 3, 2, 1], 3), 1)
        assert_equal(sol([1, 3, 2, 2], 4), 2)
        print('ALL TEST CASES PASSED')

obj = TestPairSum()
obj.test(pair_sum)