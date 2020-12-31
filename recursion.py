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
    cache = {}
    # Base case T_0 = 0, T_1 = 1, T_2 = 1
    if n == 0:
        return 0

    if n == 1:
        return 1

    if n == 2:
        return 1

    else:
        if n not in cache:
            cache[n] = tribonacci(
                n-3) + tribonacci(n-2) + tribonacci(n-1)
        return cache[n]


if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED!")
    print()
