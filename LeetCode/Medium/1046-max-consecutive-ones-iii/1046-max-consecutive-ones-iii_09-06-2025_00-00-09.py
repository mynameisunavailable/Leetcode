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

import collections 

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if k < 1:
            return findMaxConsecutiveOnes(nums)

        zero_queue = collections.deque()
        length = len(nums)
        left = -1
        right = 0
        max_len = 0
        nums.append(0)
        while right < length:
            while k > 0:
                if nums[right] == 0:
                    if right < length:
                        zero_queue.append(right)
                        k -= 1
                    else:
                        break
                right += 1
            #move right pointer to right
            while nums[right] == 1:
                right += 1
            if right - left - 1> max_len:
                max_len = right - left - 1
            left = zero_queue.popleft()
            k += 1

        return max_len