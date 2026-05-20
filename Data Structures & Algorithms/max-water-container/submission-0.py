class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxwater,n = 0,len(heights)
        l,r = 0,n-1

        while(l<r):
            leftval, rightval = heights[l],heights[r]
            curwater = min(leftval,rightval) * (r-l)
            print(leftval, rightval,curwater)
            maxwater = max(maxwater,curwater)

            if leftval >= rightval:
                r-=1
            else:
                l+=1
        return maxwater

        

        