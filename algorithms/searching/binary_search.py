import math

from nose.tools import assert_equal

def binary_search(arr, n, value) -> int:
    high = n - 1
    low = 0
    while low <= high:
        mid = int((low + high) / 2)
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_leftmost_element(arr, n , value):
    low, high, result = 0, n-1, -1
    while low <= high:
        mid = int((low + high) / 2)
        if arr[mid] == value:
            result = mid
            high = mid - 1
        elif arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return result


def binary_search_alternative(arr, n, value):
    left = 0
    right = n - 1

    while left != right:
        middle = math.ceil((left + right) / 2)

        if arr[left] < value:
            left = middle
        else:
            right = middle - 1

    if arr[left] == value:
        return left
    return

def binary_search_leftmost(arr, n, value):
    left = 0
    right = n - 1
    result = -1
    while left <= right:
        middle = int((left + right) / 2)
        if arr[middle] == value:
            result = middle
            right = middle - 1
        if arr[middle] < value:
            left = middle + 1
        else:
            right = middle

    return result


# class BinarySearch:
#     def test(self, sol):
#         assert_equal(sol([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 8), 7)
#         assert_equal(sol([2, 3, 11, 15, 26, 37, 48, 59, 60], 9, 65), None)
#         print('ALL TEST CASES PASSED')

# obj = BinarySearch()
# obj.test(binary_search)
# obj.test(binary_search_alternative)

arr = [1,1,1,1,2,2,2,2,3,3,3,4,5]
n = len(arr)
print (binary_search_leftmost_element(arr, n, 2))


# here the complexity of binary search is O(log n)
# binary search can be apply if array/elements are sorted.
# 