class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        uniqueElem = set(nums)
        maps = {item:0 for item in uniqueElem}


        for num in nums:
            maps[num] += 1
        # print(maps)
        # sorting dict
        map1 = sorted(maps.items(), key=lambda x: x[1], reverse=True)
        # map2 = sorted(maps)
        # map3 = sorted(maps.items())
        # map4 = sorted(maps.keys())
        # map5 = sorted(maps.values())
        # print("1",map1, "2",map2, "3",map3,"4", map4, "5",map5)

    

        return [x[0] for x in map1[:k]]
        # return []

# {1:1, 2:3, 3:4}
# return - 2,3, k=2
# one way is to sort thee unique elements and return the top k
# another way is [(1,1), (2,3)] 
# maps = sorted  


        
        