# stock_prices = [10, 7, 5, 8, 11, 9]

stock_prices = [5,4,3,2,1]



# Returns 6 (buying for $5 and selling for $11)
def apple_stock(arr):
    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    min_buy = arr[0]
    curr_best = arr[1] - min_buy

    for i in range(1,len(arr)-1):
        min_buy = min(min_buy,arr[i])
        curr_profit = arr[i+1]-min_buy
        curr_best = max(curr_best, curr_profit)
    return curr_best


print(apple_stock(stock_prices))
