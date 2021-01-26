tribonacci_cache = {}


def tribonacci(n):
    """The Tribonacci sequence Tn is defined as follows:

    T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
    Given n, return the value of Tn.
        >>> tribonacci(25)
        1389537
        >>> tribonacci(37)
        2082876103
    """
    # Base case T_0 = 0, T_1 = 1, T_2 = 1
    if n == 0:
        return 0

    if n == 1:
        return 1

    if n == 2:
        return 1

    else:
        if n not in tribonacci_cache:
            tribonacci_cache[n] = tribonacci(
                n-3) + tribonacci(n-2) + tribonacci(n-1)
        return tribonacci_cache[n]


def countAndSay(n):
    """The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

        countAndSay(1) = "1"
        countAndSay(n) is the way you would "say" the digit
        string from countAndSay(n-1), which is then converted into a different digit string.
        To determine how you "say" a digit string, split it into the minimal
        number of groups so that each group is a contiguous section all of the same character.
        Then for each group, say the number of characters, then say the character.
        To convert the saying into a digit string, replace the counts with a number and
        concatenate every saying.

        Given a positive integer n, return the nth term of the count-and-say sequence.
        >>> countAndSay(1)
        '1'
        >>> countAndSay(4)
        '1211'
        >>> countAndSay(10)
        '13211311123113112211'
        """

    if n == 1:
        return "1"

    def computing(string):
        say = string[0]
        count = 1
        countAndSay = ""

        if len(string) > 1:
            for i in range(len(string)-1):
                if string[i] == string[i + 1]:
                    count += 1
                else:
                    countAndSay += str(count) + say
                    count = 1
                    say = string[i+1]
                    if i+1 == len(string)-1:
                        countAndSay += "1" + say
                        return countAndSay
        return countAndSay + str(count) + say

    return computing(countAndSay(n-1))


def removeDuplicates(nums):
    """Given a sorted array nums, remove the duplicates in-place such
    that each element appears only once and returns the new length.

    >>> removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    5
    >>> removeDuplicates([])
    0
    >>> removeDuplicates([1])
    1
    >>> removeDuplicates([1,1,2])
    2
   """

    if len(nums) == 0 or len(nums) == 1:
        return len(nums)

    def find_duplicates(nums_2, i):

        if i == len(nums_2)-1:
            return len(nums_2)

        elif nums_2[i] == nums_2[i+1]:
            nums_2.pop(i+1)
            return find_duplicates(nums_2, i)

        else:
            return find_duplicates(nums_2, i+1)

    return find_duplicates(nums, 0)


def twoSum(nums, target):
    """Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.

    You can return the answer in any order.
    >>> twoSum([2,7,11,15],9)
    [0, 1]
    >>> twoSum([3,2,4],6)
    [1, 2]
    >>> twoSum([3,3],6)
    [0, 1]
    >>> twoSum([3,3,1],7)
    'No matches'

    """

    if len(nums) == 2:
        return [0, 1]

    def find_sum(nums, target, i):

        j = i + 1

        if j == len(nums):
            return "No matches"

        while j < len(nums):
            if nums[i] + nums[j] == target:
                return [i, j]
            else:
                j += 1

        return find_sum(nums, target, i+1)

    return find_sum(nums, target, 0)
    # runtime of O(n^2)


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
            return False
        else:
            return check_balance(node_1.left, node_2.right) and check_balance(node_1.right, node_2.left)

    return check_balance(root.left, root.right)


def isSameTree(p, q):
    """Given the roots of two binary trees p and q,
    write a function to check if they are the same or not.

    Two binary trees are considered the same if they are structurally identical,
    and the nodes have the same value."""

    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    else:
        return isSameTree(p.right, q.right) and isSameTree(p.left, q.left)
    # Time complexity = O(N)


def searchBST(root, val):
    """You are given the root of a binary search tree (BST) and an integer val.
    Find the node in the BST that the node's value equals val and return the
    subtree rooted with that node. If such a node does not exist, return null."""

    if root:
        if root.val == val:
            return root
        elif root.val < val:
            return searchBST(root.right, val)
        else:
            return searchBST(root.left, val)

    return


def sumOfLeftLeaves(root):
    """Find the sum of all left leaves in a given binary tree."""

    sum = 0

    if not root:
        return 0

    if root.left and (not root.left.left and not root.left.right):
        sum += root.left.val

    return sum + sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right)


if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED!")
    print()
