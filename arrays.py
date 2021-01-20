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

    # length check to see if there are cookies and if not return 0
    if len(s) == 0:
        return 0

    # put the lists in order
    greed_sorted = sorted(g)   # m log m
    cookies_sorted = sorted(s)  # n log n

    content_children = 0

    while cookies_sorted and greed_sorted:
        if greed_sorted[0] <= cookies_sorted[0]:
            content_children += 1
            greed_sorted.pop(0)
            cookies_sorted.pop(0)
        else:
            cookies_sorted.pop(0)
    return content_children

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

    nums_as_dict = {}

    for index, num in enumerate(nums):
        difference = target - num
        if difference in nums_as_dict.values() and index != nums.index(difference):
            return [nums.index(difference), index]
        nums_as_dict[index] = num

    return "No matches"

    # runtime of O(n)


if __name__ == '__main__':
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print('ALL TESTS PASSED')
    print()
