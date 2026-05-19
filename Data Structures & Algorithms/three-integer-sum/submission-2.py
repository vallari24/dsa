class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n,res = len(nums),[]
        if n<3:
            return [[]]

        nums.sort()

        for i in range(0,n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1, n-1
            target = 0 - nums[i]
            while(l<r):
                cursum = nums[l] + nums[r]
                if cursum == target:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while(nums[l]==nums[l-1] and l<r):
                        l+=1
                if cursum < target:
                    l+=1
                if cursum > target:
                    r-=1
        return res




# issues with this approach - duplicates

# 1 [[0, 1], [2, -1]]
# 0 [[-1, 1], [1, -1]]
# -1 [[-1, 0], [0, -1]]
# -2 [[-1, -1]]
# 4 []

#  def twoSum(self, nums, target, selfi): # O(n)
#         seen,res = set(),[]
#         for i in range(len(nums)):
#             if i == selfi:
#                 continue
#             diff = target - nums[i]
#             if diff in seen:
#                 res.append([diff,nums[i]])
#             seen.add(nums[i])
#         return res
 
#  #[-1,0,1,2,-1,-4]
#  #[-4,-1,-1,0,1,2]
#  # 


#     def threeSum(self, nums: List[int]) -> List[List[int]]:

#         n = len(nums)
#         if n < 3:
#             return []

#         res, seen = [[]], set()

#         for i in range(n):
#             if nums[i] in seen:
#                 continue
#             seen.add(nums[i])
#             target = 0 - nums[i]
#             twosum = self.twoSum(nums,target,i)
#             print(target, twosum)
#             if twosum:
#                 res.append([nums[i],twosum[0]])
        

#         return res


        


# nums = [-1,0,1,2,-1,-4]
# -1, 0-(-1) = 1
# index - [0,1], [2,-1]
# 0, 0-0 = 0
# [1,-1]
# 1, 0-1 = -1
# [-1,0]
# 2, 2-1 = 1
# [0,1], [2,-1]
# 

# nums = [-1,0,1,2,-1,-4]
# -1 -> 0 and check if anything else is 0
# 0-(-1) = 1
# find targets for each numbers
# find those numbers in array