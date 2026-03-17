class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for index, val in enumerate(nums):
            diff = target - val 

            if diff in hashMap:
                return [index,hashMap[diff]]

            hashMap[val] = index