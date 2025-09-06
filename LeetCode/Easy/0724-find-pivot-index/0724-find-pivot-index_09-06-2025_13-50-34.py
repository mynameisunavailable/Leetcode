class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        left_sum = []
        right_sum = []
        temp_sum = 0
        for i in nums:
            temp_sum += i
            left_sum.append(temp_sum)
        
        temp_sum = 0
        for i in reversed(nums):
            temp_sum += i
            right_sum.append(temp_sum)

        for i in range(length):
            if left_sum[i] == right_sum[length - 1 - i]:
                return i
        
        return (-1)