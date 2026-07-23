class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque 

        queue, res = deque(), []
        l,r,n = 0,0,len(nums)

        while(r < n):
             
            while queue and nums[r] > nums[queue[-1]]:
                queue.pop()
            queue.append(r)

            if l>queue[0]:
                queue.popleft()
  

            if (r+1)>=k:
                res.append(nums[queue[0]])
                l+=1
            r+=1
        
        return res





        