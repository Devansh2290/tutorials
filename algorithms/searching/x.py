def get_pair_of_sum(arr, total):
    seen = set()
    for i in arr:
        val = total - i
        if i in seen:
            print (i, val)
            seen.remove(i)
        else:
            seen.add(val)


arr = [5, 1, 2, 3, 5, 6, 4, 5, 5, 5]
{5, 9, 8, 7 }

get_pair_of_sum(arr, 10)