class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()  # use a set for fast lookup
        for num in nums:
            if num in hashmap:
                return True
            else:
                hashmap.add(num)
        return False