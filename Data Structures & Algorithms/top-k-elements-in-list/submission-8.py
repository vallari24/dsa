class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap, heap, res = {}, [], []
        bucket = []
        for num in nums:
            countMap[num] =  1 + countMap.get(num,0)

        heap = [[-value,key] for key,value in countMap.items()]
        heapq.heapify(heap)
        # print(heap)

        for i in range(k):
            big = heapq.heappop(heap)
            res.append(big[1])


        return res



# get the dict and then sort it
# sparse one - more repeating numbers, 
# k list, and check if k is disrupted each time u add something, k can be a map
# 