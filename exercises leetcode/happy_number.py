# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# 1 9
# 19 mod 1 9

# Step 0 initialise the set, current_sum
# STEP 1 calculate sum
# Step 2 check cycle


class Solution:
    def isHappy(self, n: int) -> bool:
        hash_set = set()
        sum_n = 0
        while sum_n != 1:
            current = n
            sum_n = 0

            # Step 1
            while current != 0:
                sum_n += (current % 10) ** 2
                current = current // 10

                # Step 2
            if sum_n in hash_set:
                return False

            else:
                hash_set.add(sum)
                n = sum_n
        return True