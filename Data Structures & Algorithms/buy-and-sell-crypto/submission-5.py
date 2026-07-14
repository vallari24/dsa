class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find out the max number to the right of current index
        # subtract the index with the max on the right
        # n,maxprice = len(prices),0
        # rightmax = [0] * n

        # for i in range(n-2,-1,-1):
        #     rightmax[i] = max(prices[i+1], rightmax[i+1])

        # for i in range(n):
        #     currentprice = rightmax[i] - prices[i]
        #     maxprice = max(currentprice, maxprice)

        # return maxprice








        # n,maxprofit = len(prices),0
        # l,r = 0,1

        # while(r<n):
        #     curprofit = prices[r] - prices[l]
        #     maxprofit = max(maxprofit,curprofit)
        #     if prices[r]<prices[l]:
        #         l = r
        #     r+=1
        # return maxprofit




        n,maxprofit = len(prices),0
        minprice = prices[0]
        
        for i in range(1,n):
            curprofit = prices[i] - minprice
            maxprofit = max(maxprofit,curprofit)
            minprice = min(minprice,prices[i])
        return maxprofit
#[10,1,5,6,7,1], minprice = 10
# 1-10 , minprice = 1
# 5-1 = 4


    #    for i in range(n):
    #         for j in range(i+1,n):
    #             curprofit = prices[j] - prices[i]
    #             maxprofit = max(maxprofit,curprofit)
        
    #     return maxprofit

# prices = [10,1,7,2,20,0,30]
# 1-10 =-1, 7-10= -3 , 2-10
# 7-1,2-1
# 2-7
# 1


# prices = [10,8,7,5,2]
# 8-10, 7-10, 5-10, 2-19
# 7-8, 5-8, 2-8
# 5-7, 2-7
# 2-5

# 0
# 30   