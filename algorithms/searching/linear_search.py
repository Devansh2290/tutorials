from nose.tools import assert_equal

def linear_search(arr, value):
    for index, item  in enumerate(arr):
        if item == value:
            return index



class LinearSearch:
    def test(self, sol):
        assert_equal(sol([2,3,5,1,5,7,3,1], 5), 2)


obj = LinearSearch()
obj.test(linear_search)


# here the complexity of the liner search O(n)