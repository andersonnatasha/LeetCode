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

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.
    >>> twoSum([2,7,11,15],9)
    [0, 1]
    >>> twoSum([3,2,4],6)
    [1, 2]
    >>> twoSum([3,3],6)
    [0, 1]
    """

    if len(nums) == 2:
        return [0, 1]

    def find_sum(nums, target, i):

        j = i + 1

        while j < len(nums):
            if nums[i] + nums[j] == target:
                return [i, j]
            else:
                j += 1

        return find_sum(nums, target, i+1)

    return find_sum(nums, target, 0)


if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED!")
    print()
