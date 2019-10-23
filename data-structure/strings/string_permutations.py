def permutations(arr, low, high):
    print(low, high)
    if low == high:
        print (''.join(arr))
    else:
        for i in range(low, high):
            arr[low], arr[i] = arr[i], arr[low]
            permutations(arr, low + 1, high)
            arr[low], arr[i] = arr[i], arr[low]

string = "ABCDE"
n = len(string) 
arr = list(string) 

permutations(arr, 0, n)