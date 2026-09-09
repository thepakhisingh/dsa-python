"""
LESSON 5 — The collections module

Run me:  python lessons/05_collections_module.py

Three imports carry most of your interview code:

    from collections import deque, Counter, defaultdict

Know these cold and a lot of problems shrink to a handful of lines.
"""

from collections import deque, Counter, defaultdict


def section(name):
    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)


# ---------------------------------------------------------------------------
section("1. deque — the BFS workhorse")
# ---------------------------------------------------------------------------

d = deque([1, 2, 3])
print("deque           ", d)

d.append(4)         # right, O(1)
d.appendleft(0)     # left,  O(1)   <- a list can't do this cheaply
print("after appends   ", d)

print("pop()           ", d.pop())        # from right, O(1)
print("popleft()       ", d.popleft())    # from left,  O(1)
print("now             ", d)

print("""
    list.pop(0)      O(n)   shifts every remaining element
    deque.popleft()  O(1)

A BFS with a list-based queue is O(n^2). With a deque it's O(n). Same code
otherwise. This is why deque is the default queue.
""")

# Fixed-length deque — a sliding window that discards for you:
window = deque(maxlen=3)
for n in [1, 2, 3, 4, 5]:
    window.append(n)
    print("  window        ", list(window))


# ---------------------------------------------------------------------------
section("2. BFS with a deque — the template")
# ---------------------------------------------------------------------------

graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["d", "e"],
    "d": ["e"],
    "e": [],
}

def bfs_shortest(graph, start, goal):
    """Fewest edges from start to goal, or -1."""
    if start == goal:
        return 0
    queue = deque([(start, 0)])         # (node, distance)
    seen = {start}                      # mark on ENQUEUE, not on dequeue
    while queue:
        node, dist = queue.popleft()
        for nxt in graph[node]:
            if nxt == goal:
                return dist + 1
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, dist + 1))
    return -1

print("a -> e          ", bfs_shortest(graph, "a", "e"))

print("""
Memorise that shape. It is the answer to: shortest path in an unweighted
graph, word ladder, rotting oranges, number of islands (with DFS or BFS),
knight moves, maze problems. Same eight lines every time.

The one thing people get wrong: mark `seen` when you ENQUEUE a node, not when
you dequeue it. Otherwise the same node gets queued many times.
""")


# ---------------------------------------------------------------------------
section("3. Counter — frequency maps for free")
# ---------------------------------------------------------------------------

c = Counter("mississippi")
print("Counter         ", c)
print("c['s']          ", c["s"])
print("c['z']          ", c["z"], "  <- missing keys give 0, never KeyError")
print("most_common(2)  ", c.most_common(2))
print("total           ", sum(c.values()))

print("from a list     ", Counter([1, 1, 2, 3, 3, 3]))

# Counters do arithmetic:
print("c1 + c2         ", Counter("aab") + Counter("abc"))
print("c1 - c2         ", Counter("aab") - Counter("abc"))

# Anagram check in one line:
print("anagram?        ", Counter("listen") == Counter("silent"))


# ---------------------------------------------------------------------------
section("4. defaultdict — no more 'if key not in d'")
# ---------------------------------------------------------------------------

# Without it:
plain = {}
for a, b in [("x", "y"), ("x", "z")]:
    if a not in plain:
        plain[a] = []
    plain[a].append(b)
print("plain dict      ", plain)

# With it:
adj = defaultdict(list)
for a, b in [("x", "y"), ("x", "z")]:
    adj[a].append(b)            # missing key auto-creates []
print("defaultdict     ", dict(adj))

tally = defaultdict(int)
for ch in "hello":
    tally[ch] += 1              # missing key auto-creates 0
print("defaultdict int ", dict(tally))

groups = defaultdict(set)
groups["evens"].add(2)
print("defaultdict set ", dict(groups))

print("""
    defaultdict(list)   -> missing key becomes []
    defaultdict(int)    -> missing key becomes 0
    defaultdict(set)    -> missing key becomes set()

Careful: merely READING a missing key creates it.
    d = defaultdict(int); x = d["ghost"]   # "ghost" now exists with value 0
Use `key in d` when you only want to check.
""")


# ---------------------------------------------------------------------------
section("5. Group anagrams — all three ideas at once")
# ---------------------------------------------------------------------------

def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        key = "".join(sorted(w))        # anagrams share a sorted spelling
        groups[key].append(w)
    return dict(groups)

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


print("\nDone. Now open drills/drill_05.py\n")
