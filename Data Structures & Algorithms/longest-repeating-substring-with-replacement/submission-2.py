class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # in the window keep the most frequent, not the least
        # window size - max_frequency <= k
        l,n = 0,len(s)
        count = {}
        replacement,maxf,res = 0,0,0

        for r in range(n):
            count[s[r]] = count.get(s[r],0) + 1
 
            while ((r-l+1)-max(count.values()) > k):
                count[s[l]]-=1
                l+=1


            res = max(res, r-l+1)

        return res
                





#AAABABBBB
#k=2
# for a given string, l=0,r=2, 
# which element is the most frequent element so far
# is the current element = most frequent element - yes, count the lenght
# if not - we check if we have replacement remaining, if yes, we inc the replamenet and count the length
# if no replacement - we move the left pointer and dec the count of left most value 


# l=0,r=0, maxfreq[A] = 1, 1-1=0
#  l=0, r=1, maxfreq[A] = 2, 2-2=0
# l=0,r=2