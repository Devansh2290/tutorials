# Find sets of numbers that add up to numeric value



def rec(arr, total, index):
    if total == 0:
        return 1

    elif total < 0:
        return 0

    elif index < 0:
        return 0

    elif total < arr[index]:
        return rec(arr, total, index - 1)

    else:
        return rec(arr, total - arr[index], index - 1) + rec(arr, total, index-1)

def count_sets(arr, total):
    return rec(
        arr=arr,
        total=total,
        index=len(arr) - 1
    )



arr = [i ** 2 for i in range(1, 11)]
total = 100
print (count_sets(arr, total))

