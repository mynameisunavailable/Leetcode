class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.insert(0,0)
        n_pointer = 0
        z_pointer = 0
        while n_pointer < len(nums) and z_pointer < len(nums):
            if nums[n_pointer] == 0:
                n_pointer += 1
            elif nums[z_pointer] != 0:
                z_pointer += 1
            else:
                nums[n_pointer], nums[z_pointer] = nums[z_pointer], nums[n_pointer]
        nums.pop(-1)