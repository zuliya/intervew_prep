def firstUniqChar(self, s: str) -> int:
    for i in range(len(s)):
        if s[i] not in s[i+1:] and s[i] not in s[0:i]:
            return i
    return -1


# reverse integer
import math
def reverse(x: int) -> int:
    reverse_x = 0
    str_x = str(abs(x))
    for i in range(len(str_x)):
        reverse_x += int(str_x[i]) * 10 ** i

    if reverse_x > 2 ** 31 - 1:
        return 0
    elif x > 0:
        return reverse_x
    else:
        return reverse_x * (-1)



def reverseString(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    for i in range(len(s) // 2):
        s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
    print(s)
