# DSA in Python — Practice Repo

Phase 0 of the roadmap: making Python invisible so all your thinking goes to the algorithm.

---

## One-time setup

1. **Install Python 3.10+** from [python.org](https://python.org). On Windows, tick
   "Add Python to PATH" during install.
2. **Install VS Code** from [code.visualstudio.com](https://code.visualstudio.com).
3. **Install the Python extension** — open VS Code, press `Ctrl+Shift+X`
   (`Cmd+Shift+X` on Mac), search "Python", install the Microsoft one.
4. **Open this folder** — `File > Open Folder...` and pick `dsa-python`.
5. **Check it works** — open a terminal inside VS Code with ``Ctrl+` `` and run:

   ```
   python check.py
   ```

   You should see all drills failing. That's correct. That's the point.

No pip installs, no virtualenv, no dependencies. Everything here is standard library.

---

## How this works

Two kinds of file:

**`lessons/`** — read them, then run them. Each one prints its own output so you
see the behaviour, not just the description.

```
python lessons/01_lists_and_slicing.py
```

**`drills/`** — functions with `TODO` in the body. You write the code. Then:

```
python check.py 1        # check drill 1
python check.py          # check everything
```

The checker tells you which case failed, what it expected, and what you gave it.

---

## The loop

For each numbered topic:

1. Read the lesson file top to bottom in VS Code.
2. Run it. Compare the output to what you predicted before running.
3. Open the matching drill file.
4. Solve the functions **without looking anything up first**. Get stuck, then look.
5. Run `python check.py N` until green.
6. Come back three days later and re-solve one drill from scratch.

Step 6 is the one everybody skips and it's the one that makes it stick.

---

## Order

| # | Lesson | Drill |
|---|--------|-------|
| 1 | Lists and slicing | `drill_01.py` |
| 2 | Dicts, sets, tuples | `drill_02.py` |
| 3 | Comprehensions and sorting | `drill_03.py` |
| 4 | Strings | `drill_04.py` |
| 5 | The `collections` module | `drill_05.py` |
| 6 | `heapq`, `bisect`, `itertools`, `functools` | `drill_06.py` |

Roughly one per two days. Two weeks total, and then you start Phase 1 with the
language out of your way.

---

## Version control

Read **`GITHUB.md`** in this folder. It teaches git and GitHub using this
exact repo — commit each drill as you solve it, push it, and the included
GitHub Actions workflow will run your tests automatically on every push.

Do it alongside the drills, not after.

---

## VS Code things worth knowing early

- `F5` runs the current file with the debugger attached.
- Click in the gutter (left of a line number) to set a **breakpoint**, then `F5`.
  Step with `F10`, inspect variables in the left panel. Learn this now — it will
  save you more time than any other single habit.
- `Ctrl+Shift+P` → "Python: Select Interpreter" if VS Code picks the wrong Python.
- `Ctrl+/` toggles a comment on the selected lines.
