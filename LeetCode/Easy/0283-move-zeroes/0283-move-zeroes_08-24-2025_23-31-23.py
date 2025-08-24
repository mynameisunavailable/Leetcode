class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        count = 0
        while count < len(nums):
            if nums[i] == 0:
                temp = nums.pop(i)
                nums.append(temp)
            else:
                i += 1
            count += 1