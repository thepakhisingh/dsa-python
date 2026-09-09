"""
DRILL 5 — The collections module

Read lessons/05_collections_module.py first.
Check your work:   python check.py 5

This is the drill where the code starts looking like real interview answers.
"""

from collections import deque, Counter, defaultdict


def bfs_shortest_path(graph, start, goal):
    """
    graph is a dict: node -> list of neighbours.
    Return the FEWEST number of edges from start to goal, or -1 if unreachable.
    Distance from a node to itself is 0.

    g = {'a': ['b', 'c'], 'b': ['d'], 'c': ['d'], 'd': [], 'e': []}
    bfs_shortest_path(g, 'a', 'd')  ->  2
    bfs_shortest_path(g, 'a', 'a')  ->  0
    bfs_shortest_path(g, 'a', 'e')  ->  -1

    Use a deque. Mark nodes as seen when you ENQUEUE them.
    Write this from memory — you will write it a hundred more times.
    """
    pass  # TODO


def build_adjacency(edges):
    """
    Turn a list of undirected edges into an adjacency dict.
    Neighbour lists must be SORTED. Return a plain dict, not a defaultdict.

    build_adjacency([("a", "b"), ("a", "c")])
        ->  {'a': ['b', 'c'], 'b': ['a'], 'c': ['a']}
    build_adjacency([])  ->  {}

    Hint: defaultdict(list), then convert at the end with dict(...).
    """
    pass  # TODO


def top_k_common(items, k):
    """
    The k most common items, most frequent first.
    Ties: whichever appeared first in `items` wins.

    top_k_common(["a", "b", "a", "c", "b", "a"], 2)  ->  ['a', 'b']

    Counter.most_common already breaks ties by first-seen order. Use it.
    """
    pass  # TODO


def group_anagrams(words):
    """
    Return a dict: sorted-letters key -> list of words with those letters,
    in input order.

    group_anagrams(["eat", "tea", "tan"])
        ->  {'aet': ['eat', 'tea'], 'ant': ['tan']}
    """
    pass  # TODO


def sliding_window_max(nums, k):
    """
    For every window of size k, the maximum in that window.

    sliding_window_max([1, 3, -1, -3, 5, 3], 3)  ->  [3, 3, 5, 5]
    sliding_window_max([1], 1)                   ->  [1]
    sliding_window_max([], 3)                    ->  []

    Start with the obvious O(n*k) version and make the tests pass.
    THEN come back and do it in O(n) with a monotonic deque holding INDICES
    in decreasing order of value. That second version is LeetCode Hard 239
    and it's worth the struggle.
    """
    pass  # TODO


def is_valid_parentheses(s):
    """
    True if brackets are correctly matched and nested. Characters: ()[]{}

    is_valid_parentheses("([]{})")  ->  True
    is_valid_parentheses("(]")      ->  False
    is_valid_parentheses("(")       ->  False
    is_valid_parentheses("")        ->  True

    A list used as a stack is fine here — you only push and pop from the end.
    """
    pass  # TODO
