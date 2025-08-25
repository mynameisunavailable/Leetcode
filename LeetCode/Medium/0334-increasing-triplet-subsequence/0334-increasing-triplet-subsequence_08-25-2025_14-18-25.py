class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        size = len(nums)
        max_n = nums[size - 1] - 1
        for i in reversed(range(size)):
            # print(i)
            if max_n < nums[i]:
                max_n = nums[i]
                max_n2 = nums[i - 1]
                for j in reversed(range(i - 1)):
                    if nums[j] >= max_n:
                        continue
                    elif nums[j] < max_n2 and max_n > max_n2:
                        return True
                    elif max_n2 < nums[j]:
                        max_n2 = nums[j]
        return False
