def romanToInt(s):
    """Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    For example, 2 is written as II in Roman numeral, just two one's added together.
    12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right.
    However, the numeral for four is not IIII. Instead, the number four is written as IV.
    Because the one is before the five we subtract it making four.
    The same principle applies to the number nine, which is written as IX.
    There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given a roman numeral, convert it to an integer.

    >>> romanToInt("MCMXCIV")
    1994
    >>> romanToInt("I")
    1
    >>> romanToInt("LVIII")
    58

    """

    roman_to_int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    value = 0

    if len(s) == 1:
        return roman_to_int[s]

    # Otherwise, check two values at once
    i = 0
    while i < len(s)-1:
        # Check if first > second
        if roman_to_int[s[i]] >= roman_to_int[s[i+1]]:
            # if so, add value of first to value
            value += roman_to_int[s[i]]
            i += 1
            if i == len(s)-1:
                value += roman_to_int[s[i]]
        else:
            # if not then value of second minus value of first = value add 2 to [i]
            value += (roman_to_int[s[i+1]] - roman_to_int[s[i]])
            i += 2
            if i == len(s)-1:
                value += roman_to_int[s[i]]
    return value


if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED!")
    print()
