# Implement an algorithm to determine if a string has all unique characters
# What if you can not use additional data structures?

#  Hash map
#  if the numbers are all characters could just have a 32 thing

def check_if_unique(arr):
    unique_dict = {}
    for i in arr:
        if i in unique_dict.keys():
            return False
        else:
            unique_dict[i] = 1
    return True


def reverse_string(input_str):
    temp = input_str
    for i in range(len(input_str)):
        input_str = input_str + input_str[len(temp)-i-1]
    return input_str[len(temp):]

# print(reverse_string('absc'))

def remove_dub_string(in_str):
    for i in in_str:
        return False


