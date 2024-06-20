class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        cost=0
        count=0

        for i in range(len(prices)):
            cost+=prices[i]
            count+=1
            if cost==money and count==2:
                return 0
            elif(cost<money and count==2):
                return money-cost
            
        return money
