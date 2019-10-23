from nose.tools import assert_equal

def find_last_toy_postion(n, d, t):
    position = d - 1
    for _ in range(1, t+1):
        if position == n: 
            position = 1
        else:
            position += 1
    return position


class FindLastToyPosition:
    def test(self, sol):
        assert_equal(sol(10, 5, 7), 1)
        assert_equal(sol(10, 5, 10), 4)
        assert_equal(sol(10, 5, 12), 6)
        print("ALL TEST CASE PASSED")

obj = FindLastToyPosition()
obj.test(find_last_toy_postion)

print (find_last_toy_postion(10000, 436, 1500000))