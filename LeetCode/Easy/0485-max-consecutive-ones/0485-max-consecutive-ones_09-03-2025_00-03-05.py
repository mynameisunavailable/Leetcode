class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        length = len(nums)
        max_res = temp_res = 0
        while i < length:
            if nums[i] == 1:
                temp_res += 1
            else:
                if temp_res > max_res:
                    max_res = temp_res
                temp_res = 0
            i += 1
        #check final item
        if temp_res > max_res:
            max_res = temp_res
        return max_res