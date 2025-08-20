def plantflowers(i: int, flowerbed: list[int], n: int, blocked: bool) -> bool:
    #stop if all flowers planted
    if n == 0:
        return True
    #stop if flowerbed reached the end
    if len(flowerbed) < i + 1 + 1:
        return False

    if flowerbed[i] == 1:
        return plantflowers(i + 1, flowerbed, n, True)
    elif blocked == True:
        return plantflowers(i + 1, flowerbed, n, False)
    elif blocked == False and flowerbed[i + 1] == 1:
        return plantflowers(i + 1, flowerbed, n, False)
    elif blocked == False:
        return plantflowers(i + 1, flowerbed, n - 1, True)

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #add a 0 at the end to prevent index error
        flowerbed.append(0)
        return plantflowers(0, flowerbed, n, False)