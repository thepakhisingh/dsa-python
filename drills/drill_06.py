"""
DRILL 6 — heapq, bisect, itertools, functools

Read lessons/06_heapq_bisect_itertools.py first.
Check your work:   python check.py 6

Last drill of Phase 0. After this, the language is out of your way.
"""

import heapq
import bisect
from functools import cache


def k_largest(nums, k):
    """
    The k largest values, DESCENDING. If k >= len(nums), return all of them sorted.

    k_largest([7, 2, 9, 4], 2)  ->  [9, 7]
    k_largest([1], 5)           ->  [1]
    k_largest([], 3)            ->  []

    Do it with a size-k min-heap in O(n log k), not by sorting everything.
    Then check yourself against heapq.nlargest.
    """
    pass  # TODO


def merge_sorted_lists(lists):
    """
    Merge k already-sorted lists into one sorted list.

    merge_sorted_lists([[1, 4, 5], [1, 3], [2, 6]])  ->  [1, 1, 2, 3, 4, 5, 6]
    merge_sorted_lists([])                            ->  []
    merge_sorted_lists([[], [1]])                     ->  [1]

    Concatenating and sorting passes the tests but misses the point.
    Use a heap holding (value, list_index, position) — O(n log k).
    This is LeetCode 23, a genuine Google favourite.
    """
    pass  # TODO


def count_in_range(sorted_nums, lo, hi):
    """
    How many values in a SORTED list fall in [lo, hi], inclusive both ends.

    count_in_range([1, 3, 3, 5, 8], 3, 5)   ->  3
    count_in_range([1, 3, 3, 5, 8], 4, 4)   ->  0
    count_in_range([], 1, 5)                ->  0

    Two bisect calls. O(log n). No loop.
    """
    pass  # TODO


def insert_position(sorted_nums, target):
    """
    The index where target is, or where it would be inserted to keep order.
    If target already appears, return the index of its FIRST occurrence.

    insert_position([1, 3, 5, 6], 5)  ->  2
    insert_position([1, 3, 5, 6], 2)  ->  1
    insert_position([1, 3, 5, 6], 7)  ->  4
    insert_position([], 1)            ->  0

    Use bisect to pass. Then write it AGAIN by hand as a while-loop binary
    search and make sure both agree. You need the handwritten one for interviews.
    """
    pass  # TODO


def climb_stairs(n):
    """
    You climb 1 or 2 steps at a time. How many distinct ways to reach step n?

    climb_stairs(2)   ->  2      # 1+1, 2
    climb_stairs(3)   ->  3      # 1+1+1, 1+2, 2+1
    climb_stairs(0)   ->  1      # one way: do nothing
    climb_stairs(45)  ->  1836311903

    Write the recursive version with @cache. Without the cache, n=45 will
    hang. This is your first dynamic programming problem — the recurrence is
    the whole answer, memoization just makes it fast.
    """
    pass  # TODO


def coin_change(coins, amount):
    """
    Fewest coins summing to exactly `amount`. Return -1 if impossible.
    You have unlimited coins of each denomination.

    coin_change([1, 5, 11], 15)  ->  3      # 5+5+5, not 11+1+1+1+1
    coin_change([2], 3)          ->  -1
    coin_change([1, 2, 5], 0)    ->  0

    A cached recursion works. Note that greedy (always take the biggest coin)
    gives 5 for the first case — wrong. Understanding WHY greedy fails here
    is more valuable than the code.
    """
    pass  # TODO
