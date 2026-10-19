class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqSet, res = set(nums), 0
        seqMap = {}
        for num in nums:
            if num in seqMap:
                continue
   
            start = num
            count = 1
            while(start+1 in seqSet):
                if start+1 in seqMap:
                    count += seqMap[start+1]
                    break
                else:
                    count+=1
                    start+=1
 
            seqMap[num] = count
            res = max(res,count)
            
        return res



        