a = list(range(0,100,2))
num_to_find = 116



def binary_search(a,num_to_find):
    not_found = True
    start = 0
    end = len(a)-1

    while not_found is not False:
        mid = (end - start // 2) + start
        if end - start < 0:
            return False
        if num_to_find == a[mid]:
            return mid
        elif num_to_find < a[mid]:
            end = mid - 1
        elif num_to_find > a[mid]:
            start = mid + 1


binary_search(a,num_to_find)