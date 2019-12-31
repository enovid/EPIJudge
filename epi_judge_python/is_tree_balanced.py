from test_framework import generic_test
from test_framework import test_utils_deserialization
from binary_tree_with_parent_prototype import BinaryTreeNode
from collections import deque, namedtuple

def is_balanced_binary_tree(tree):
    if not tree: return True
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else 0

    q = deque([tree])
    while q:
        t = q.popleft()
        if abs(height(t.left) - height(t.right)) < 2:
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
        else:
            return False
    return True

def is_balanced_binary_tree(tree):
    BalancedHeightStatus = namedtuple('BalancedHeightStatus', ['is_balanced', 'height'])

    def check_balance(t):
        if not t:
            return BalancedHeightStatus(True, -1)

        left_status = check_balance(t.left)
        if not left_status.is_balanced:
            return BalancedHeightStatus(False, 0)
        right_status = check_balance(t.right)
        if not right_status.is_balanced:
            return BalancedHeightStatus(False, 0)

        balanced = abs(left_status.height - right_status.height) <= 1
        if not balanced:
            return BalancedHeightStatus(False, 0)
        return BalancedHeightStatus(True, 1 + max(left_status.height, right_status.height))

    return check_balance(tree).is_balanced

if __name__ == '__main__':
    # s = ["-4", "-5", "5", "-10", "-2", "6", "11", "null", "-9", "-2", "12"]
    # t = test_utils_deserialization.build_binary_tree(s, lambda x: str(x), BinaryTreeNode)
    # result = is_balanced_binary_tree(t)
    # print(result)

    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
