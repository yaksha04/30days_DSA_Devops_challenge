1. Merge vs Rebase

Both combine changes from one branch into another, but they do it differently.

Merge

Creates a new merge commit that joins two branches.

A---B---C (main)
     \
      D---E (feature)

git checkout main
git merge feature

A---B---C---------M
     \           /
      D---------E
Command
git checkout main
git merge feature
Advantages
Preserves complete history
Easy to understand
Safe for shared branches
No history rewriting
Disadvantages
Creates extra merge commits
History can become messy
Rebase

Moves your branch so it appears to start from the latest commit.

Instead of creating a merge commit, Git replays your commits.

Before:

A---B---C (main)
     \
      D---E (feature)

After

git checkout feature
git rebase main
A---B---C---D'---E'

Notice:

D → D'
E → E'

They are new commits.

Then merging becomes

git checkout main
git merge feature
A---B---C---D'---E'

No merge commit.

Advantages

✔ Clean history

✔ Looks linear

✔ Easier to understand git log

✔ Preferred before opening Pull Requests

Disadvantages

Never rebase commits already pushed to a shared branch.

Because commit hashes change.

Your teammates' history breaks.

When to use Merge

Use merge when

branch is shared
preserving history matters
working with teams
integrating completed features

Example

feature-login
↓

main

Use

git merge feature-login
When to use Rebase

Use rebase

before creating Pull Request
updating your branch
keeping history clean
only on your local commits

Example

main updated

↓

feature
git checkout feature
git fetch
git rebase origin/main
Interview Question

Which is better?

Answer:

Neither.

Merge preserves history.
Rebase creates cleaner history.

Use rebase on private branches and merge on shared branches.

2. Fast-forward vs 3-Way Merge
Fast-forward Merge

Happens when no new commits exist on main.

Example

main

A---B

feature

A---B---C---D

Merge

git checkout main
git merge feature

Result

A---B---C---D

No merge commit.

Git simply moves the pointer.

Advantages
Clean
Simple
No extra commit
3-Way Merge

Occurs when both branches have new commits.

A---B---C (main)
     \
      D---E (feature)

Merge

git merge feature

Result

       D---E
      /     \
A---B---C----M

Git creates merge commit M.

Git compares

Three versions

common ancestor
current branch
feature branch

Hence called 3-way merge.

3. Squash Commits Before Merging

Suppose history looks like

Fix typo

Fix typo again

Update README

Forgot semicolon

Remove debug

Final fix

Not useful.

Instead combine them into one meaningful commit.

Implement User Authentication
Method 1
git merge --squash feature
git commit

Everything becomes one commit.

Method 2

Interactive rebase

git rebase -i HEAD~5

Choose squash.

Benefits

Cleaner history

Easy rollback

Easy review

Professional repositories often prefer squash merges.

4. Resolving Merge Conflicts Step by Step

Suppose

Main

print("Hello")

Feature

print("Hello World")

Both edited same line.

Merge

git merge feature

Git says

CONFLICT
Step 1

Check status

git status

Output

both modified: app.py
Step 2

Open file

You'll see

<<<<<<< HEAD
print("Hello")
=======
print("Hello World")
>>>>>>> feature
Meaning
<<<<<<< HEAD

Current branch

=======

Separator

>>>>>>> feature

Incoming branch

Step 3

Edit manually

Example

print("Hello World")

Remove markers.

Step 4

Stage

git add app.py
Step 5

Finish merge

git commit

Done.

Abort Merge

If everything went wrong

git merge --abort

Returns to previous state.

5. Cherry-pick Specific Commits

Copies one commit from another branch.

Suppose

feature

A---B---C

Need only commit B.

Copy hash

git log
3ad82bc

Now

git checkout main

git cherry-pick 3ad82bc

Result

main

A---X

Where X contains changes from commit B.

Use Cases

Bug fix

Emergency production fix

Selective feature migration

Cherry-pick Multiple Commits
git cherry-pick hash1 hash2 hash3
Cherry-pick Range
git cherry-pick A^..D

Copies A through D.

6. Revert vs Reset vs Checkout

These are often confused.

Git Revert

Creates a new commit that undoes an earlier commit.

Safe.

History remains.

A---B---C

Revert C

A---B---C---D

D reverses C

Command

git revert <commit>

Best for shared repositories.

Git Reset

Moves branch pointer backward.

A---B---C

Reset to B

A---B

Command

git reset --hard HEAD~1

Dangerous.

Commits may be lost.

Types

Soft

git reset --soft HEAD~1

Removes commit

Keeps staged files

Mixed (default)

git reset HEAD~1

Removes commit

Keeps files unstaged

Hard

git reset --hard HEAD~1

Deletes commit

Deletes working directory changes

Very dangerous.

Git Checkout

Older command used for

Switch branches

git checkout feature

Restore file

git checkout app.py

Nowadays Git recommends

git switch

and

git restore

instead.

Quick Comparison
Command	History Changes	Safe?	Use Case
git revert	Adds new commit	✅ Yes	Undo public commits
git reset	Rewrites history	⚠️ Sometimes	Undo local commits
git checkout / git switch	No	✅ Yes	Switch branches or restore files
7. Interactive Rebase (git rebase -i)

Interactive rebase lets you edit commit history before sharing it.

Command

git rebase -i HEAD~5

Git opens something like

pick a1 First commit
pick b2 Second commit
pick c3 Third commit
pick d4 Fourth commit
pick e5 Fifth commit

You can replace pick with other actions.

1. Reorder Commits

Simply rearrange the lines.

Before

pick A
pick B
pick C

After

pick B
pick A
pick C

Git replays them in the new order.

2. Squash

Combine commits while keeping both commit messages (you can edit the final message).

pick A
squash B
squash C

Result

A+B+C
3. Fixup

Like squash, but discards the commit message of the fixup commits.

pick A
fixup B
fixup C

Useful for small follow-up fixes like "fix typo" or "address review comments".

4. Edit

Pause during the rebase so you can modify a commit.

edit A
pick B

Git stops after replaying A. You can:

# Make changes
git add .
git commit --amend
git rebase --continue
5. Reword

Change only the commit message.

reword A

Git prompts you to enter a new message without changing the commit's content.

Continue After Resolving Conflicts

If a conflict occurs during rebase:

# Resolve the conflict manually
git add .

git rebase --continue

To skip the problematic commit:

git rebase --skip

To cancel the entire rebase:

git rebase --abort
Interview Summary
Topic	Best Practice
Merge	Use for shared branches; preserves complete history.
Rebase	Use on your local/private branch to create a clean, linear history before merging.
Fast-forward Merge	Happens when the target branch has no new commits; no merge commit is created.
3-Way Merge	Happens when both branches diverged; creates a merge commit.
Squash	Combine many small commits into one meaningful commit before merging.
Merge Conflicts	Resolve conflicts manually, stage the resolved files, then continue the merge or rebase.
Cherry-pick	Copy one or more specific commits from another branch without merging the whole branch.
Revert	Safely undo changes by creating a new commit; preferred for shared repositories.
Reset	Move the branch pointer backward; use cautiously, especially with --hard.
Checkout/Switch/Restore	Use git switch for branches and git restore for files; git checkout is the older, multifunction command.
Interactive Rebase	Reorder, squash, fixup, edit, or reword commits to produce a clean commit history before sharing.
