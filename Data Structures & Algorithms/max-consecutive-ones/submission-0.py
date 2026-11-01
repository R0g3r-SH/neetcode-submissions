class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxC = 0 
        cnt = 0 

        for n in nums:
            if n == 1:
                cnt +=1
            else:
                maxC = max(maxC,cnt)
                cnt = 0

        return max(maxC,cnt)
        