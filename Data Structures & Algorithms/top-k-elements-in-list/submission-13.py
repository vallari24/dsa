class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        countMap, res = {}, []
        n = len(nums)
        bucket = [[] for _ in range(n+1)]
 
       
        for num in nums:
            countMap[num] =  1 + countMap.get(num,0)

        for key,value in countMap.items():
            bucket[value].append(key)
        # print(bucket)

        for i in range(n, -1, -1):
            if bucket[i]:
                res.extend(bucket[i])
                if len(res) == k:
                    break
        return res
        
        


        
        