class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_hash = {}
        for i, num in enumerate(nums):
            num2 = target - num
            if num2 in my_hash:
                return [my_hash[num2],i]
            my_hash[num] = i
        return [0,0]

