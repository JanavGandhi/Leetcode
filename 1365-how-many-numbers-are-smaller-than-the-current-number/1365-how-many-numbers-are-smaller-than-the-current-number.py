class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = sorted(nums)   

        hashMap = {}

        for index, val in enumerate(n):
            if val not in hashMap:
                hashMap[val] = index

        ret = []
        for i in nums:
            ret.append(hashMap[i])

        return ret