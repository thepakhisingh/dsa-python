"""
LESSON 6 — heapq, bisect, itertools, functools

Run me:  python lessons/06_heapq_bisect_itertools.py

The last of the standard library that earns its place in an interview.
After this, Phase 0 is done and the language stops being the obstacle.
"""

import heapq
import bisect
from itertools import permutations, combinations, product, accumulate
from functools import lru_cache, cache


def section(name):
    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)


# ---------------------------------------------------------------------------
section("1. heapq — a MIN-heap on a plain list")
# ---------------------------------------------------------------------------

h = []
for n in [5, 1, 8, 3]:
    heapq.heappush(h, n)            # O(log n)

print("internal list   ", h, "  <- NOT sorted; only h[0] is guaranteed smallest")
print("peek h[0]       ", h[0], "  <- O(1), doesn't remove")
print("heappop()       ", heapq.heappop(h), "  <- O(log n)")
print("after pop       ", h)

# Turn an existing list into a heap in O(n):
nums = [9, 4, 7, 1]
heapq.heapify(nums)
print("heapify         ", nums)


# ---------------------------------------------------------------------------
section("2. There is no max-heap. Negate instead.")
# ---------------------------------------------------------------------------

maxheap = []
for n in [5, 1, 8, 3]:
    heapq.heappush(maxheap, -n)     # push the negative

print("largest         ", -heapq.heappop(maxheap))
print("next largest    ", -heapq.heappop(maxheap))


# ---------------------------------------------------------------------------
section("3. Heaps of tuples — compared left to right")
# ---------------------------------------------------------------------------

tasks = []
heapq.heappush(tasks, (2, "write tests"))
heapq.heappush(tasks, (1, "fix bug"))
heapq.heappush(tasks, (3, "refactor"))

print("by priority     ", heapq.heappop(tasks))

# Warning: if priorities tie, Python compares the SECOND element. If that
# element can't be compared (a custom object), you get a TypeError. Add a
# tiebreaker counter: (priority, counter, obj)


# ---------------------------------------------------------------------------
section("4. Top-K without a full sort")
# ---------------------------------------------------------------------------

nums = [7, 2, 9, 4, 1, 8]

print("nlargest(3)     ", heapq.nlargest(3, nums))
print("nsmallest(3)    ", heapq.nsmallest(3, nums))

print("""
Sorting to get the top K is O(n log n).
A heap of size K is O(n log k) — much better when k is small and n is large.

    def k_largest(nums, k):
        h = []
        for n in nums:
            heapq.heappush(h, n)
            if len(h) > k:
                heapq.heappop(h)     # drop the smallest
        return sorted(h, reverse=True)

Note the inversion that trips people up: to keep the K LARGEST, you use a
MIN-heap and throw away the smallest each time.
""")


# ---------------------------------------------------------------------------
section("5. bisect — binary search you don't have to write")
# ---------------------------------------------------------------------------

sorted_nums = [1, 3, 3, 3, 7, 9]
print("list            ", sorted_nums)

print("bisect_left(3)  ", bisect.bisect_left(sorted_nums, 3), "  <- FIRST index where 3 could go")
print("bisect_right(3) ", bisect.bisect_right(sorted_nums, 3), "  <- AFTER the last 3")
print("count of 3s     ", bisect.bisect_right(sorted_nums, 3) - bisect.bisect_left(sorted_nums, 3))

print("insert pos of 5 ", bisect.bisect_left(sorted_nums, 5))

# insort keeps a list sorted as you add:
running = [1, 4, 9]
bisect.insort(running, 5)
print("after insort(5) ", running)

print("""
Numbers in a range [lo, hi] inclusive:
    bisect_right(a, hi) - bisect_left(a, lo)

You still have to be able to WRITE binary search by hand in an interview —
bisect is for speed once you've proven you understand it.
""")


# ---------------------------------------------------------------------------
section("6. itertools")
# ---------------------------------------------------------------------------

print("permutations    ", list(permutations([1, 2, 3])))
print("perms of 2      ", list(permutations([1, 2, 3], 2)))
print("combinations    ", list(combinations([1, 2, 3], 2)), "  <- order doesn't matter")
print("product         ", list(product([0, 1], repeat=2)))
print("accumulate      ", list(accumulate([1, 2, 3, 4])), "  <- prefix sums")

# accumulate with a custom operation:
import operator
print("running max     ", list(accumulate([3, 1, 4, 1, 5], max)))

print("""
These are great for brute-force baselines and for checking your clever
solution against a slow-but-obviously-correct one. Don't reach for
permutations as your actual answer to a backtracking question, though —
the interviewer wants to see you build the recursion.
""")


# ---------------------------------------------------------------------------
section("7. functools — memoization in one line")
# ---------------------------------------------------------------------------

calls_naive = 0
def fib_naive(n):
    global calls_naive
    calls_naive += 1
    return n if n < 2 else fib_naive(n - 1) + fib_naive(n - 2)

calls_cached = 0
@cache                       # or @lru_cache(maxsize=None) on older Python
def fib_cached(n):
    global calls_cached
    calls_cached += 1
    return n if n < 2 else fib_cached(n - 1) + fib_cached(n - 2)

fib_naive(25)
fib_cached(25)
print(f"fib(25) naive   {calls_naive:>8} calls   O(2^n)")
print(f"fib(25) cached  {calls_cached:>8} calls   O(n)")

print("""
@cache turns exponential recursion into linear. It is the fastest possible
route from "I see the recurrence" to "I have a working DP solution".

Write the recursive version, slap @cache on it, and you have top-down DP.
Then, if the interviewer asks, convert it to a bottom-up table.

Two catches:
  - arguments must be hashable, so pass tuples, not lists
  - default recursion limit is ~1000; sys.setrecursionlimit(10**6) if needed
""")


# ---------------------------------------------------------------------------
section("8. Phase 0 complete")
# ---------------------------------------------------------------------------

print("""
After drill 6, you know the tools. Every Phase 1 topic from here on is about
IDEAS, not syntax — and that's exactly where you want your attention to go.
""")


print("\nDone. Now open drills/drill_06.py\n")
