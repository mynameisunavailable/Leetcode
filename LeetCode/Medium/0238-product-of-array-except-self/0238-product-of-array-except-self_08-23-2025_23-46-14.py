class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums.insert(0, 1)
        nums.append(1)
        result = nums.copy()
        #pass from front
        for i in range(1, len(result) - 1):
            temp = result[i - 1] * nums[i - 1]
            result[i] = temp

        resultback = nums.copy()
        #pass from back
        for i in reversed(range(1, len(result) - 1)):
            temp = nums[i + 1] * resultback[i + 1]
            nums[i] = temp
        
        for i in range(0, len(result)):
            temp = result[i] * nums[i]
            result[i] = temp
        return result[1:-1]