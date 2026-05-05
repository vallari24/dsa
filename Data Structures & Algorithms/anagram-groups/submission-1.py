class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # strMap = {}
        # abc = "abcdefghijklmnopqrstuvwxyz"
         
        # # print(abcMap)
        # for string in strs:
        #     abcMap = {char:0 for char in abc}
        #     for char in string:
        #          abcMap[char] += 1
        #     toStr = str(abcMap)
        #     if toStr in strMap:
        #         strMap[toStr].append(string)
        #     else:
        #         strMap[toStr] = [string]
        
        # # print (strMap.values())
        # res = []
        # for values in strMap.values():
        #     res.append(values)


        # return res

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for char in s:
                n = ord(char) - ord('a')
                count[n] += 1

            # print (count)
            res[tuple(count)].append(s)

        # print (res)
        return list(res.values())


        
        