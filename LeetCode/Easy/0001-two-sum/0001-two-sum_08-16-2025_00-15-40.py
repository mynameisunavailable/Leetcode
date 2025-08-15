class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list= []
        count = 0
        for i in nums:
            # print(count)
            answer = target - i
            if answer in nums and nums.index(answer) != count:
                list = ([nums.index(answer), count])
                return list
            count += 1