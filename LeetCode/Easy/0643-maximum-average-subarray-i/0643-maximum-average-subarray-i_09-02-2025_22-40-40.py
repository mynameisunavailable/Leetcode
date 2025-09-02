class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right = 0, k - 1
        max_res = sum(nums[left: k])
        temp_res = max_res
        length = len(nums)
        while right < length - 1:
            temp_res = temp_res - nums[left] + nums[right + 1]
            left += 1
            right += 1
            if temp_res > max_res:
                max_res = temp_res
        return max_res / k
