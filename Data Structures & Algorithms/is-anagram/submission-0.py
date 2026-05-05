class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = {}
        set_t = {}
        if len(s) != len(t):
            return False
        for char in s:
            if char in set_s:
                count = set_s[char]
                set_s[char] = count+1
            else:
                set_s[char] = 1
        
        for char in t:
            if char in set_t:
                count = set_t[char]
                set_t[char] = count+1
            else:
                set_t[char] = 1
        
        if set_s == set_t:
            return True
        
        return False


            

        