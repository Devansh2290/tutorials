def get_list1(num):
    result = []
    result.extend(range(num))

    return result

def get_list2(num):
    return [x for x in range(num)]



import time

s = time.time()
get_list1(100)
t1 = time.time() - s

s = time.time()
get_list1(100)
t2 = time.time() - s
print(f' t1 grt tr {t1 > t2}')