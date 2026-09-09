"""
DRILL 1 — Lists and slicing

Read lessons/01_lists_and_slicing.py first.

Replace each `pass  # TODO` with your solution.
Check your work:   python check.py 1

Rules for yourself:
  - No looking things up until you've been stuck for 10 minutes.
  - No copying from the lesson file. Type it from memory.
"""


def second_largest(nums):
    """
    Return the second largest DISTINCT value in nums.
    Return None if there aren't two distinct values.

    second_largest([3, 1, 4, 4, 5])  ->  4
    second_largest([2, 2, 2])        ->  None
    second_largest([1])              ->  None

    Bonus once it passes: solve it in one pass, no sorting.
    """
    pass  # TODO


def rotate_right(nums, k):
    """
    Return a NEW list rotated right by k places. Don't modify nums.
    k may be larger than len(nums). k may be 0.

    rotate_right([1, 2, 3, 4, 5], 2)  ->  [4, 5, 1, 2, 3]
    rotate_right([1, 2, 3], 4)        ->  [3, 1, 2]
    rotate_right([], 3)               ->  []

    Hint: slicing does this in one line. Watch out for k % len on an empty list.
    """
    pass  # TODO


def chunk(nums, size):
    """
    Split nums into consecutive chunks of length `size`.
    The final chunk may be shorter.

    chunk([1, 2, 3, 4, 5], 2)  ->  [[1, 2], [3, 4], [5]]
    chunk([1, 2, 3], 5)        ->  [[1, 2, 3]]
    chunk([], 3)               ->  []
    """
    pass  # TODO


def flatten_once(nested):
    """
    Flatten ONE level of nesting.

    flatten_once([[1, 2], [3], [], [4, 5]])  ->  [1, 2, 3, 4, 5]
    flatten_once([[1, [2]], [3]])            ->  [1, [2], 3]
    """
    pass  # TODO


def running_max(nums):
    """
    Return a list where position i holds the maximum of nums[0..i].

    running_max([3, 1, 4, 1, 5])  ->  [3, 3, 4, 4, 5]
    running_max([])               ->  []

    Must be O(n). If you call max() inside the loop, it's O(n^2) — fix that.
    """
    pass  # TODO


def move_zeros(nums):
    """
    Return a NEW list with all zeros moved to the end, other values keeping
    their relative order.

    move_zeros([0, 1, 0, 3, 12])  ->  [1, 3, 12, 0, 0]
    move_zeros([0, 0])            ->  [0, 0]

    This exact problem is LeetCode 283. You'll meet it again.
    """
    pass  # TODO
