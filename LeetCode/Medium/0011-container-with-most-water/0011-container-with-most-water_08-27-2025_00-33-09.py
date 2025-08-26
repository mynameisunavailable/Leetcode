def rect_area(height: list[int], h1: int, h2: int):
    h = min(height[h1], height[h2])
    w = h2 - h1
    return h * w

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = max_area = 0
        j = len(height) - 1
        h1 = i
        h2 = j
        while i < len(height):
            temp_area = rect_area(height, h1, h2)
            if temp_area > max_area:
                max_area = temp_area
            if height[i] > height[h1]:
                h1 = i
            elif height[j] > height[h2]:
                h2 = j
            
            if height[h1] > height[h2]:
                j -= 1
            else:
                i += 1

        return max_area