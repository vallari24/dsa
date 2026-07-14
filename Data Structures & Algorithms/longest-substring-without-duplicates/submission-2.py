class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force - u iterate for each index 
        # check if there is any repeat using hashmap
        # until u hit increment the count and use max
        n = len(s)
        if n<1:
            return 0
        l,r,maxlen = 0,1,1
        seen = set()
        seen.add(s[0])

        while(r<n):
            
            char = s[r]
            if char in seen:
                seen.remove(s[l])
                l+=1
                
            else:
                maxlen = max(maxlen, r-l+1)
                seen.add(char)
                r+=1
        
        return maxlen
        



        