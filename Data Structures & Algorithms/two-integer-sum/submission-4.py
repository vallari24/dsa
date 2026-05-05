class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # numDict = {}
        # for i,num in enumerate(nums):
        #     numDict[num] = i
        # # print (numDict)
        # for i,num in enumerate(nums):
        #     find = target - num
        #     if find in numDict and i != numDict[find]:
        #         return [i, numDict[find]]
        
        # return []

        # we have to be careful with the i != numDict[find], we can't return two similar index
        # it is easy to solve it using one pass

        prevMap = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[num] = i
        return []
            

        
        