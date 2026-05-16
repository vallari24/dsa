class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums)<=1:
            return len(nums)


        seen = defaultdict(list)
        seen = {num:[] for num in nums}
        maxL = 1
        

        for num in seen:
            if num-1 in seen:
                continue
            else:
                curnum = num
                curmax = 1
                while (curnum in seen):
                    if curmax > maxL:
                        maxL = curmax
                    curnum +=1 
                    curmax +=1

        return maxL



# [2,20,4,10,3,4,5]
# [2,3,4,5]


#[1,-8,7,-2,-4,-4,6,3,-4,0,-7,-1,5,1,-9,-3]
