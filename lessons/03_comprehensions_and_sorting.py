"""
LESSON 3 — Comprehensions and sorting

Run me:  python lessons/03_comprehensions_and_sorting.py

Comprehensions save you keystrokes under time pressure.
Sorting with a key function shows up in maybe a fifth of all problems.
"""

def section(name):
    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)


# ---------------------------------------------------------------------------
section("1. List comprehensions")
# ---------------------------------------------------------------------------

nums = [1, 2, 3, 4, 5, 6]

# The long way:
squares = []
for n in nums:
    squares.append(n * n)

# The short way — same thing:
squares2 = [n * n for n in nums]
print("squares         ", squares2)

# With a filter:
evens = [n for n in nums if n % 2 == 0]
print("evens           ", evens)

# Transform AND filter:
print("even squares    ", [n * n for n in nums if n % 2 == 0])

# Conditional VALUE (note: the if/else goes in front):
print("parity labels   ", ["even" if n % 2 == 0 else "odd" for n in nums])

# Nested loops — read left to right, same order as nested for-loops:
pairs = [(a, b) for a in [1, 2] for b in "xy"]
print("pairs           ", pairs)

# Flattening one level:
nested = [[1, 2], [3, 4], [5]]
print("flattened       ", [x for row in nested for x in row])

# Building a grid (remember Lesson 1 — this is the SAFE way):
grid = [[0] * 3 for _ in range(2)]
print("grid            ", grid)


# ---------------------------------------------------------------------------
section("2. Dict and set comprehensions")
# ---------------------------------------------------------------------------

words = ["apple", "fig", "cherry"]

print("word -> length  ", {w: len(w) for w in words})
print("inverted        ", {len(w): w for w in words})
print("set of lengths  ", {len(w) for w in words})

# From two lists:
keys, vals = ["a", "b"], [1, 2]
print("zipped to dict  ", {k: v for k, v in zip(keys, vals)})
print("or just         ", dict(zip(keys, vals)))


# ---------------------------------------------------------------------------
section("3. Generator expressions — same syntax, round brackets")
# ---------------------------------------------------------------------------

# A list comprehension builds the whole list in memory.
# A generator produces items one at a time.

print("sum             ", sum(n * n for n in nums))
print("any negative?   ", any(n < 0 for n in nums))
print("all positive?   ", all(n > 0 for n in nums))
print("max by rule     ", max((n for n in nums if n % 2), default=None))

# any() and all() with a generator short-circuit — they stop at the first
# answer. That makes them genuinely fast, not just pretty.


# ---------------------------------------------------------------------------
section("4. Sorting with key=")
# ---------------------------------------------------------------------------

words = ["banana", "fig", "cherry", "date"]

print("default (alpha) ", sorted(words))
print("by length       ", sorted(words, key=len))
print("by last letter  ", sorted(words, key=lambda w: w[-1]))
print("descending      ", sorted(words, key=len, reverse=True))

people = [("ana", 31), ("bo", 24), ("cy", 31), ("dee", 24)]

print("by age          ", sorted(people, key=lambda p: p[1]))

# TWO keys at once — return a TUPLE. Compared left to right.
print("age, then name  ", sorted(people, key=lambda p: (p[1], p[0])))

# Mixed directions: negate a number to flip just that field.
print("age DESC, name  ", sorted(people, key=lambda p: (-p[1], p[0])))

# That negation trick only works on numbers. For strings you'd sort twice,
# relying on stability (below).


# ---------------------------------------------------------------------------
section("5. Stability")
# ---------------------------------------------------------------------------

data = [("a", 2), ("b", 1), ("c", 2), ("d", 1)]
print("original        ", data)
print("sorted by num   ", sorted(data, key=lambda x: x[1]))

print("""
Python's sort is STABLE: items that compare equal keep their original relative
order. Above, ("b",1) still comes before ("d",1).

This lets you sort by a secondary key first, then a primary key, and get a
correct multi-level sort in two passes.
""")


# ---------------------------------------------------------------------------
section("6. Sorting by frequency — a very common ask")
# ---------------------------------------------------------------------------

from collections import Counter

nums = [4, 4, 1, 2, 2, 2, 3]
freq = Counter(nums)
print("frequencies     ", dict(freq))

# Most frequent first; ties broken by smaller value first:
ordered = sorted(freq, key=lambda n: (-freq[n], n))
print("by freq desc    ", ordered)

# Expanded back out:
print("expanded        ", [n for n in ordered for _ in range(freq[n])])


print("\nDone. Now open drills/drill_03.py\n")
