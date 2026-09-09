"""
DRILL 4 — Strings

Read lessons/04_strings.py first.
Check your work:   python check.py 4
"""


def is_palindrome(s):
    """
    True if s reads the same both ways, ignoring case and any character
    that isn't a letter or digit.

    is_palindrome("A man, a plan, a canal: Panama")  ->  True
    is_palindrome("race a car")                      ->  False
    is_palindrome("")                                ->  True

    Solve it with two pointers and O(1) extra space, not by building a
    cleaned copy. The lesson shows both — write the harder one from memory.
    """
    pass  # TODO


def reverse_words(s):
    """
    Reverse the ORDER of words. Collapse runs of whitespace. No leading or
    trailing spaces in the result.

    reverse_words("the sky  is blue")   ->  "blue is sky the"
    reverse_words("  hello world  ")    ->  "world hello"
    reverse_words("   ")                ->  ""
    """
    pass  # TODO


def are_anagrams(a, b):
    """
    True if a and b use exactly the same letters with the same counts.
    Case-sensitive. No Counter — build the counts yourself.

    are_anagrams("listen", "silent")  ->  True
    are_anagrams("rat", "car")        ->  False
    are_anagrams("a", "ab")           ->  False
    """
    pass  # TODO


def longest_common_prefix(words):
    """
    The longest string that starts every word in the list.

    longest_common_prefix(["flower", "flow", "flight"])  ->  "fl"
    longest_common_prefix(["dog", "car"])                ->  ""
    longest_common_prefix([])                            ->  ""
    longest_common_prefix(["single"])                    ->  "single"
    """
    pass  # TODO


def compress(s):
    """
    Run-length encode. A run of length 1 keeps no number.
    If the encoded form isn't SHORTER than the original, return the original.

    compress("aaabbc")   ->  "a3b2c"
    compress("abc")      ->  "abc"      # encoding would be the same length
    compress("aabb")     ->  "aabb"     # "a2b2" is the same length, so no gain
    compress("")         ->  ""

    Build the result with a list and "".join, not with += in a loop.
    """
    pass  # TODO


def first_non_repeating(s):
    """
    The first character that appears exactly once. Return "" if there is none.

    first_non_repeating("swiss")   ->  "w"
    first_non_repeating("aabb")    ->  ""
    first_non_repeating("x")       ->  "x"

    Two passes. One to count, one to find. Don't do it in one nested pass.
    """
    pass  # TODO
