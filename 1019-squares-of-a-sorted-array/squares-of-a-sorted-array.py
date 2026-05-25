class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq =[]
        for x in nums:
            sq.append(x**2)
        sq.sort()
        return sq
    
        