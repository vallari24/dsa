class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1] * l
        prefix = 1
        for i in range(0,l):
            res[i] = prefix
            prefix *= nums[i]
        # print(res)
        suffix = 1
        for i in range(l-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]
        return res

#.   [1,2,4,6]
#res [1,1,2,8]
# res [.    ,8]


           # if l==0:
        #     return []
        # if l==1:
        #     return [1]
        # if l==2:
        #     return [nums[1],nums[0]]    
#[2,3,4,5]
#[1,2,6,24]
#[120,60,20,5,1]

#[1,2,4,6]
#[1,1*2,1*2*4,1*2*4*6] = [1,2,8,48]
#[6*4*2*1,6*4*2,6*4,6] = [48,48,24,6]
# [6*4*2, 1*4*6, 1*2*6,1*2*4]
#[2*4*6, 1*4*6, ]
#[47, 46, 24-8, 6-48]
# [48,24,12,8]
# [48,24,12,8]

# [-1,0,1,2,3]
# [-1,0,0,0,0]
# [ 0,0,6,6,3]

#ans [0,6*-1,0*6,3*0,]
        