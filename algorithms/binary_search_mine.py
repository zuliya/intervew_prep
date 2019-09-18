def iterative_binary_search(arr, num):
    start_i = 0
    end_i = len(arr)-1

    while start_i <= end_i:

        mid_index = start_i+(end_i-start_i)//2

        if arr[mid_index] == num:
            return mid_index

        elif arr[mid_index]<num:
            start_i = mid_index + 1

        elif arr[mid_index]>num:
            end_i = mid_index - 1

    return mid_index


a = [0,1,2,3,4,5,6,8,9,10]

print(iterative_binary_search(a,0))

print(iterative_binary_search(a,9))

print(iterative_binary_search(a,7))

