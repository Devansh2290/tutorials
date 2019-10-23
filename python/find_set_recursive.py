# Python program to print all subsets with given sum 


def find_subset_rec(arr, total, current_subset, i):
    if total == 0:
        for value in current_subset : 
            print(value, end=" ") 
        print() 
        return

    elif total < 0:
        return

    # If no remaining elements, 
    elif i < 0:
        return
    
    # We consider two cases for every element. 
    # a) We do not include last element. 
    # b) We include last element in current subset. 
    find_subset_rec(arr, total, current_subset, i - 1)
    new_current_subset = [] + current_subset
    new_current_subset.append(arr[i - 1])
    find_subset_rec(arr, total - arr[i - 1], new_current_subset, i - 1)


def print_all_subsets(arr, total):
    current_subset = []
    find_subset_rec(
        arr=arr,
        total=total,
        current_subset=current_subset,
        i=len(arr) - 1
    )

def build_arr(num, e):
    base_value = int(round(num ** (float(1)/ e)))
    print (base_value)
    arr = [i ** e for i in range(1, int(base_value) + 1 )]
    print (arr)
    print_all_subsets(arr, num)


build_arr(1064,3)