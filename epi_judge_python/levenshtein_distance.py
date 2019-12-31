from test_framework import generic_test
from collections import defaultdict, Counter


def levenshtein_distance(A, B):
    def compute_distance_between_prefixes(A_idx, B_idx):
        if A_idx < 0:
            return B_idx + 1 # A is empty so add all of B's characters.
        elif B_idx < 0:
            return A_idx + 1 # B is empty so delete all of A's characters.
        if distance_between_prefixes[A_idx][B_idx] == -1:
            if A[A_idx] == B[B_idx]:
                distance_between_prefixes[A_idx][B_idx] = compute_distance_between_prefixes(A_idx - 1, B_idx - 1)
            else:
                substitute_last                         = compute_distance_between_prefixes(A_idx - 1, B_idx - 1)
                add_last                                = compute_distance_between_prefixes(A_idx - 1, B_idx)
                delete_last                             = compute_distance_between_prefixes(A_idx, B_idx - 1)
                distance_between_prefixes[A_idx][B_idx] = min(substitute_last, add_last, delete_last) + 1
        return distance_between_prefixes[A_idx][B_idx]

    distance_between_prefixes = [[-1] * len(B) for _ in A]
    return compute_distance_between_prefixes(len(A) - 1, len(B) - 1)


def levenshtein_distance(A, B):
    def pr(g, align_width=3):
        top_row = '    ' +\
                  ''.join([' '] * align_width) +\
                  ''.join(f'{s:^{align_width}}' for s in A)
        print(top_row)
        divider = ''.join(['-'] * len(top_row))
        print(divider)
        for i, row in enumerate(g):
            letter = f'{B[i-1]} | ' if i > 0 else '  | '
            fmt_row = ''.join(f'{s:^{align_width}}' for s in row)
            print(letter + fmt_row)
        print()
    dp = [[0] * (len(A)+1) for _ in range(len(B)+1)]
    dp[0] = list(range(len(A)+1))
    for i, row in enumerate(dp): row[0] = i

    pr(dp)

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if A[j-1] == B[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        pr(dp)

    pr(dp)
    return dp[-1][-1]









if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))

# a, b = len(A), len(B)
# lev_distance = E(A[0:a-1], B[0:b-1])

# if A[-1] == B[-1]:
    # E(A[0:a-1], B[0:b-1]) = E(A[0:a-2], B[0:b-2])
# else:
    # E(A[0:a-1], B[0:b-1]) = 1 + min(E(A[0:a-2], B[0:b-2]),
                                    # E(A[0:a-1], B[0:b-2]),
                                    # E(A[0:a-2], B[0:b-1]))



