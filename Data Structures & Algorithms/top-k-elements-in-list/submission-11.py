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
                heapq.heappushpop(heap, [value, key])



        return [elem[1] for elem in heap]
        