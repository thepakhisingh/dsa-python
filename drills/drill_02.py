"""
DRILL 2 — Dicts, sets, tuples

Read lessons/02_dicts_sets_tuples.py first.
Check your work:   python check.py 2
"""


def char_frequency(s):
    """
    Return a dict mapping each character to how many times it appears.

    char_frequency("hello")  ->  {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    char_frequency("")       ->  {}

    Do this WITHOUT Counter. You'll use Counter in drill 5; right now the
    point is that you can build it yourself.
    """
    pass  # TODO


def two_sum(nums, target):
    """
    Return the two indices [i, j] with i < j such that nums[i] + nums[j] == target.
    Exactly one solution exists. Return [] if somehow none does.

    two_sum([2, 7, 11, 15], 9)  ->  [0, 1]
    two_sum([3, 2, 4], 6)       ->  [1, 2]

    Must be O(n). Two nested loops will pass the tests but you're cheating
    yourself — this is THE hashmap problem.
    """
    pass  # TODO


def common_elements(a, b):
    """
    Return a SORTED list of values that appear in both lists, no duplicates.

    common_elements([1, 2, 2, 3], [2, 3, 4])  ->  [2, 3]
    common_elements([1], [2])                 ->  []
    """
    pass  # TODO


def group_by_length(words):
    """
    Return a dict mapping word length -> list of words of that length,
    in the order they appeared in the input.

    group_by_length(["hi", "cat", "to", "dog"])
        ->  {2: ['hi', 'to'], 3: ['cat', 'dog']}
    """
    pass  # TODO


def has_duplicate_within_k(nums, k):
    """
    True if there are two EQUAL values at indices i and j where abs(i - j) <= k.

    has_duplicate_within_k([1, 2, 3, 1], 3)     ->  True
    has_duplicate_within_k([1, 2, 3, 1], 2)     ->  False
    has_duplicate_within_k([1, 0, 1, 1], 1)     ->  True

    Hint: a dict of value -> most recent index.
    """
    pass  # TODO


def unique_paths_visited(moves):
    """
    You start at (0, 0). `moves` is a string of 'U', 'D', 'L', 'R'.
    Return how many DISTINCT coordinates you visit, including the start.

    unique_paths_visited("RRLL")  ->  3   # (0,0), (1,0), (2,0)
    unique_paths_visited("")      ->  1
    unique_paths_visited("UD")    ->  2

    This is why tuples matter: a list can't go in a set, a tuple can.
    """
    pass  # TODO
