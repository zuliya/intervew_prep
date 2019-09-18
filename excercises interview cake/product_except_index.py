arr = [1, 7, 3, 4]

def get_all_products_except_at_index(arr):
    if len(arr) < 2:
        raise IndexError('Getting the product of numbers at other '
                         'indices requires at least 2 numbers')

    total_product = [1] * len(arr)

    # Calculate beginning product
    curr_product = 1
    for i in range(len(arr)-1):
        curr_product = arr[i] * curr_product
        total_product[i+1] = curr_product
    print(total_product)

    # Calculate end product
    curr_product = 1
    for i in range(0, len(arr)-1):
        curr_product = arr[len(arr)-i-1] * curr_product
        total_product[len(arr)-2-i] *= curr_product

    return total_product


print(get_all_products_except_at_index(arr))


# Can do better by just having one array