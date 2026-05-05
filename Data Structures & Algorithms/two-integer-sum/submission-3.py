class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numDict = {}
        for i,num in enumerate(nums):
            numDict[num] = i
        # print (numDict)
        for i,num in enumerate(nums):
            find = target - num
            if find in numDict and i != numDict[find]:
                return [i, numDict[find]]
        
        return []

        
        