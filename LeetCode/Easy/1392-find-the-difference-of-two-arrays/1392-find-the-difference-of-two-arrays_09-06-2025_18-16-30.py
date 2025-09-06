class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        numsset1 = set(nums1)
        numsset2 = set(nums2)
        answer = []
        answer.append(list(numsset1.difference(numsset2)))
        answer.append(list(numsset2.difference(numsset1)))

        return answer