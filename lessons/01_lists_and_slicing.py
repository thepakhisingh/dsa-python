"""
LESSON 1 — Lists and slicing

Run me:  python lessons/01_lists_and_slicing.py

Read a section, guess the output, THEN look at what printed.
Guessing first is what turns reading into learning.
"""

def section(name):
    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)


# ---------------------------------------------------------------------------
section("1. Indexing — forwards and backwards")
# ---------------------------------------------------------------------------

nums = [10, 20, 30, 40, 50]

print("nums          ", nums)
print("nums[0]       ", nums[0])       # first
print("nums[-1]      ", nums[-1])      # last  <- use this, never nums[len(nums)-1]
print("nums[-2]      ", nums[-2])      # second to last

# Negative indexing is not a trick. It's the normal way to reach the end.


# ---------------------------------------------------------------------------
section("2. Slicing — nums[start:stop:step]")
# ---------------------------------------------------------------------------

print("nums[1:4]     ", nums[1:4])     # start INCLUSIVE, stop EXCLUSIVE
print("nums[:3]      ", nums[:3])      # from the beginning
print("nums[2:]      ", nums[2:])      # to the end
print("nums[:]       ", nums[:])       # a full COPY
print("nums[::2]     ", nums[::2])     # every 2nd element
print("nums[::-1]    ", nums[::-1])    # reversed — you will use this constantly
print("nums[-2:]     ", nums[-2:])     # last two

# Slicing never raises IndexError. It just gives you what exists:
print("nums[2:99]    ", nums[2:99])
print("nums[99:]     ", nums[99:])     # empty list, no crash


# ---------------------------------------------------------------------------
section("3. Copy vs reference — the bug that bites everyone")
# ---------------------------------------------------------------------------

a = [1, 2, 3]
b = a           # NOT a copy. b is another name for the same list.
b.append(4)
print("a is now      ", a, "  <- you changed it without touching 'a'")

c = [1, 2, 3]
d = c[:]        # this IS a copy (so is list(c) and c.copy())
d.append(4)
print("c is still    ", c)
print("d is          ", d)

# Nested lists need more care — a slice copies the OUTER list only:
grid = [[0, 0], [0, 0]]
shallow = grid[:]
shallow[0][0] = 9
print("grid          ", grid, "  <- inner lists are still shared!")

# For a grid, build each row separately:
grid2 = [[0] * 3 for _ in range(2)]
grid2[0][0] = 9
print("grid2         ", grid2, "  <- correct")

# NEVER do this for a grid:  [[0] * 3] * 2
wrong = [[0] * 3] * 2
wrong[0][0] = 9
print("wrong         ", wrong, "  <- same row object twice")


# ---------------------------------------------------------------------------
section("4. The methods you actually use")
# ---------------------------------------------------------------------------

xs = [3, 1, 4, 1, 5]
print("start         ", xs)

xs.append(9)                 # add to end            O(1)
print("append(9)     ", xs)

xs.pop()                     # remove from end       O(1)
print("pop()         ", xs)

xs.insert(0, 0)              # insert at front       O(n)  <- slow
print("insert(0,0)   ", xs)

xs.pop(0)                    # remove from front     O(n)  <- slow
print("pop(0)        ", xs)

print("count of 1    ", xs.count(1))
print("index of 4    ", xs.index(4))

xs.sort()                    # sorts IN PLACE, returns None
print("sort()        ", xs)

ys = sorted([3, 1, 2])       # returns a NEW list
print("sorted(...)   ", ys)

xs.reverse()                 # in place
print("reverse()     ", xs)

# Common mistake:
result = [3, 1, 2].sort()
print("[..].sort()   ", result, "  <- None! .sort() returns nothing")


# ---------------------------------------------------------------------------
section("5. Cost — this is what interviewers care about")
# ---------------------------------------------------------------------------

print("""
    lst[i]           O(1)     indexing is free
    lst.append(x)    O(1)
    lst.pop()        O(1)     from the END
    lst.pop(0)       O(n)     from the FRONT — shifts everything
    lst.insert(0,x)  O(n)     same problem
    x in lst         O(n)     scans the whole list
    x in some_set    O(1)     <- use a set when you're checking membership
    lst.sort()       O(n log n)
    lst[a:b]         O(b-a)   slicing COPIES, it isn't free

If you need to pop from the front repeatedly, you want collections.deque
(Lesson 5). Using a list there turns an O(n) algorithm into O(n^2), and that
is a real interview failure, not a nitpick.
""")


# ---------------------------------------------------------------------------
section("6. Unpacking and iteration")
# ---------------------------------------------------------------------------

point = [3, 7]
x, y = point
print("x, y          ", x, y)

first, *rest = [1, 2, 3, 4]
print("first, *rest  ", first, rest)

for i, val in enumerate([10, 20, 30]):
    print(f"  index {i} -> {val}")

for a, b in zip([1, 2, 3], "abc"):
    print(f"  zipped {a} {b}")

# Iterating backwards, two idioms:
print("reversed:     ", list(reversed([1, 2, 3])))
print("slice:        ", [1, 2, 3][::-1])


print("\nDone. Now open drills/drill_01.py\n")
