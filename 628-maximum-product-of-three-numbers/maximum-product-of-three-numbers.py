from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Track three largest
        lar = float("-inf")
        slar = float("-inf")
        tlar = float("-inf")

        
        smal = float("inf")
        ssmal = float("inf")

        for num in nums:
           
            if num > lar:
                tlar = slar
                slar = lar
                lar = num
            elif num > slar:
                tlar = slar
                slar = num
            elif num > tlar:
                tlar = num

           
            if num < smal:
                ssmal = smal
                smal = num
            elif num < ssmal:
                ssmal = num

        return max(lar * slar * tlar, smal * ssmal * lar)
