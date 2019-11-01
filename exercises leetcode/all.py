class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_i = 0
        i = 0
        while i != (len(nums) - 1):
            if nums[i] == 0:
                del nums[i]
                zero_i += 1
            else:
                i += 1
        return nums.extend([0] * zero_i)

        """
        Do not return anything, modify nums in-place instead.
        """


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while digits[i] == 9:
            digits[i] = 0
            i -= 1
            if i < 0:
                digits.insert(0, 1)
                return digits
        digits[i] = digits[i] + 1
        return digits

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        desired_sum = {}
        for i in range(len(nums)):
            desired_sum[target - nums[i]] = i
        for i in range(len(nums)):
            if nums[i] in desired_sum.keys() and desired_sum[nums[i]] != i:
                return [i, desired_sum[nums[i]]]
