class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sets = set()
        for num in nums:
            if num in sets:
                return True
            sets.add(num)
        # print(sets)
        return False
    