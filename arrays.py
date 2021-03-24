def findContentChildren(g, s):
    """Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
    Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with;
    and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content.
    Your goal is to maximize the number of your content children and output the maximum number.
    >>> findContentChildren([10,9,8,7], [5,6,7,8])
    2
    >>> findContentChildren([1,2,3], [1,1])
    1
    >>> findContentChildren([1,2], [1,2,3])
    2
    >>> findContentChildren([1,9,7,2], [])
    0
    """

    count = 0

    g = sorted(g)
    s = sorted(s)

    pointer_g = len(g) - 1
    pointer_s = len(s) - 1

    while pointer_g >= 0 and pointer_s >= 0:
        if s[pointer_s] >= g[pointer_g]:
            count += 1
            pointer_s -= 1
            pointer_g -= 1
        else:
            pointer_g -= 1

    return count

   # time complexity max of m log m/n log n + max of o(n)/o(m)


def removeElement(nums, val):
    """Given an array nums and a value val,
     remove all instances of that value in-place and return the new length.
    Do not allocate extra space for another array,
    you must do this by modifying the input array in-place with O(1) extra memory.
    The order of elements can be changed.
    It doesn't matter what you leave beyond the new length.
    >>> removeElement([], 12)
    0
    >>> removeElement([3,2,2,3], 3)
    2
    >>> removeElement([0,1,2,2,3,0,4,2], 2)
    5

    """

    i = 0

    while val in nums:
        if nums[i] == val:
            nums[i:i+1] = []
        else:
            i += 1
    return len(nums)


def findDisappearedNumbers(nums):
    """Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
    some elements appear twice and others appear once.
    Find all the elements of [1, n] inclusive that do not appear in this array.
    >>> findDisappearedNumbers([4,3,2,7,8,2,3,1])
    [5, 6]
    >>> findDisappearedNumbers([1])
    []
    >>> findDisappearedNumbers([1,1,1,1,1,1,1,1])
    [2, 3, 4, 5, 6, 7, 8]
    >>> findDisappearedNumbers([])
    []
    """

    n = len(nums)
    range_set = set()

    for i in range(len(nums)):  # o(n)
        range_set.add(i+1)
    for i in range(len(nums)):  # o(n)
        if nums[i] in range_set:  # o(1)
            range_set.remove(nums[i])  # o(1)
    return list(range_set)  # o(n)


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

    nums_as_dict = {}  # O(1)

    for index, num in enumerate(nums):
        difference = target - num  # O(1) * N --> O(N)
        if difference in nums_as_dict.values() and index != nums.index(difference):  # O(1) * N ---> O(N)
            return [nums.index(difference), index]  # (1)
        nums_as_dict[index] = num  # O(1) * N-1 --> O(N)

    return "No matches"  # O(1)

    # runtime of O(n)


def lengthOfLastWord(s):
    """Given a string s consists of some words separated by spaces,
    return the length of the last word in the string.
    If the last word does not exist, return 0.
    A word is a maximal substring consisting of non-space characters only.
    >>> lengthOfLastWord('Hello World')
    5
    >>> lengthOfLastWord('a  ')
    1
    >>> lengthOfLastWord('   ')
    0
    """

    s = s.split(" ")

    end_pointer = -1

    while -(end_pointer) <= len(s):
        if len(s[end_pointer]) != 0:
            return len(s[end_pointer])
        end_pointer -= 1

    return 0


def rotate(nums, k):
    """
    Given an array, rotate the array to the right by k steps,
    where k is non-negative.
    >>> rotate([1,2,3,4,5,6,7], 3)
    [5, 6, 7, 1, 2, 3, 4]
    >>> rotate([1,2,3,4,5,6,7], 20)
    [2, 3, 4, 5, 6, 7, 1]
    """

    k %= len(nums)

    for i in range(k):
        number = nums.pop()
        nums.insert(0, number)

    return nums


def shuffle(nums, n):
    """Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

    Return the array in the form [x1,y1,x2,y2,...,xn,yn].

    >>> shuffle([2,5,1,3,4,7], 3)
    [2, 3, 5, 4, 1, 7]

    >>> shuffle([2,5,1,3,4,7], 3)
    [2, 3, 5, 4, 1, 7]
    """

    first_half = nums[:len(nums)//2]
    second_half = nums[len(nums)//2:]
    new_list = []

    for i, num in enumerate(first_half):
        new_list.append(first_half[i])
        new_list.append(second_half[i])

    return new_list


def checkIfExist(arr):
    """Given an array arr of integers,
    check if there exists two integers N and M
    such that N is the double of M ( i.e. N = 2 * M).
    >>> checkIfExist([10,2,5,3])
    True
    >>> checkIfExist([7,1,14,11])
    True
    >>> checkIfExist([3,1,7,11])
    False
    """

    doubles = {}

    arr = sorted(arr)

    for i, num in enumerate(arr):
        doubles[i] = num * 2

    for i, num in enumerate(arr):
        for key, value in doubles.items():
            if num == value and i != key:
                return True
    return False


def sumOddLengthSubarrays(arr):
    """Given an array of positive integers arr,
    calculate the sum of all possible odd-length subarrays.

    A subarray is a contiguous subsequence of the array.
    Return the sum of all odd-length subarrays of arr.

    >>> sumOddLengthSubarrays([1,4,2,5,3])
    58
    >>> sumOddLengthSubarrays([1,2])
    3
    >>> sumOddLengthSubarrays([10,11,12])
    66

    """

    ans = 0

    for i in range(1, len(arr)+1):
        if i % 2 != 0:
            ans += sum([sum(x) for x in [arr[j:j+i]
                                         for j in range(len(arr) - (i-1))]])

    return ans


def countSubstrings(s):
    """Given a string, your task is to count how many palindromic substrings in this string.

    The substrings with different start indexes or end indexes are counted as different
    substrings even they consist of same characters.

    >>> countSubstrings("abc")
    3
    >>> countSubstrings("aaa")
    6
    >>> countSubstrings("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    4656

    """

    def is_pal(s):
        start = 0
        end = len(s) - 1

        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    substrings = []
    count = 0
    seen = set()

    for i in range(len(s)):
        substrings.extend([s[j:j+(i+1)] for j in range(len(s) - (i))])

    for substring in substrings:
        if substring in seen:
            count += 1
            continue
        if is_pal(substring) == True:
            count += 1
            seen.add(substring)

    return count


def generate(numRows):
    """Given an integer numRows, return the first numRows of Pascal's triangle.(numRows will be at least 1)
    >>> generate(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    >>> generate(1)
    [[1]]
    """

    pascal = []

    for i in range(numRows):
        if i == 0:
            array = [i + 1]
            pascal.append(array)
            continue
        else:
            array = [0] + array + [0]
            array = [sum(array[i:i+2]) for i in range(len(array)-1)]
            pascal.append(array)
    return pascal


def getRow(rowIndex):
    """Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
    >>> getRow(3)
    [1, 3, 3, 1]
    >>> getRow(0)
    [1]
    >>> getRow(1)
    [1, 1]

    """

    for i in range(rowIndex+1):
        if i == 0:
            array = [1]
        else:
            array = [0] + array + [0]
            array = [sum(array[i:i+2]) for i in range(len(array)-1)]
    return array


if __name__ == '__main__':
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print('ALL TESTS PASSED')
    print()
