
def find_square_root(in_num):
    find_array = list(range(in_num))
    start = 0
    end = in_num
    for i in range(in_num):
        mid_point = start + ((end - start) // 2)
        if mid_point**2 == in_num:
            return mid_point

        elif mid_point**2 < in_num:
            start = mid_point + 1


        elif mid_point**2 > in_num:
            end = mid_point - 1

        else:
            return mid_point

print(find_square_root(12))