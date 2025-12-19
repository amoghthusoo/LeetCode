class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        
        prices.sort()
        _sum = prices[0] + prices[1]

        if(_sum > money):
            return money
        else:
            return money - _sum