class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i,l,r, total = 1,0,n-1,0
        leftmax, rightmax = [0] * n,[0] * n
        while (i<n):
            leftmax[i] = max(height[l],leftmax[l])
            rightmax[n-1-i] = max(height[r],rightmax[r])
            i+=1
            l+=1
            r-=1
        
        for i in range(n):
            trap = min(leftmax[i], rightmax[i]) - height[i]
            if trap > 0:
                total += trap


        return total
        