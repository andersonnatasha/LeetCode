import doctest


def reverse(x):
    """Given a 32-bit signed integer, reverse digits of an integer.
    Assume we are dealing with an environment that could only store
    integers within the 32-bit signed integer range: [−231,  231 − 1].
    For the purpose of this problem, assume that your function returns
    0 when the reversed integer overflows.
        >>> reverse(-2147483648)
        0
        >>> reverse(123)
        321
        >>> reverse(-123)
        -321
        """

    x_as_string = str(x)
    x_as_reversed_string = ""

    if x_as_string[0] == "-":
        x_as_reversed_string = x_as_reversed_string + "-"
        x_as_reversed_string = x_as_reversed_string + x_as_string[-1:0:-1]
    else:
        x_as_reversed_string = x_as_reversed_string + x_as_string[::-1]

    if (-2)**31 > int(x_as_reversed_string) or int(x_as_reversed_string) > (2**31) - 1:
        return 0

    return int(x_as_reversed_string)


if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED!")
    print()
