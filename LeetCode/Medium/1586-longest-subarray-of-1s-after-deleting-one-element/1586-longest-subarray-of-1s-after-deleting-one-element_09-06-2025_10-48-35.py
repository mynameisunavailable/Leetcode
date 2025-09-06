class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        length = len(nums)
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
