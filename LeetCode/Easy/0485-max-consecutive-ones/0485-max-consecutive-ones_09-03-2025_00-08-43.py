class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_res = temp_res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                temp_res += 1
            else:
                if temp_res > max_res:
                    max_res = temp_res
                temp_res = 0
            i += 1
        #check final item
        max_res = max(temp_res, max_res)
        return max_res