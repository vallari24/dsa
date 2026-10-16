class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap, heap, res = {}, [], []
        bucket = []
        for num in nums:
            countMap[num] =  1 + countMap.get(num,0)

        for key,value in countMap.items():
            if len(heap)<k:
                heapq.heappush(heap,[value,key])
            else:
                smallest = heapq.heappop(heap)
                if value > smallest[0]:
                    heapq.heappush(heap,[value,key])
                else:
                    heapq.heappush(heap,smallest)
        
        # print(heap)
        for i in range(k):
            big = heapq.heappop(heap)
            res.append(big[1])


        return res
        