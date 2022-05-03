

def max_profit(prices):
    if len(prices) < 2:
        return 0
    
    maxprofit, minstock = float("-inf"), prices[0]
    for price in prices:
        maxprofit = max(maxprofit, price - minstock)
        minstock = min(price, minstock)
        
    return maxprofit


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    
    ans = max_profit(prices)

    ans