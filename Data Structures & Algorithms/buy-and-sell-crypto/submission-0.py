class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n,maxprofit = len(prices),0
        for i in range(n):
            for j in range(i+1,n):
                curprofit = prices[j] - prices[i]
                maxprofit = max(maxprofit,curprofit)
        
        return maxprofit




# prices = [10,1,7,2]
# 1-10 =-1, 7-10= -3 , 2-10
# 7-1,2-1
# 2-7

# prices = [10,8,7,5,2]
# 8-10, 7-10, 5-10, 2-19
# 7-8, 5-8, 2-8
# 5-7, 2-7
# 2-5
        