# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)
    return arr


from nose.tools import assert_equal

class TestQuickSort:
    def test(self, sol):
        arr = [10, 1, 20, 12]
        n = len(arr) - 1
        assert_equal(sol(arr, 0, n), [1, 10, 12, 20])
        arr = [10, 7, 8, 9, 1, 5] 
        n = len(arr) - 1
        assert_equal(sol(arr, 0, n), [1, 5, 7, 8, 9, 10])
        print("ALL TEST CASES PASSED!")

obj = TestQuickSort()
obj.test(quickSort)
