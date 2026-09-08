class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_map = {}


        for  i in range(len(nums)):
            subs = target-nums[i]

            if subs in nums_map:
                return [nums_map[subs],i]

            nums_map[nums[i]] = i

        return [0,0]