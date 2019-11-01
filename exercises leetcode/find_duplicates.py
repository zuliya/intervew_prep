def printRepeating(arr):
    print("The repeating elements are: ")
    size = len(arr)
    for i in range(0, size):
        print(abs(arr[i]))
        # print(arr[abs(arr[i])])
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            print("Duplicate")
            # print(abs(arr[i]), end=" ")

print(printRepeating([12313,1,2,2,3,4,3,4,5,6,7,8,8,1]))