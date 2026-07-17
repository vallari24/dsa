class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        l,maxArray=0,[]
        for i in range(0,len(nums)-k+1):
            subArray = nums[i:i+k]
            maxArray.append(max(subArray))
        
        return maxArray

        