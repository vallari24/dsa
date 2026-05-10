class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        countMap,res = {},[]
        bucket = [[] for _ in range(len(nums)+1)]


        for num in nums:
            countMap[num] = 1 + countMap.get(num,0)

        # print(countMap)
        # print(bucket)
        
        for item,count in countMap.items():
            bucket[count].append(item)

        

        for i in range(len(bucket)-1, 0, -1):
            if bucket[i]:
                res.extend(bucket[i])
            if len(res) >= k:
                break

        return res[:k]
   
        
        
        
        
        
        # # print(maps)
        # # sorting dict
        # map1 = sorted(maps.items(), key=lambda x: x[1], reverse=True)
        # # map2 = sorted(maps)
        # # map3 = sorted(maps.items())
        # # map4 = sorted(maps.keys())
        # # map5 = sorted(maps.values())
        # # print("1",map1, "2",map2, "3",map3,"4", map4, "5",map5)

    

        # return [x[0] for x in map1[:k]]
        # # return []




# {1:1, 2:3, 3:4}
# return - 2,3, k=2
# one way is to sort thee unique elements and return the top k
# another way is [(1,1), (2,3)] 
# maps = sorted  


        
        