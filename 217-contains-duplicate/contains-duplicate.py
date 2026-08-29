class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup = {}

        for num in nums:
            if num in dup:
                return True
            dup[num] = dup.get(num, 0) + 1

        return False
        

