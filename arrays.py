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
    # [7,8,9,10]
    cookies_sorted = sorted(s)  # n log n
    # [5,6,7,8]

    # o(n) o(m)
    # max of m,n
    # max of m log m/n log n + max of o(n)/o(m)

    content_children = 0

    while cookies_sorted and greed_sorted:
        if greed_sorted[0] <= cookies_sorted[0]:
            content_children += 1
            greed_sorted.pop(0)
            cookies_sorted.pop(0)
        else:
            cookies_sorted.pop(0)
    return content_children

    # if greed is =< cookie then we can add one to content and then remove the first of both list and add           # one to content
    # look at first in the list and if greed is larger than cookie then break / return content


if __name__ == '__main__':
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print('ALL TESTS PASSED')
    print()
