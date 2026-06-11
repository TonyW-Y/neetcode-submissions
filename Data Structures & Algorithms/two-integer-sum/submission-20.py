class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        updated_Nums = {}
        for i,n in enumerate(nums):
            look = target - n
            if look in updated_Nums:
                return [updated_Nums[look], i]
            updated_Nums[n] = i
