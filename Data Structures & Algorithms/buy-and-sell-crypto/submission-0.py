class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro=0
        minPrice=float('inf')
        for i in prices:
            minPrice=min(i,minPrice)
            maxPro=max(maxPro,i-minPrice)
        return maxPro
        