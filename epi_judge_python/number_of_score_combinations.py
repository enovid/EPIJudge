from test_framework import generic_test
from collections import defaultdict
from icecream import ic

def num_combinations_for_final_score(final_score, individual_play_scores):
    def pr(g):
        align_width = len(str(individual_play_scores))
        scores = ''.join([' ' for _ in range(align_width + 3)]) + \
                 ''.join(f'{i%10:^2}' for i in range(final_score + 1))
        print(scores)
        print(''.join('-' for _ in range(len(scores))))
        for i, row in enumerate(g):
            fmt_row = f'{str(individual_play_scores[:i+1]):>{align_width}} | ' +\
                      ''.join(f'{s:^2}' for s in row)
            print(fmt_row)
        print()
    dp = [[0] * (final_score + 1) for _ in range(len(individual_play_scores))]

    for j in range(final_score+1):
        if j % individual_play_scores[0] == 0:
            dp[0][j] = 1

    for i in range(1, len(dp)):
        for j in range(final_score+1):
            dp[i][j] = dp[i-1][j]
            if j >= individual_play_scores[i]: 
                dp[i][j] += dp[i][j-individual_play_scores[i]]

    return dp[-1][-1]

def num_combinations_for_final_score(final_score, individual_play_scores):
    def pr(g):
        align_width = len(str(individual_play_scores))
        scores = ''.join([' ' for _ in range(align_width + 3)]) + \
                 ''.join(f'{i%10:^2}' for i in range(final_score + 1))
        print(scores)
        print(''.join('-' for _ in range(len(scores))))
        for i, row in enumerate(g):
            fmt_row = f'{str(individual_play_scores[:i+1]):>{align_width}} | ' +\
                      ''.join(f'{s:^2}' for s in row)
            print(fmt_row)
        print()
    num_combinations_for_score = [[1] + [0] * final_score 
                                  for _ in range(len(individual_play_scores))]  

    for i in range(len(individual_play_scores)):
        for j in range(1, final_score + 1):
            with_this_play = (num_combinations_for_score[i][j-individual_play_scores[i]]
                              if j >= individual_play_scores[i] else 0)
            without_this_play = (num_combinations_for_score[i-1][j]
                                 if i-1 >= 0 else 0)
            num_combinations_for_score[i][j] = with_this_play + without_this_play

    return num_combinations_for_score[-1][-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
