1. Git Architecture

Git has three main areas:

                git add            git commit
Working Directory ----------> Staging Area ----------> Local Repository
        ↑                                                |
        |                                                |
        ------------ git checkout ------------------------
Working Directory

This is where you actually edit files.

Example

project/
   app.py
   Dockerfile
   README.md

You modify files here.

Git knows they changed but they are not ready to commit.

Check:

git status

Example

modified: app.py
Staging Area (Index)

The staging area is a temporary area where you choose what will go into the next commit.

Think of it like a shopping cart.

Working directory = supermarket

Staging area = shopping cart

Commit = checkout bill

Example

Edit file
↓

git add app.py
↓

Staged
↓

git commit
Local Repository

This contains the complete history.

commit A
↓

commit B
↓

commit C

Each commit stores

author
timestamp
message
snapshot
2. git init

Creates a new Git repository.

mkdir project

cd project

git init

Output

Initialized empty Git repository

Git creates

.git/

Inside

objects/
refs/
HEAD
config
logs/
hooks/

The .git folder stores the entire history.

Delete it

rm -rf .git

Git history disappears.

3. git clone

Downloads an existing repository.

git clone https://github.com/user/project.git

Git performs

Download commits

↓

Download branches

↓

Download files

↓

Configure origin

↓

Checkout latest commit

Now you have

project/
.git/
4. git add

Moves changes into staging.

Example

echo "Hello" >> app.py

git add app.py

Only app.py is staged.

Stage everything

git add .

Stage all tracked files

git add -u

Interactive staging

git add -p

Very useful in interviews.

5. git commit

Creates a snapshot.

git commit -m "Added login API"

Git creates

Commit ID

↓

Parent Commit

↓

Author

↓

Message

↓

Snapshot

Example

A → B → C

Each commit points to its parent.

6. git push

Uploads local commits.

Local

A-B-C-D

↓

Push

↓

Remote

A-B-C-D

Command

git push origin main

Meaning

Push

to remote named origin

branch main
7. git pull

Downloads new commits.

Actually

git pull

=

git fetch

+

git merge

Flow

Remote updated

↓

Fetch

↓

Merge
8. Working Directory vs Staging Area

Suppose

app.py

Original

print("Hello")

You modify

print("Hello")

print("Linux")

Status

Working Directory

Modified

Not staged

Run

git add app.py

Now

Working Directory

Modified

↓

Staging Area

Ready for commit

Then

git commit

Stored permanently.

Comparison

Working Directory	Staging Area
Current files	Selected files
Editable	Ready to commit
Temporary	Snapshot preparation
9. HEAD Explained

HEAD means

"Where am I currently?"

Normally

HEAD

↓

main

↓

Commit C
A → B → C
          ↑
        HEAD

Current branch

git branch

Shows

* main

HEAD points to

main
10. origin Explained

Origin is simply the default remote.

Example

git clone https://github.com/user/project.git

Git creates

origin

↓

https://github.com/user/project.git

See remotes

git remote -v

Output

origin

You can rename it.

git remote rename origin github

Origin is not a special Git keyword—it's just the conventional default name for the remote repository.

11. Upstream Explained

Upstream is the branch your local branch tracks.

Example

Local

main

↓

tracks

↓

origin/main

Check

git branch -vv

Output

main origin/main

Now

git pull

Git already knows

Pull from origin/main

Without upstream

git pull origin main

every time.

Set upstream

git push -u origin main

-u

means

Remember this branch
12. Detached HEAD

Normally

HEAD

↓

main

↓

Commit C

Suppose

git checkout abc123

Now

HEAD

↓

Commit abc123

No branch.

This is Detached HEAD.

Diagram

A---B---C---D
     ↑
    HEAD

Why?

You checked out a commit directly.

Now if you commit

A-B-C-D

     E

E belongs to no branch.

Later

git checkout main

Commit E becomes unreachable unless you create a branch before leaving the detached HEAD state:

git switch -c my-fix

Use cases

inspect old code
debug old release
compare versions
test older commit
13. .gitignore

Tells Git

"Ignore these files."

Example

node_modules/

Git ignores the folder.

Example

*.log

Ignore all log files.

Common patterns

Ignore Python cache

__pycache__/

Ignore compiled Python

*.pyc

Ignore env

.env

Ignore VSCode

.vscode/

Ignore IntelliJ

.idea/

Ignore logs

*.log

Ignore all zip

*.zip

Ignore folder

build/

Ignore all PDFs

*.pdf

Negation

*.log

!important.log

Everything ignored except

important.log

Ignore only root

/temp

Only root temp.

Ignore everywhere

temp/

Every temp folder.

One important interview question

If a file is already tracked,

.gitignore

will not ignore it.

Need

git rm --cached filename

Then commit.

14. Git Config

Git stores configuration at three levels.

System (all users)
git config --system
Global (current user)
git config --global
Local (current repository)
git config --local

Priority:

Local
   ↑
Global
   ↑
System

The more specific level overrides the broader one.

Set username
git config --global user.name "John"
Set email
git config --global user.email "john@gmail.com"

Check configuration

git config --list

Check only username

git config user.name
Aliases

Instead of

git checkout

Use

git config --global alias.co checkout

Now

git co

Similarly

git config --global alias.st status
git config --global alias.cm commit
git config --global alias.br branch
git config --global alias.lg "log --oneline --graph --decorate"

Then

git st
git cm
git br
git lg
15. Git Stash

Stash temporarily saves uncommitted changes without creating a commit.

Situation

Working

↓

Half done

↓

Urgent bug arrives

You cannot commit incomplete work.

Use

git stash

Now

Working Directory

↓

Clean

Switch branches.

Fix bug.

Come back.

Restore

git stash pop

Changes return.

Common commands

Save changes

git stash

Save with message

git stash push -m "WIP login feature"

List stashes

git stash list

Apply latest stash (keep it in stash list)

git stash apply

Apply and remove from stash list

git stash pop

Delete latest stash

git stash drop

Delete all stashes

git stash clear
Real-world use cases
Urgent production fix: You're halfway through a feature when a critical bug needs immediate attention. Stash your work, switch branches, fix the bug, then restore your changes.
Branch switching: Git may prevent switching branches if your changes would conflict. Stash, switch, then apply the stash on the new branch if needed.
Pulling remote updates safely: If you have local uncommitted changes that conflict with incoming changes, stash them, pull the latest updates, then reapply the stash.
Experimentation: Temporarily save your current work to test another idea without committing incomplete code.
Frequently Asked Git Interview Questions
Question	Short Answer
What is Git?	A distributed version control system that tracks changes in source code.
Difference between git pull and git fetch?	fetch downloads changes only; pull = fetch + merge (or rebase if configured).
What is HEAD?	A pointer to the current commit, usually through the currently checked-out branch.
What is origin?	The default name given to the remote repository after cloning.
What is an upstream branch?	The remote branch that a local branch tracks for push and pull operations.
What is a detached HEAD?	HEAD points directly to a commit instead of a branch.
Why use the staging area?	To selectively choose which changes go into the next commit.
Does .gitignore remove tracked files?	No. It only prevents new untracked files matching the patterns from being tracked.
When should you use git stash?	To temporarily save uncommitted work without creating a commit.
