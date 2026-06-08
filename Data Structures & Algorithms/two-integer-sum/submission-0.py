class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preNums = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in preNums:
                return [preNums[diff], i]
            preNums[val] = i    
        return
