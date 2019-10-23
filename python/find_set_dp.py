def dp(arr, total, i, memo):
    key = f'{total}:{i}'

    if key in memo:
        return memo[key]

    if total == 0:
        return 1

    elif total < 0:
        return 0

    elif i < 0:
        return 0

    elif total < arr[i]:
        to_return = dp(arr, total, i-1, memo)
    else:
        to_return = dp(arr, total-arr[i], i-1, memo) + dp(arr, total, i-1, memo)

    memo[key] = to_return
    return to_return

def count_sets(arr, total):
    memo = {} # empty dict of hash table to store results.
    x = dp(arr, total, len(arr)-1, memo)
    return x

arr = [i ** 2 for i in range(1, 11)]
print (arr)
total = 100
print (count_sets(arr, total))