class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCount = {}
        for char in s:
            if char in charCount:
                charCount[char] += 1
            else:
                charCount[char] = 1
        # print (charCount)
        for char in t:
            if char in charCount:
                charCount[char] -= 1
            else:
                return False
        # print (charCount)
        for count in charCount.values():
            # print (count)
            if count != 0:
                return False
        return True
        
            


        

            

        