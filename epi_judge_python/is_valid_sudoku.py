from test_framework import generic_test


def pr(g):
    for i, row in enumerate(g):
        fmt_row = ''
        for j, num in enumerate(list(row)):
            fmt_row += str(num) + ' '
            if (j+1) % 3 == 0:
                fmt_row += '| '
        print(fmt_row)
        if (i+1) % 3 == 0:
            print(''.join(['-']*len(fmt_row)))
    print()

def is_valid_sudoku(partial_assignment):
    pr(partial_assignment)
    print(partial_assignment)
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
