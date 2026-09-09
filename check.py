"""
Drill checker. No dependencies — just run it.

    python check.py        check every drill
    python check.py 3      check drill 3 only
    python check.py 3 -v   also show the cases that passed

Written to be readable: open it if you're curious how a test runner works.
"""

import sys
import inspect
import importlib
import traceback

sys.path.insert(0, "tests")
sys.path.insert(0, "drills")

from cases import CASES   # noqa: E402


GREEN = "\033[92m"
RED = "\033[91m"
GREY = "\033[90m"
BOLD = "\033[1m"
OFF = "\033[0m"

TIMEOUT_NOTE = "took too long — check for an infinite loop or missing memoization"


def load_drill(n):
    name = f"drill_{n:02d}"
    try:
        return importlib.import_module(name)
    except ModuleNotFoundError:
        return None


def show(value):
    text = repr(value)
    return text if len(text) <= 70 else text[:67] + "..."


def is_unwritten(func):
    """
    True if the body is still the untouched `pass  # TODO`.

    We check the source rather than the return value, because some of these
    functions are SUPPOSED to return None sometimes — second_largest([1]),
    for instance. Checking the return value would let an empty function
    quietly 'pass' those cases.
    """
    try:
        body = inspect.getsource(func)
    except (OSError, TypeError):
        return False
    return "pass  # TODO" in body


def run_drill(n, verbose=False):
    module = load_drill(n)
    if module is None:
        print(f"{RED}drills/drill_{n:02d}.py not found{OFF}")
        return 0, 0

    cases = CASES.get(n, [])
    passed = failed = 0
    skipped = set()
    reported = set()

    print(f"\n{BOLD}Drill {n}{OFF}  ({len(cases)} cases)")
    print("-" * 62)

    for func_name, args, expected in cases:
        func = getattr(module, func_name, None)

        if func is None:
            if func_name not in reported:
                print(f"  {RED}MISSING{OFF}  {func_name}  — no such function")
                reported.add(func_name)
            failed += 1
            continue

        if is_unwritten(func):
            failed += 1
            if func_name not in skipped:
                print(f"  {GREY}TODO      {func_name}  — not written yet{OFF}")
                skipped.add(func_name)
            continue

        try:
            actual = func(*args)
        except RecursionError:
            failed += 1
            if func_name not in reported:
                print(f"  {RED}ERROR  {OFF}  {func_name}{args}")
                print(f"           {GREY}infinite recursion — check your base case{OFF}")
                reported.add(func_name)
            continue
        except Exception:
            failed += 1
            if func_name not in reported:
                print(f"  {RED}ERROR  {OFF}  {func_name}{args}")
                lines = traceback.format_exc().strip().splitlines()
                print(f"           {GREY}{lines[-1]}{OFF}")
                reported.add(func_name)
            continue

        if actual == expected:
            passed += 1
            if verbose:
                print(f"  {GREEN}pass   {OFF}  {func_name}{args}")
        else:
            failed += 1
            print(f"  {RED}FAIL   {OFF}  {func_name}{args}")
            print(f"           expected  {show(expected)}")
            print(f"           got       {show(actual)}")

    total = passed + failed
    if failed == 0 and total:
        print(f"  {GREEN}all {total} cases pass{OFF}")
    else:
        colour = GREEN if passed else RED
        print(f"  {colour}{passed}{OFF}/{total} passing")

    return passed, total


def main():
    args = [a for a in sys.argv[1:]]
    verbose = "-v" in args or "--verbose" in args
    numbers = [int(a) for a in args if a.isdigit()]

    if not numbers:
        numbers = sorted(CASES)

    grand_pass = grand_total = 0
    for n in numbers:
        p, t = run_drill(n, verbose)
        grand_pass += p
        grand_total += t

    if len(numbers) > 1:
        print("\n" + "=" * 62)
        pct = (grand_pass / grand_total * 100) if grand_total else 0
        print(f"{BOLD}TOTAL  {grand_pass}/{grand_total}  ({pct:.0f}%){OFF}")
        print("=" * 62)

    print()
    if grand_pass == grand_total and grand_total:
        print("Phase 0 done. Go back to the Notion roadmap and start Phase 1.\n")
        return 0
    else:
        remaining = grand_total - grand_pass
        print(f"{remaining} to go. Run with -v to see what's already passing.\n")
        return 1


if __name__ == "__main__":
    # Exit code 0 = everything passed, 1 = something failed.
    # This is how GitHub Actions knows whether to show a green tick or a red X.
    sys.exit(main())
