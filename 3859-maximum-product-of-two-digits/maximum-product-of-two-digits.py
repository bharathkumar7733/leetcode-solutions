class Solution:
    def maxProduct(self, n: int) -> int:
        digits = str(n)

        lar = float("-inf")
        slar = float("-inf")

        for digit in digits:
            num = int(digit)

            if num > lar:
                slar = lar
                lar = num

            elif num > slar:
                slar = num

        return lar * slar