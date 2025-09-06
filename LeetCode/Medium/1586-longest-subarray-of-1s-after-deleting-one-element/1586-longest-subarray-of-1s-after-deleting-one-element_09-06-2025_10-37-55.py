class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        #if no zero then just -1 from sum
        if sum(nums) == length:
            return length - 1

        delete = 1 #remove 1 element
        left = 0
        for i in range(length):
            if nums[i] == 0:
                delete -= 1
            
            if delete < 0:
                if nums[left] == 0:
                    delete += 1
                left += 1
        
        return length - left - 1