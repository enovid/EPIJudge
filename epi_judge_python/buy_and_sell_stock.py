from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    max_profit = 0
    curr_min = float('inf')
    for i, p in enumerate(prices):
        curr_min = min(p, curr_min)
        max_profit = max(max_profit, p - curr_min)
    return max_profit



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
