class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0 
        r = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target - nums[j] == nums[i]:
                    l = j
                    r = i
                else:
                    continue

        return r,l
