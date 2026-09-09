"""
LESSON 4 — Strings

Run me:  python lessons/04_strings.py

Strings behave like tuples of characters: you can index and slice them, but
you can never change one in place. Understanding that single fact prevents
most string bugs and one very common performance disaster.
"""

def section(name):
    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)


# ---------------------------------------------------------------------------
section("1. Immutability")
# ---------------------------------------------------------------------------

s = "hello"
print("s               ", s)
print("s[0]            ", s[0])
print("s[-1]           ", s[-1])
print("s[1:4]          ", s[1:4])
print("s[::-1]         ", s[::-1], "  <- reversing a string")

try:
    s[0] = "H"
except TypeError as e:
    print("s[0] = 'H'      -> TypeError:", e)

# To "edit" a string, convert to a list, change it, join it back:
chars = list(s)
chars[0] = "H"
print("edited          ", "".join(chars))


# ---------------------------------------------------------------------------
section("2. The O(n^2) trap")
# ---------------------------------------------------------------------------

print("""
    # SLOW — builds a brand new string every iteration:
    out = ""
    for ch in text:
        out += ch                 # O(n) each time -> O(n^2) total

    # FAST — collect, then join once:
    parts = []
    for ch in text:
        parts.append(ch)
    out = "".join(parts)          # O(n) total

Always build with a list and join at the end. This is the single most common
performance mistake in Python string code, and interviewers do notice it.
""")


# ---------------------------------------------------------------------------
section("3. Methods worth memorising")
# ---------------------------------------------------------------------------

t = "  Hello, World!  "

print("repr            ", repr(t))
print(".strip()        ", repr(t.strip()))
print(".lower()        ", t.strip().lower())
print(".upper()        ", t.strip().upper())
print(".replace()      ", t.strip().replace("World", "Coco"))
print(".split(',')     ", t.strip().split(","))
print(".split()        ", "a  b   c".split(), "  <- no arg splits on ANY whitespace run")
print(".startswith()   ", t.strip().startswith("Hello"))
print(".find('World')  ", t.strip().find("World"), "  <- -1 if absent, no crash")

print(".join()         ", "-".join(["a", "b", "c"]))
print("join numbers    ", ",".join(str(n) for n in [1, 2, 3]), "  <- join needs strings")

print(".isalnum()      ", "abc123".isalnum())
print(".isdigit()      ", "123".isdigit())
print(".isalpha()      ", "abc".isalpha())


# ---------------------------------------------------------------------------
section("4. Characters as numbers")
# ---------------------------------------------------------------------------

print("ord('a')        ", ord("a"))
print("chr(97)         ", chr(97))
print("ord('c')-ord('a')", ord("c") - ord("a"), "  <- index into a 26-slot array")

# Frequency array without a dict — sometimes asked for explicitly:
counts = [0] * 26
for ch in "banana":
    counts[ord(ch) - ord("a")] += 1
print("counts[0:5]     ", counts[:5], "  (a=3, b=1, n=2)")


# ---------------------------------------------------------------------------
section("5. f-strings")
# ---------------------------------------------------------------------------

name, score = "Coco", 0.8567
print(f"  plain        {name} scored {score}")
print(f"  2 decimals   {score:.2f}")
print(f"  percentage   {score:.1%}")
print(f"  padded       |{name:>10}|{name:<10}|{name:^10}|")
print(f"  expression   {2 ** 10}")
print(f"  debug (=)    {score=}")


# ---------------------------------------------------------------------------
section("6. Two patterns you'll write a hundred times")
# ---------------------------------------------------------------------------

def is_palindrome(s):
    """Ignore non-alphanumerics, ignore case."""
    cleaned = [ch.lower() for ch in s if ch.isalnum()]
    return cleaned == cleaned[::-1]

print("palindrome?     ", is_palindrome("A man, a plan, a canal: Panama"))


def is_palindrome_two_pointer(s):
    """Same result, O(1) extra space. This is the version to show an interviewer."""
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

print("two-pointer     ", is_palindrome_two_pointer("A man, a plan, a canal: Panama"))
print("negative case   ", is_palindrome_two_pointer("hello"))


print("\nDone. Now open drills/drill_04.py\n")
