class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                if dif > max:
                    max = diff
            else:
                l = r
            r += 1
    
    return max