class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        length = len(nums)
        right = left = max_len = 0
        while right < length:
            if k > 0:
                if nums[right] == 0:
                    k -= 1
                right += 1
                # print(right)
            else:
                while right < length and nums[right] == 1:
                    right += 1
                max_len = max(right - left, max_len)
                # print(left, right, max_len, nums[left:right])
                if nums[left] == 0:
                    k += 1
                left += 1
        max_len = max(right - left, max_len)

        return max_len