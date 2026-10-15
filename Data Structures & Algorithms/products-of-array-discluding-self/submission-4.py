class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res, prefix, suffix = [1]*l, [1]*l, [1]*l

        for i in range(1,l):
            prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(l-2,-1,-1):
            suffix[i] = nums[i+1] * suffix[i+1]
        for i in range(l):
            res[i] = prefix[i] * suffix[i]



        return res
        