from test_framework import generic_test, test_utils





def permutations(A):
    results = [[]]
    for i in range(len(A)):
        new_results = []
        for partial_seq in results:
            rest = A[:i]+A[i+1:]
            for other in rest:
                new_results.append(partial_seq + [other])
        results = new_results
    return results

def permutations(A):
    def permute(rest, path):
        if not rest:
            results.append(path)
        for i in range(len(rest)):
            rv = permute(rest[:i] + rest[i+1:], path + [rest[i]])
    results = []
    permute(A, [])
    return results 

def permutations(A):
    if not A or len(A) == 1:
        return [A]
    results = []
    for i in range(len(A)):
        for seq in permutations(A[:i]+A[i+1:]):
            results.append([A[i]] + seq)
    return results

def permutations(A):
    def directed_permutations(i):
        if i == len(A) - 1:
            results.append(A.copy())
            return
        # Try every possibility for A[i]
        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            # Generate all permutations for A[i + 1:]
            directed_permutations(i + 1)
            A[i], A[j] = A[j], A[i]

    results = []
    directed_permutations(0)
    return results



if __name__ == '__main__':
    print(permutations([0,1]), '\n')
    print(permutations([1,2,3]), '\n')
    # exit(
        # generic_test.generic_test_main("permutations.py", 'permutations.tsv',
                                       # permutations,
                                       # test_utils.unordered_compare))
