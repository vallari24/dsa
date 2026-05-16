class Solution:


    def is_alphanumeric(self,char):
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

        # for i in range(n//2):
        start, end = 0,n-1
        while(start<end):
            # print (start,s[start],end,s[end])
            while(start<end and self.is_alphanumeric(s[start]) == False):
                start+=1
                continue
            while(start<end and self.is_alphanumeric(s[end]) == False):
                end-=1
                continue
            # print (start,end)
            if(start==end):
                return True
            if (s[start].lower()!=s[end].lower()):
                return False
            else:
                start+=1
                end-=1
            # print (start,s[start],end,s[end])
        return True


# s= "..."

        