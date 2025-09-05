def findMaxConsecutiveOnes(nums: list[int]) -> int:
    max_res = temp_res = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            temp_res += 1
        else:
            if temp_res > max_res:
                max_res = temp_res
            temp_res = 0
    #check final item
    max_res = max(temp_res, max_res)
    return max_res

#return a list with the first k 0s filled
#return index for left and right pointers
def initialise_list(nums: list[int], k: int) -> int:
    left = right = -1
    for i in range(len(nums)):
        if k > 0:
            if nums[i] == 0:
                k -= 1
                nums[i] = 1
        else:
            break
        right += 1
    
    length = len(nums)
    while nums[right] == 1:
        if right < length - 1:
            right += 1
        else:
            return nums, left, right
    right -= 1
    
    return nums, left, right

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if k < 1:
            return findMaxConsecutiveOnes(nums)

        #create left right and nums_dup
        length = len(nums)
        nums_dup = nums[:]
        nums_dup, left, right = initialise_list(nums_dup, k)
        print("", nums, "\n", nums_dup, left, right)

        max_len = right - left
        while right < length - 1 and left < right:
            if nums[left + 1] == 1:
                left += 1
            else:
                nums_dup[left + 1] = 0
                left += 1
                right += 1
                while nums_dup[right] == 1 and right < length - 1:
                    right += 1
                nums_dup[right] = 1
                while nums_dup[right] == 1:
                    if right < length - 1:
                        right += 1
                    elif right == length - 1:
                        return max(right - left, max_len)
                right -= 1
                max_len = max(right - left, max_len)
            
        return max_len