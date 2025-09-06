class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        right_sum = sum(nums)
        cum_sum = 0
        for i in range(length):
            right_sum -= nums[i]
            if right_sum == cum_sum:
                return i
            cum_sum += nums[i]
            
        return (-1)