class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = set(nums)
        ret = []
        for i in range(1,len(nums)+1):
            if i not in n:
                ret.append(i) 
        return ret
        