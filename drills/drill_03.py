"""
DRILL 3 — Comprehensions and sorting

Read lessons/03_comprehensions_and_sorting.py first.
Check your work:   python check.py 3

Every function here should be short. If you're writing 10 lines, there's a
comprehension or a key= function waiting to replace it.
"""


def squares_of_evens(nums):
    """
    Squares of the even numbers, in order.

    squares_of_evens([1, 2, 3, 4])  ->  [4, 16]

    One line.
    """
    pass  # TODO


def invert_dict(d):
    """
    Swap keys and values. Assume values are unique and hashable.

    invert_dict({'a': 1, 'b': 2})  ->  {1: 'a', 2: 'b'}
    """
    pass  # TODO


def sort_by_length_then_alpha(words):
    """
    Sort by length ascending; ties broken alphabetically.

    sort_by_length_then_alpha(["pear", "fig", "kiwi", "date"])
        ->  ['fig', 'date', 'kiwi', 'pear']
    """
    pass  # TODO


def sort_by_frequency(nums):
    """
    Sort by frequency DESCENDING. Equal frequencies: smaller value first.
    Every occurrence is kept.

    sort_by_frequency([4, 4, 1, 2, 2, 2, 3])  ->  [2, 2, 2, 4, 4, 1, 3]
    sort_by_frequency([1, 2])                 ->  [1, 2]

    Hint: build a frequency dict, then sort with a tuple key. Remember the
    negation trick for mixing ascending and descending.
    """
    pass  # TODO


def top_k_frequent(words, k):
    """
    The k most frequent words. Ties broken alphabetically. Returned in
    descending frequency order.

    top_k_frequent(["a", "b", "a", "c", "b", "a"], 2)  ->  ['a', 'b']
    top_k_frequent(["z", "y"], 2)                      ->  ['y', 'z']
    """
    pass  # TODO


def sort_people(people):
    """
    people is a list of (name, age) tuples.
    Sort by age DESCENDING, then name ASCENDING.

    sort_people([("ana", 31), ("bo", 24), ("cy", 31)])
        ->  [('ana', 31), ('cy', 31), ('bo', 24)]
    """
    pass  # TODO
