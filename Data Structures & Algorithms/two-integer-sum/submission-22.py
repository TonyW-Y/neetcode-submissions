class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_num = {}

        for i, num in enumerate(nums):
            val = target - num
            if val in hash_num:
                return [hash_num[val], i]
            hash_num[num] = i
        return [0,0]
        