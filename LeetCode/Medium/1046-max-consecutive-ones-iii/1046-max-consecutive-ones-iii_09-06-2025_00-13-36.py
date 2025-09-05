class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        length = len(nums)
        left = -1
        max_len = remainder = 0
        for right in range(length):
            if nums[right] == 0:
                remainder += 1
            
            while remainder > k:
                left += 1
                if nums[left] == 0:
                    remainder -= 1

            if right - left > max_len:
                max_len = right - left

        return max_len