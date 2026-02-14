class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = 0
        
        for i in range (len(nums) -1):
            for j in range (i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    l = i 
                    r = j

        return [l, r]