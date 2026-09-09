"""
LESSON 2 — Dicts, sets, tuples

Run me:  python lessons/02_dicts_sets_tuples.py

Roughly a third of all interview problems are solved by "put it in a hashmap".
This lesson is the one that pays off fastest.
"""

def section(name):
    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)


# ---------------------------------------------------------------------------
section("1. Dicts — the workhorse")
# ---------------------------------------------------------------------------

ages = {"ana": 31, "bo": 24, "cy": 45}

print("ages            ", ages)
print("ages['bo']      ", ages["bo"])
print("'bo' in ages    ", "bo" in ages)      # O(1) — checks KEYS
print("len(ages)       ", len(ages))

ages["dee"] = 19            # add
ages["bo"] = 25             # update
print("after edits     ", ages)

del ages["cy"]
print("after delete    ", ages)


# ---------------------------------------------------------------------------
section("2. Reading safely — .get() instead of KeyError")
# ---------------------------------------------------------------------------

print("get('zed')          ", ages.get("zed"))          # None, no crash
print("get('zed', 0)       ", ages.get("zed", 0))       # your own default

counts = {}
for ch in "hello":
    counts[ch] = counts.get(ch, 0) + 1   # the frequency-map one-liner
print("char counts         ", counts)

# .setdefault is the version for building lists:
graph = {}
for a, b in [("x", "y"), ("x", "z"), ("y", "z")]:
    graph.setdefault(a, []).append(b)
print("adjacency           ", graph)

# Lesson 5 shows defaultdict, which is cleaner than both of these.


# ---------------------------------------------------------------------------
section("3. Iterating a dict")
# ---------------------------------------------------------------------------

for k in ages:                      # keys by default
    print("  key       ", k)

for v in ages.values():
    print("  value     ", v)

for k, v in ages.items():           # this is the one you want most of the time
    print(f"  {k} -> {v}")

# Dicts keep insertion order (guaranteed since Python 3.7).
print("keys as list    ", list(ages.keys()))


# ---------------------------------------------------------------------------
section("4. Sets — membership and dedup")
# ---------------------------------------------------------------------------

s = {3, 1, 4, 1, 5}
print("set literal     ", s, "  <- duplicate 1 vanished, order is arbitrary")

print("from list       ", set([1, 1, 2, 2, 3]))
print("empty set       ", set(), "  <- {} is an empty DICT, not a set")

s.add(9)
s.discard(100)      # no error if missing
print("after add       ", s)

print("3 in s          ", 3 in s, "  <- O(1). This is why sets exist.")

a, b = {1, 2, 3}, {2, 3, 4}
print("a | b union     ", a | b)
print("a & b intersect ", a & b)
print("a - b difference", a - b)
print("a ^ b symmetric ", a ^ b)


# ---------------------------------------------------------------------------
section("5. Tuples — and why they matter for hashing")
# ---------------------------------------------------------------------------

t = (3, 7)
print("tuple           ", t)
print("t[0]            ", t[0])

try:
    t[0] = 99
except TypeError as e:
    print("t[0] = 99       -> TypeError:", e)

# Immutable means hashable, which means usable as a dict key or set element:
visited = set()
visited.add((0, 0))
visited.add((1, 2))
print("visited coords  ", visited, "  <- grid problems live on this")

distances = {(0, 0): 0, (1, 0): 1}
print("dict with tuple keys", distances)

# A list can NOT be a key:
try:
    {[1, 2]: "nope"}
except TypeError as e:
    print("list as key     -> TypeError:", e)


# ---------------------------------------------------------------------------
section("6. The pattern this all exists for")
# ---------------------------------------------------------------------------

print("""
Two Sum, in full:

    def two_sum(nums, target):
        seen = {}                       # value -> index
        for i, n in enumerate(nums):
            need = target - n
            if need in seen:            # O(1) lookup
                return [seen[need], i]
            seen[n] = i
        return []

Brute force is two nested loops, O(n^2). The hashmap makes it O(n) by trading
memory for time. Almost every "make this faster" moment in an interview is
some version of that trade. Recognise it and you have half the job done.
""")


print("\nDone. Now open drills/drill_02.py\n")
