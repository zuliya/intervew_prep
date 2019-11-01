# Space to be O(1)
a = [-12,0,0,0,1,2,3,4,5,5,5,6]

def remove_duplicates(nums):
    i = 0
    for j in range(1,len(nums)):
        if nums[i] != nums[j]:
            nums[i] = nums[j]
            i +=1
    return i
print(remove_duplicates(a))