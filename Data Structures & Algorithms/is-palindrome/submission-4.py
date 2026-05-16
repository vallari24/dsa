class Solution:


    def isAlphanumeric(self,char):
        is_upper = 65 <= ord(char) <= 90   # A-Z
        is_lower = 97 <= ord(char) <= 122  # a-z
        is_digit = 48 <= ord(char) <= 57   # 0-9
        if not (is_upper or is_lower or is_digit):
            return False
        return True

    def isPalindrome(self, s: str) -> bool:


        n = len(s)

        if n<2:
            return True

        start, end = 0,n-1
        while(start<end):
            while(start<end and self.isAlphanumeric(s[start]) == False):
                start+=1
            while(start<end and self.isAlphanumeric(s[end]) == False):
                end-=1
         
            if (s[start].lower()!=s[end].lower()):
                return False
        
            start+=1
            end-=1
        return True


# s= "..."

        