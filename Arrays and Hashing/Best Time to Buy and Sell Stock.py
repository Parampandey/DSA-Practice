class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0 # we use sliding window left pointer for buy the stock
        right=1 # right pointer is to sell the stock so profit right-left
        maxprofit=0
        while right<len(prices):
            if prices[left]>prices[right]:  
                left=right
            else:
                profit=prices[right]-prices[left]
                maxprofit=max(maxprofit,profit)
            right+=1
               
        return maxprofit 
               

