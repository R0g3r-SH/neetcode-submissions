class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        mxA = 0

        l = 0
        r = len(heights)-1

        while l<r:
            w = r - l
            h = min(heights[r],heights[l])
            mxA = max(mxA,w*h)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return mxA

