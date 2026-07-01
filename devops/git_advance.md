1. Git Hooks (pre-commit, pre-push, post-merge)

Git Hooks are scripts that run automatically when certain Git events occur.

They help automate tasks like:

Running tests
Checking code formatting
Preventing bad commits
Installing dependencies
Sending notifications

Hooks are stored inside:

.git/hooks/

Example:

.git/hooks/
├── pre-commit
├── pre-push
├── post-merge
├── commit-msg
├── pre-rebase

Git provides sample hook files ending in .sample. Rename them (or create new files) and make them executable.

chmod +x .git/hooks/pre-commit
A. pre-commit Hook

Runs before a commit is created.

If the script exits with a non-zero status, the commit is blocked.

Common Uses
Run linting
Run unit tests
Check formatting
Prevent secrets from being committed
Validate commit content

Example:

#!/bin/bash

echo "Running tests..."

pytest

if [ $? -ne 0 ]
then
    echo "Tests failed!"
    exit 1
fi

Flow:

git commit
      ↓
Run pre-commit
      ↓
Tests pass?
     / \
   Yes  No
    |    |
 Commit  Block commit
B. pre-push Hook

Runs before Git pushes commits to a remote repository.

Example:

git push

Hook executes first.

Common Uses

Run integration tests
Verify branch name
Check build success
Ensure no secrets are pushed

Example:

#!/bin/bash

npm test

If tests fail

Push cancelled
C. post-merge Hook

Runs after a successful merge.

Useful for updating the local environment.

Example

git pull

After merge

post-merge executes

Common Uses

Install dependencies
Rebuild project
Clear cache
Update generated files

Example

#!/bin/bash

npm install
Common Git Hooks
Hook	Runs When	Typical Use
pre-commit	Before commit	Linting, tests, formatting
commit-msg	Before commit message is saved	Enforce commit message conventions
pre-push	Before push	Run integration tests, security checks
post-merge	After merge	Install dependencies, refresh environment
post-checkout	After checkout	Regenerate files, update environment
pre-rebase	Before rebase	Validate whether rebase is allowed
Interview Tip

Hooks are local by default. They are not pushed with the repository, so teams usually manage shared hooks using tools like Husky, pre-commit, or custom scripts.

2. Git Bisect (Bug Hunting)

Imagine:

Today → Bug exists

Last week

Everything worked.

There are 500 commits.

Which one introduced the bug?

Instead of checking all 500 commits manually, Git Bisect performs a binary search, dramatically reducing the number of checks.

Binary Search Example
Commit 1 → Good
Commit 500 → Bad

Git checks

Commit 250

If good

Search

251–500

If bad

Search

1–249

This repeats until the first bad commit is found.

Commands

Start

git bisect start

Mark bad

git bisect bad

Mark good commit

git bisect good <commit>

Git automatically checks out intermediate commits.

After testing

If good

git bisect good

If bad

git bisect bad

Eventually

First bad commit:
a34c8d2

Finish

git bisect reset
Benefits
Very fast
Uses binary search
Excellent for debugging regressions
Works even with thousands of commits
3. Git Reflog (Recover Lost Commits)

Reflog records every movement of HEAD and branch references.

Even if a commit is no longer reachable from any branch (for example after a reset or rebase), it is often still recoverable through the reflog until Git eventually garbage-collects it.

Example

You accidentally run

git reset --hard HEAD~3

Three commits disappear from the branch history.

Use

git reflog

Output

a1b2c3 HEAD@{0}: reset: moving to HEAD~3
f4e5d6 HEAD@{1}: commit: Added login
789abc HEAD@{2}: commit: Fixed bug

Recover

git reset --hard HEAD@{1}

or

git checkout f4e5d6
Reflog vs Log
git log	git reflog
Shows reachable commit history	Shows local reference history (HEAD/branch movements)
Doesn't show deleted commits	Often helps recover "lost" commits
Shared history	Local only
Interview Question

Can Git recover deleted commits?

Yes.

If they still exist in the reflog (or another reference) and haven't been garbage-collected, they can often be recovered.

4. Git Submodules and Subtrees

Both allow one repository to use another repository, but they work differently.

A. Git Submodule

A submodule is a separate Git repository embedded inside another repository.

Example

Main Project
│
├── app/
├── docs/
└── shared-library/   ← Separate Git repo

Main repository stores only the commit pointer for the submodule.

Add

git submodule add <repository-url>

Clone

git clone <repo>
git submodule update --init --recursive
Advantages
Independent history
Independent releases
Reusable across many projects
Disadvantages
More complex workflow
Extra commands required
Easy for beginners to misuse
B. Git Subtree

Subtree copies another repository into your repository while preserving its history.

Example

Main Repository

src/
docs/
shared-lib/

Everything lives in one working tree.

Add

git subtree add --prefix=shared-lib <repository-url> main
Advantages
Easier for developers
No special clone commands
Simpler day-to-day workflow
Disadvantages
Repository becomes larger
Synchronizing upstream changes can require extra subtree commands
Submodule vs Subtree
Feature	Submodule	Subtree
Separate repository	Yes	No (contents are copied into the main repo)
Clone requires extra step	Yes	No
Easier to use	No	Yes
Best for	Shared libraries with independent lifecycles	Vendor code or simpler dependency management
5. Signed Commits with GPG

Normally

Author:
Yaksha

Anyone could configure Git with that name and email.

GPG signing proves that the commit was signed with the private key associated with your identity.

Why Sign Commits?
Verify author identity
Protect against commit spoofing
Increase trust in open-source projects
Meet security or compliance requirements

Platforms like GitHub can display a Verified badge for correctly signed commits.

Basic Steps

Generate a GPG key

gpg --full-generate-key

List keys

gpg --list-secret-keys --keyid-format=long

Configure Git

git config --global user.signingkey <KEY_ID>
git config --global commit.gpgsign true

Commit

git commit -S -m "Initial commit"
Interview Question

Why use signed commits?

To cryptographically verify the author and integrity of commits, reducing the risk of impersonation or tampering.

6. Git LFS (Large File Storage)

Git stores every version of every file.

Large binary files (videos, models, datasets, PSDs, ZIPs) make repositories huge because Git cannot efficiently delta-compress many binary formats.

Git LFS stores large files outside the main Git object database while Git tracks lightweight pointer files.

Examples

Good candidates

Machine learning models
Videos
Photoshop files
CAD files
Game assets
Large datasets
Install
git lfs install

Track

git lfs track "*.zip"

Commit

git add .gitattributes
git add large.zip
git commit -m "Add large file"
Advantages
Faster cloning
Smaller repository size
Better handling of binary assets
Limitations
Requires Git LFS support on the remote server
Storage and bandwidth quotas may apply on hosting platforms
7. Monorepo vs Polyrepo Strategies
Monorepo

One repository contains many related projects.

Example

company/

frontend/
backend/
mobile/
shared/
infra/
docs/

Everything lives in a single repository.

Advantages
Easier code sharing
Atomic cross-project changes
Unified CI/CD
Single source of truth
Disadvantages
Large repository
More complex CI/CD as the codebase grows
Requires tooling for scalability in very large organizations

Used by organizations such as Google (internally) and Meta (for many internal codebases).

Polyrepo

Each project has its own repository.

Example

frontend-repo
backend-repo
mobile-repo
infra-repo

Each repository has its own lifecycle.

Advantages
Smaller repositories
Independent releases
Separate access control
Simpler ownership boundaries
Disadvantages
Harder to coordinate changes spanning multiple repositories
Shared code often requires separate packages or libraries
More repository management overhead

Common in many startups and teams using microservices.

Monorepo vs Polyrepo
Feature	Monorepo	Polyrepo
Number of repositories	One	Many
Cross-project changes	Easy	Harder
Shared code	Simple	Package or library based
CI/CD	Centralized	Independent
Scalability	Requires specialized tooling at very large scale	Naturally isolated
Best for	Closely related projects with frequent collaboration	Independent services or teams with separate release cycles
Interview Summary
Topic	Key Takeaway
Git Hooks	Automate checks before/after Git events like commits, pushes, and merges.
Git Bisect	Uses binary search to quickly identify the commit that introduced a bug.
Git Reflog	Tracks local reference history and helps recover commits after resets or rebases.
Git Submodules	Embed and reference another Git repository while keeping separate history.
Git Subtrees	Copy another repository into your project with a simpler workflow.
Signed Commits (GPG)	Cryptographically verify commit authorship and integrity.
Git LFS	Store large binary files efficiently using lightweight pointers in Git.
Monorepo	One repository for many related projects; simplifies shared development.
Polyrepo	Multiple repositories with independent lifecycles; ideal for loosely coupled projects or teams.
