class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        strMap = {}
        abc = "abcdefghijklmnopqrstuvwxyz"
         
        # print(abcMap)
        for string in strs:
            abcMap = {char:0 for char in abc}
            for char in string:
                 abcMap[char] += 1
            toStr = str(abcMap)
            if toStr in strMap:
                strMap[toStr].append(string)
            else:
                strMap[toStr] = [string]
        
        # print (strMap.values())
        res = []
        for values in strMap.values():
            res.append(values)


        return res


        
        