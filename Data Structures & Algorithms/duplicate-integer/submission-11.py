class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = sorted(nums)
        for i, num in enumerate(res[:-1]):
            if num == res[i+1]:
                return True
        return False