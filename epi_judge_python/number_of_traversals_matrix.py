from test_framework import generic_test


def number_of_ways(n, m):
    def pr(g):
        for i, row in enumerate(g):
            print(''.join(f'{s:^2}' for s in row))
        print()

    dp = [[0] * m for _ in range(n)] 
    dp[0][0] = 1
    # pr(dp)
    for i in range(n):
        for j in range(m):
            for di, dj in [(-1,0),(0,-1)]:
                row, col = i+di, j+dj
                if 0 <= row < n and 0 <= col < m:
                    dp[i][j] += dp[row][col]
    return dp[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
