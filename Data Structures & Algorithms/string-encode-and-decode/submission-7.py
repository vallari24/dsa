class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            n = str(len(s))
            res += n + "#" + s
 
        return res


    def decode(self, s: str) -> List[str]:
        # print(s)

        res,i,j = [],0,0
        # print(s)

        while (j < len(s)):
            if (s[j]=='#'):
                print (s[i:j])
                lenght = int(s[i:j])
                res.append(s[j+1:j+1+lenght])
                # print(res)
                i = j+1+lenght
                j=i
            j+=1
        return res

            # while (s[j]!='#'):
            #     j += 1
            #     lenght = int(s[i:j])

        #     if s[i] == '#':
        #         lenght = int(s[:i-1])
        #         res.append(s[j+1:j+1+lenght])
        #         i = j+1+lenght
        #     i+=1
        # return res




        # for i,char in enumerate(s):
        #     delimiter = s.find("#")
        #     # print(delimiter)
        #     if delimiter == -1:
        #         return res
            
        #     l = int(s[:delimiter])
        #     # print("l",l)
   
        #     res.append(s[delimiter+1:delimiter+1+l])
        #     # print (res)
        #     s = s[l+2:]
        #     # print(s)

        # return res

