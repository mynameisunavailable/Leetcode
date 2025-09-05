class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        length = len(nums)
        for right in range(length):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return length - left