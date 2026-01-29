class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        p = n*(n+1)//2 - sum(nums)

        return p
