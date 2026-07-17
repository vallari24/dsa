class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n,nTarget,l = len(s),len(t),0
        if nTarget>n:
            return ""

        countTarget, countS = {},{}

        for i in range(nTarget):
            countTarget[t[i]] = countTarget.get(t[i],0) + 1

        have,need = 0,len(countTarget)
        l,res,resLen = 0,"", float('inf')


        for r in range(n):
            char = s[r]
            countS[char] = countS.get(char,0) + 1
        
            if char in countTarget and countS[char]==countTarget[char]:
                have += 1

            while have==need:
                if r-l+1 < resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                leftChar = s[l]
                countS[leftChar]-=1
                if leftChar in countTarget and countS[leftChar]<countTarget[leftChar]:
                    have -= 1 
                l+=1


        return res


            














        