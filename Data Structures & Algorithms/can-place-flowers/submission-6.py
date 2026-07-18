class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = 0
        for i in range(len(flowerbed)):
            if not flowerbed[i]:
                left = (i == 0 or not flowerbed[i - 1])
                right = (i == len(flowerbed) - 1 or not flowerbed[i + 1])

                if left and right:
                    flowers += 1
                    flowerbed[i] = 1
        
        return flowers >= n