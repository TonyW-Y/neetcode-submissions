class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_hash = {}

        for num in nums:
            if num not in my_hash:
                my_hash[num] = 1
            else:
                my_hash[num] += 1
        for key in my_hash:
            if my_hash[key] != 1:
                return True

        return False