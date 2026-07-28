class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = []
        g={}

        for num in nums2[::-1]:

            while stack and stack[-1] <= num:
                stack.pop()


            if stack:
                g[num] = stack[-1]
            else:
                g[num] = -1

            stack.append(num)

        for num in nums1:
            ans.append(g[num])

        return ans