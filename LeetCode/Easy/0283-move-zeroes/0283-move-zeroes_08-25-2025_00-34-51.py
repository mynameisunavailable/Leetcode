class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n_pointer = 0
        index = 0
        n = len(nums)
        while n_pointer < len(nums):
            if nums[n_pointer] != 0:
                if n_pointer == index:
                    pass
                else:
                    nums[n_pointer], nums[index] = nums[index], nums[n_pointer]
                    # index += 1
                n_pointer += 1
                index += 1
            else:
                n_pointer += 1