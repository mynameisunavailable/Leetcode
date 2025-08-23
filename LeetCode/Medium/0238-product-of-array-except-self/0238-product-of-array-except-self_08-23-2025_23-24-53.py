class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = nums.copy()
        result.insert(0, 1)
        result.append(1)
        front_list = result.copy()
        #pass from front
        for i in range(1, len(nums)+1):
            temp = result[i - 1] * front_list[i - 1]
            front_list[i] = temp
        # print(front_list)

        back_list = result.copy()
        #pass from back
        for i in reversed(range(1, len(nums)+1)):
            temp = result[i + 1] * back_list[i + 1]
            back_list[i] = temp
        
        result = []
        for i in range(0, len(front_list)):
            product = front_list[i] * back_list[i]
            result.append(product)
        return result[1:-1]