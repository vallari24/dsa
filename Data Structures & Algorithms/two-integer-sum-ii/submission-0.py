class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) < 1:
            return [0,0]
        
        l,r = 0,len(numbers)-1

        while(l<r):
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
            if sum < target:
                l += 1
            if sum == target:
                return [l+1,r+1]
        return [0,0]
    



# [1,2,3,4]
# start with l, r extreme
# sum = n[l] + n[r]
# if target is small than sum - move right to inc
# if target is big than sum - move left
# u will find the target
        