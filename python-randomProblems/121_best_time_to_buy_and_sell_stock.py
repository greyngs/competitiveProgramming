class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxPro = 0
        minPri = float('inf')

        for price in prices:
            if price < minPri:
                minPri = price
            elif price - minPri > maxPro:
                maxPro = price - minPri
        
        return maxPro

