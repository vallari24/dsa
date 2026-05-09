class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        uniqueElem = set(nums)
        maps = {item:0 for item in uniqueElem}


        for num in nums:
            maps[num] += 1

        # sorting dict
        maps = sorted(maps.items(), key=lambda x: x[1], reverse=True)

    

        return [x[0] for x in maps[:k]]

# {1:1, 2:3, 3:4}
# return - 2,3, k=2
# one way is to sort thee unique elements and return the top k
# another way is [(1,1), (2,3)]   


        
        