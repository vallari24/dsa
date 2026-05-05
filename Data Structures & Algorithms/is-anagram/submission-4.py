class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # charCount = {}
        # for char in s:
        #     if char in charCount:
        #         charCount[char] += 1
        #     else:
        #         charCount[char] = 1
        # # print (charCount)
        # for char in t:
        #     if char in charCount:
        #         charCount[char] -= 1
        #     else:
        #         return False
        # # print (charCount)
        # for count in charCount.values():
        #     # print (count)
        #     if count != 0:
        #         return False
        # return True

        countS, countT = {}, {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        
        return countS == countT
        
            


        

            

        