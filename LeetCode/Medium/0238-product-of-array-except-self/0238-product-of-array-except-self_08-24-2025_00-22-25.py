class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for x in nums]
        product = 1
        #pass from front
        for i in range(1, len(result)):
            product *= nums[i - 1]
            result[i] = product

        #pass from back
        product = 1
        for i in reversed(range(0, len(result)-1)):
            product *= nums[i + 1]
            result[i] = result[i] * product
        
        return result