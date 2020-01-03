from test_framework import generic_test


def pr(g, pad=4):
    row_ind_pad = len(str(len(g)))
    print()
    header = ''.join([' '] * (row_ind_pad + 3)) +\
            ''.join(f'{i:>{pad}}' for i in range(len(g[0])))
    print(header)
    divider = ''.join(['-'] * len(header))
    print(divider)
    for i, row in enumerate(g):
        fmt_row = ''.join(f'{s:>{pad}}' for s in row)
        row_ind = f'{i:>{row_ind_pad}} | '
        print(row_ind + fmt_row)
    print()

from collections import deque
def is_pattern_contained_in_grid(g, pattern):
    N, M = len(g), len(g[0])

    positions = [(i, j, 1) for i in range(N) for j in range(M) if g[i][j] == pattern[0]]
    q = deque(positions)
    seen = set(positions)

    while q:
        row, col, offset = q.popleft()

        if offset > len(pattern)-1: 
            return True

        for i, j in [(row-1,col), (row, col-1), (row, col+1), (row+1, col)]:
            if 0 <= i < N and 0 <= j < M and g[i][j] == pattern[offset]:
                new_position = (i, j, offset + 1)
                if new_position not in seen:
                    q.append(new_position)
                    seen.add(new_position)
                    
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_in_matrix.py",
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
