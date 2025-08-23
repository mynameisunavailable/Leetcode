class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums.insert(0, 1)
        nums.append(1)
        result = nums.copy()
        #pass from front
        for i in range(1, len(result) - 1):
            temp = result[i - 1] * nums[i - 1]
            result[i] = temp

        #pass from back
        product = 1
        for i in reversed(range(1, len(result) - 1)):
            product *= nums[i + 1]
            result[i] = result[i] * product
        
        return result[1:-1]