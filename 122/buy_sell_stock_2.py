class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(0, len(prices)-1):
            j = i + 1
            diff = prices[j] - prices[i]
            if diff > 0:
                prices += diff
        
        return profit