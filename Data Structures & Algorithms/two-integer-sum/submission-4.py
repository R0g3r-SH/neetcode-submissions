class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_hash = {}

        for i in range(len(nums)):

            subs = target - nums[i]

            if subs in nums_hash:
                return [nums_hash[subs],i]

            nums_hash[nums[i]]=i

        return [-1,-1]