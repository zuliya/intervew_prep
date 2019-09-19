
def find_rotation_point(words):
    first_word = words[0]
    floor_index = 0
    ceiling_index = len(words) - 1

    while floor_index < ceiling_index:
        # Guess a point halfway between floor and ceiling
        guess_index = floor_index + ((ceiling_index - floor_index) // 2)

        # If guess comes after first word or is the first word
        if words[guess_index] >= first_word:
            # Go right
            floor_index = guess_index
        else:
            # Go left
            ceiling_index = guess_index

        # If floor and ceiling have converged
        if floor_index + 1 == ceiling_index:
            # Between floor and ceiling is where we flipped to the beginning
            # so ceiling is alphabetically first
            return ceiling_index


words = ['k', 'v', 'a', 'b', 'c', 'd', 'e', 'g', 'i']
print(find_rotation_point(words))


# k m n o p q a b c d


def find_rotation_point_mine(words):
    left = 0
    right = len(words)-1
    while left < right:
        mid_point = ((right - left) + left) // 2
        if words[mid_point] >= words[0]:
            left = mid_point

        elif words[mid_point] <= words[0]:
            right = mid_point
        # when they meet
        if left+1 == right:
            return right
    print()


words = ['k', 'v', 'a', 'b', 'c', 'd', 'e', 'g', 'i']
print(find_rotation_point_mine(words))
