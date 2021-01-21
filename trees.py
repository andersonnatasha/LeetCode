def isSymmetric(root):
    """Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center)."""

    if not root:
        return True

    def check_balance(node_1, node_2):
        if not node_1 and not node_2:
            return True
        if not node_1 or not node_2:
            return False
        if node_1.val != node_2.val:
            print(node_1.val, node_2.val)
            return False
        else:
            return check_balance(node_1.left, node_2.right) and check_balance(node_1.right, node_2.left)

    return check_balance(root.left, root.right)
