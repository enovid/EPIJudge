import collections
import functools
from icecream import ic
from collections import deque, defaultdict

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))

def pr(dp, pad=4):
    row_ind_pad = len(str(len(dp)))
    header = ''.join([' '] * (row_ind_pad+3)) + \
             ''.join(f'{s%10:>{pad}}' for s in range(len(dp[0])))
    divider = ''.join(['-']*len(header))
    print(header)
    print(divider)
    for i, row in enumerate(dp):
        row_fmt = ''.join(f'{s:>{pad}}' for s in row)
        row_ind = f'{i:>{row_ind_pad}} | ' 
        print(row_ind + row_fmt)
    print()

def optimum_subject_to_capacity1(items, capacity):
    dp = [[-1] * (capacity+1) for _ in range(len(items))]

    def knapsack(i, capacity):
        if i < 0:
            return 0
        if dp[i][capacity] > -1:
            return dp[i][capacity]
        with_current = without_current = 0
        if items[i].weight <= capacity:
            with_current    = knapsack(i-1, capacity-items[i].weight) + items[i].value
        without_current = knapsack(i-1, capacity)
        dp[i][capacity] = max(with_current, without_current)
        return dp[i][capacity]

    result = knapsack(len(items)-1, capacity)
    pr(dp)
    return result


def optimum_subject_to_capacity(items, capacity):
    dp = [[0] * (capacity+1) for _ in range(len(items)+1)]
    # pr(dp)
    for i in range(1,len(dp)):         # items[0:i]
        for j in range(1, len(dp[0])): # capacities [1..j]
            dp[i][j] = dp[i-1][j]      # max value without current item
            if j >= items[i-1].weight: # max value with current item
                dp[i][j] = max(dp[i][j],
                               items[i-1].value + dp[i-1][j-items[i-1].weight])  
    # pr(dp)
    return dp[-1][-1]




@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("knapsack.py", "knapsack.tsv",
                                       optimum_subject_to_capacity_wrapper))
