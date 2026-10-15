class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = len(nums)
        leftprod, rightprod, res = [1]*total,[1]*total,[1]*total

        for i,num in enumerate(nums):
            if i==0:
                rightprod[i] = num
                leftprod[total-1] = nums[total-1]
            else:
                rightprod[i] = rightprod[i-1] * num
                leftprod[total-1-i] = leftprod[total-i] * nums[total-1-i]
        for i,num in enumerate(nums):
            if i==0:
                res[i] = leftprod[i+1]
            elif i==total-1:
                res[total-1] = rightprod[total-2]
            else: 
                res[i] = leftprod[i+1] * rightprod[i-1]
        return res
            


        