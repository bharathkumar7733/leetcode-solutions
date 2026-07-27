class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lar = float("-inf")
        slar = float("-inf")

        for num in nums:
            

            if num > lar:
                slar = lar
                lar = num

            elif num > slar:
                slar = num

        return (lar-1) * (slar-1)
        