class Solution:


    def isAlphanumeric(self,char):
        is_upper = ord('A') <= ord(char) <= ord('Z')   # A-Z
        is_lower = ord('a') <= ord(char) <= ord('z')  # a-z
        is_digit = ord('0') <= ord(char) <= ord('9')   # 0-9
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

        