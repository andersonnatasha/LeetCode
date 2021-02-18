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


def isValid(s):
    """Given a string s containing just the characters
    '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    >>> isValid("()")
    True
    >>> isValid("((")
    False
    >>> isValid("[{()}]")
    True
    >>> isValid("(")
    False
    """

    # dictionary that had the pairs
    pairs = {"(": ")", "{": "}", "[": "]"}

    # if the first character isn't opening brace or the len of s if odd, return False
    if s[0] not in pairs.keys() or len(s) % 2 != 0:
        return False

    # store the opening braces
    openings = []

    for i in range(len(s)):
        # if the character is a key in pairs append to opens
        if s[i] in pairs.keys():
            openings.append(s[i])
        # else, must be a value, so check if the last item in openings is a match
        else:
            # if openings is not empty and current character == the value for the dictionary key
            if openings and (s[i] == pairs[openings[-1]]):
                openings.pop()
            else:
                return False

    return not openings


def reverseString(s):
    """ Do not return anything, modify s in-place instead.

    >>> reverseString(['h','e','l','l','o'])
    ['o', 'l', 'l', 'e', 'h']
    >>> reverseString(["H","a","n","n","a","h"])
    ['h', 'a', 'n', 'n', 'a', 'H']
    """

    i = 0
    j = len(s) - 1
    while j >= i:
        s[i], s[j] = s[j], s[i]
        j -= 1
        i += 1

    return s


def isSubsequence(s, t):
    """Given two strings s and t, check if s is a subsequence of t.
    A subsequence of a string is a new string that is formed from the original string by deleting some
    (can be none) of the characters without disturbing the relative positions of the remaining characters.
    (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

    >>> isSubsequence("abc", "ahbgdc")
    True
    >>> isSubsequence("abx", "ahbgdc")
    False
    >>> isSubsequence("aa", "ba")
    False
    """

    s_pointer = 0
    t_pointer = 0

    while s_pointer < len(s) and t_pointer < len(t):
        if s[s_pointer] == t[t_pointer]:
            s_pointer += 1
            t_pointer += 1
        else:
            t_pointer += 1

    return s_pointer == len(s)


def defangIPaddr(address):
    """Given a valid (IPv4) IP address, return a defanged version of that IP address.
    A defanged IP address replaces every period "." with "[.]".

    >>> defangIPaddr('1.1.1.1')
    '1[.]1[.]1[.]1'
    """

    return "[.]".join(address.split("."))


def balancedStringSplit(s):
    """Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

    Given a balanced string s, split it in the maximum amount of balanced strings.

    Return the maximum amount of split balanced strings.
    >>> balancedStringSplit("RLRRLLRLRL")
    4
    >>> balancedStringSplit("RLLLLRRRLR")
    3
    >>> balancedStringSplit("LLLLRRRR")
    1
    >>> balancedStringSplit("RLRRRLLRLL")
    2

    """
    num_balanced_strs = 0
    pairs = {"R": "L", "L": "R"}

    here = 0
    explore = 0

    while here < len(s) - 1:
        pair = pairs[s[here]]
        if s[explore] == pair:
            if s[here:explore + 1].count('L') == s[here:explore + 1].count('R'):
                num_balanced_strs += 1
                here = explore + 1
                explore = here + 1
                continue
        explore += 1

    return num_balanced_strs


def halvesAreAlike(s):
    """You are given a string s of even length.
    Split this string into two halves of equal lengths,
    and let a be the first half and b be the second half.

    Two strings are alike if they have the same number of vowels
    ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U').
    Notice that s contains uppercase and lowercase letters.

    Return true if a and b are alike. Otherwise, return false

    >>> halvesAreAlike("book")
    True
    >>> halvesAreAlike("textbook")
    False
    >>> halvesAreAlike("MerryChristmas")
    False
    >>> halvesAreAlike("AbCdEfGh")
    True
    """

    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

    a = s[:(len(s)//2)]
    b = s[(len(s)//2):]

    a_count = 0
    b_count = 0

    for i in range(len(a)):
        if a[i] in vowels:
            a_count += 1
        if b[i] in vowels:
            b_count += 1

    return a_count == b_count


def countConsistentStrings(allowed, words):
    """You are given a string allowed consisting of distinct characters and an array of strings words.
    A string is consistent if all characters in the string appear in the string allowed.

    Return the number of consistent strings in the array words.

    >>> countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"])
    2
    >>> countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"])
    7
    >>> countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"])
    4
    """

    allowed = set(allowed)

    count_ = 0

    for word in words:
        word = set(word)
        if len((word - allowed)) == 0:
            count_ += 1

    return count_


def largeGroupPositions(s):
    """In a string s of lowercase letters, these letters form consecutive groups of the same character.

        For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

        A group is identified by an interval [start, end], where start and end denote the start and end
        indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].

        A group is considered large if it has 3 or more characters.

        Return the intervals of every large group sorted in increasing order by start index.

        >>> largeGroupPositions("abbxxxxzzy")
        [[3, 6]]
        >>> largeGroupPositions("abc")
        []
        >>> largeGroupPositions("abcdddeeeeaabbbcd")
        [[3, 5], [6, 9], [12, 14]]
        >>> largeGroupPositions("aba")
        []
        >>> largeGroupPositions("aaa")
        [[0, 2]]
        """

    start = 0
    slider = 0
    ans = []

    while start < len(s) - 1:

        while (slider <= len(s) - 1) and s[start] == s[slider]:
            slider += 1

        if len(s[start:slider]) >= 3:
            ans.append([start, slider - 1])

        start = slider

    return ans


def lengthOfLongestSubstring(s):
    """Given a string s, find the length of the longest substring without repeating characters.
    >>> lengthOfLongestSubstring("abcabcbb")
    3
    >>> lengthOfLongestSubstring("bbbbb")
    1
    >>> lengthOfLongestSubstring("pwwkew")
    3
    >>> lengthOfLongestSubstring("")
    0
    """

    # keep track of which letters seen and their index in dict
    seen_letters = {}
    # keep track of longest string len
    longest_substring = 0
    # keep track of substring currently building
    substring = []
    s = list(s)

    for i, letter in enumerate(s):
        # if the letter is not in dict, add it to the substring and add to dic
        if seen_letters.get(letter) == None or seen_letters.get(letter) < seen_letters.get(substring[0]):
            seen_letters[letter] = i
            substring.append(letter)
    # if next letter is in the dict,
        else:
            # check to see if the substrng is longer than the longest substring, if so update longest
            if len(substring) > longest_substring:
                longest_substring = len(substring)
            substring = (s[seen_letters[letter] + 1:i])
            substring.append(letter)
            seen_letters[letter] = i

    if len(substring) > longest_substring:
        longest_substring = len(substring)

    return longest_substring


if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED!")
    print()
