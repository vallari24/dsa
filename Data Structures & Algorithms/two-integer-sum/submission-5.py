class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map, result = {},[]
        for i,num in enumerate(nums):
            if num not in map:
                map[num] = [i]
            else:
                map[num].append(i)
        
        print(map)

        for i,num in enumerate(nums):
            find = target-num
            if find in map:
                print(find)
                for index in map[find]:
                    if index != i:
                        result.extend([i,index])
                        return result


        return result

        