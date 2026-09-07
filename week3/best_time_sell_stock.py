class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        day = len(prices)
        dp_l = [0]*day
        dp_r = [0]*day
        low = prices[0]
        for i in range(1, day):
            low = min(low, prices[i])
            dp_l[i] = max(dp_l[i-1], prices[i]-low)

        high = prices[day-1]
        for i in range(day-2, -1, -1):
            high = max(high, prices[i])
            dp_r[i] = max(dp_r[i+1], high- prices[i])
        price = 0
        for k in range(day-1):
            price = max(dp_l[k] + dp_r[k+1],price)
            
        
        return max(price, dp_l[day-1], dp_r[0])
                