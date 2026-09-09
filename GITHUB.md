# GitHub, learned on this repo

Don't read this as a manual. Do it, on this folder, as you work through the
drills. Every command below is one you'll type today.

---

## The one distinction people get wrong

**Git** is a program on your computer that records snapshots of a folder.
It works offline. It has nothing to do with any website.

**GitHub** is a website that stores a copy of a git repository so you can
back it up, share it, and collaborate.

You can use git forever without GitHub. You cannot use GitHub without git.
Everything confusing about "GitHub" is usually just git.

---

## Setup (once, ever)

1. Install git: [git-scm.com/downloads](https://git-scm.com/downloads).
   On Windows this also gives you **Git Bash**, a decent terminal.
2. Make a GitHub account: [github.com](https://github.com).
3. Tell git who you are — this gets stamped on every commit:

   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```

   Use the same email as your GitHub account, or your commits won't link to
   your profile and won't show on your contribution graph.

4. Set the default branch name to `main`:

   ```bash
   git config --global init.defaultBranch main
   ```

---

## Turning this folder into a repository

In VS Code, open the terminal (``Ctrl+` ``) in the `dsa-python` folder:

```bash
git init
git add .
git commit -m "Start Phase 0 practice repo"
```

Three commands, three concepts:

| Command | What actually happened |
|---|---|
| `git init` | Created a hidden `.git/` folder. This folder *is* the repository — the entire history lives there. |
| `git add .` | Moved your changes to the **staging area**: "these are the changes I want in my next snapshot." |
| `git commit -m "..."` | Took the snapshot. Permanent, with your name, the time, and that message. |

The staging area is the part that feels pointless at first. It exists so you
can commit *some* of your changes and not others — you fixed a bug and a typo,
and you want them in separate commits.

---

## Pushing it to GitHub

1. On github.com, click **+** → **New repository**.
2. Name it `dsa-python`. **Do not** tick "Add a README" — you already have one,
   and starting both sides with different histories is the single most common
   beginner mess.
3. Create it. GitHub shows you commands. You want the "push an existing
   repository" ones:

```bash
git remote add origin https://github.com/YOUR-USERNAME/dsa-python.git
git branch -M main
git push -u origin main
```

- `remote add origin ...` — saves that URL under the nickname `origin`.
- `push -u origin main` — uploads `main` and remembers the pairing, so from
  now on plain `git push` is enough.

Refresh the page. Your code is there.

---

## The daily loop

This is 90% of git, forever:

```bash
git status                      # what have I changed?
git add drills/drill_01.py      # stage that one file
git commit -m "Solve second_largest and rotate_right"
git push                        # send it up
```

Do this after every drill function you get passing. Small commits, often.

**Writing a commit message.** Finish the sentence "If applied, this commit
will ___". So: `Solve two_sum with a hashmap`, not `update` or `stuff` or
`asdf`. You'll be reading these back in three months.

Other daily commands:

```bash
git log --oneline               # your history, one line each
git diff                        # what changed but isn't staged
git diff --staged               # what's staged and about to be committed
```

---

## Branches

A branch is a movable label pointing at a commit. That's genuinely all it is.
`main` is just a branch with a conventional name.

```bash
git switch -c drill-05          # create a branch and move onto it
# ...work, commit, commit...
git switch main                 # go back
git merge drill-05              # bring the work into main
git branch -d drill-05          # delete the label, work is kept
```

Why bother for solo work? Because it lets you try a rewrite of
`sliding_window_max` without touching the version that already passes. If the
experiment fails, delete the branch and nothing was lost.

`git switch` is the modern command. Older tutorials say `git checkout` — it
does the same thing and about six other unrelated things, which is why it got
split up.

---

## Pull requests

A PR is a request to merge one branch into another, with a discussion thread
and a diff attached. On a team, nothing reaches `main` any other way.

Practise it on yourself:

```bash
git switch -c add-notes
# edit the README
git add README.md
git commit -m "Add notes on my weak topics"
git push -u origin add-notes
```

GitHub replies in the terminal with a link. Open it, click **Create pull
request**, read the diff on the **Files changed** tab, then **Merge**.

Then locally:

```bash
git switch main
git pull                        # fetch the merged result from GitHub
```

`git pull` is the mirror of `git push`. Run it before you start work on any
machine you don't have exclusive use of.

---

## Actions (CI)

`.github/workflows/check.yml` is already in this repo. The moment you push,
GitHub spins up a Linux VM, installs Python, and runs `python check.py`.

Go to the **Actions** tab and watch it. A green tick means every drill passed;
a red X means something's broken. Click into a failed run to read the exact
output.

This is continuous integration, and that file is the whole idea: *code that
runs your tests so you can't forget to*. Every real engineering team has some
version of it. Having built one is worth mentioning in an interview.

Open the file and read the comments — it's short and each line is explained.

---

## Issues

The **Issues** tab is a to-do list attached to your code. Use it as your DSA
tracker:

- "Redo sliding_window_max with a monotonic deque"
- "I keep getting binary search boundaries wrong — drill this"

Write `Closes #3` in a commit message and merging it closes issue 3
automatically.

---

## The rest of GitHub, briefly

| Feature | What it's for | Worth your time now? |
|---|---|---|
| **README.md** | The page shown on your repo's front page. Markdown. | Yes — it's the first thing a recruiter sees |
| **Fork** | Your own copy of someone else's repo | When you contribute to open source |
| **Star** | A bookmark | Free |
| **Gist** | A single shareable snippet | Occasionally handy |
| **Pages** | Free static site hosting from a repo | Later, for a portfolio |
| **Projects** | Kanban board over issues | You already have Notion |
| **Releases** | Tagged, downloadable versions | Only for shipped software |
| **Codespaces** | VS Code in the browser on a cloud VM | Nice, limited free hours |

Ignore most of that for now. Commits, branches, PRs, and Actions are the ones
that matter, and they're the ones this repo makes you practise.

---

## When it goes wrong

```bash
# Unstage a file (keep the edits)
git restore --staged path/to/file.py

# Throw away uncommitted edits to a file — THIS DELETES WORK
git restore path/to/file.py

# Fix the message of the commit you just made
git commit --amend -m "A better message"

# Undo the last commit, keep the changes as unstaged edits
git reset --soft HEAD~1

# See what you did, including things you think you lost
git reflog
```

`git reflog` is the safety net. Git almost never truly deletes a commit;
reflog shows you the ones that fell off the map, and you can get them back.
Before you panic about having "lost everything", run it.

**Never commit secrets.** API keys, tokens, passwords. Deleting them in a
later commit does *not* remove them — the old commit still holds them, and
the whole history is public. Add the file to `.gitignore` before the first
`git add`.

---

## Do this today

- [ ] Install git, set `user.name` and `user.email`
- [ ] `git init`, `git add .`, `git commit` in this folder
- [ ] Create the GitHub repo, push it
- [ ] Solve one drill function, then commit and push it on its own
- [ ] Look at the Actions tab and watch the red X
- [ ] Keep going until it turns green

That red-X-to-green-tick moment is the whole point. You now have automated
tests running on a cloud machine because you pushed a file — which is the
actual job, in miniature.
