class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l,n1,n2 = 0,len(s1),len(s2)
        s1map,s2map = {},{}

        for char in s1:
            s1map[char] = s1map.get(char,0)+1
        # print(s1map)
        
        for r in range(n2):
            # print("start",char, s2map, r, l)
            
         
            char = s2[r]
            s2map[char] = s2map.get(char,0) + 1
            # print(s2map)
    
        
            if r-l+1 > n1:
                # print("if",n1,s2map,r,l)
                s2map[s2[l]]-=1
                if s2map[s2[l]]==0:
                    del s2map[s2[l]]
                l+=1
            if s1map==s2map:
                return True
            
      
        
        return False
            







# window + hashmap coz it has substrring and find out the counts
# brute force, take the lenght size of s1 in s2 
# and check if frequency of letters are same
# as we are moving right, we remove the freq from left and keep matching
# the freq of letters?