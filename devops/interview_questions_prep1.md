Linux & Shell Scripting
Easy
1. What's the difference between a process and a thread?
Process	Thread
Independent running program	Smallest execution unit inside a process
Has its own memory	Shares memory with other threads
Communication via IPC	Communicate through shared memory
More resource-intensive	Lightweight
Slower context switching	Faster context switching

Example

Chrome browser = Process
Each browser tab = Thread
2. How do you check disk usage in Linux?
df (Disk Filesystem)

Shows filesystem usage.

df -h

Output:

Filesystem      Size Used Avail Use%
/dev/sda1        50G  20G   28G 42%

Options:

-h → Human readable
-T → Filesystem type
du (Disk Usage)

Shows directory/file size.

du -sh /var/log
1.8G    /var/log

Useful:

du -h --max-depth=1
3. What does chmod 755 mean?

Permission format:

Owner  Group Others
7      5     5

Where

7 = 4+2+1 = rwx
5 = 4+1 = r-x

Meaning

Owner  -> Read Write Execute
Group  -> Read Execute
Others -> Read Execute

Common values

777 -> Everyone full access
755 -> Owner full, others read+execute
644 -> Owner read/write, others read only
600 -> Owner only
4. How do you find a file by name?

Using find

find /home -name "notes.txt"

Case insensitive

find /home -iname "notes.txt"

Search entire system

sudo find / -name "*.log"

Using locate (faster)

locate notes.txt

Update database

sudo updatedb
5. Difference between Soft Link and Hard Link?
Hard Link	Soft Link
Points to inode	Points to filename
Cannot cross filesystem	Can cross filesystem
Survives original deletion	Breaks if original deleted
Same inode	Different inode

Create

Hard link

ln file1 file2

Soft link

ln -s file1 shortcut
Medium
6. How do you check which process is using a specific port?

Using lsof

sudo lsof -i :8080

Using ss

ss -tulpn

Using netstat

netstat -tulpn

Kill process

kill -9 PID
7. Explain the Linux boot process.
BIOS/UEFI initializes hardware.
Bootloader (GRUB) loads.
GRUB loads Linux Kernel.
Kernel initializes CPU, memory, drivers.
Kernel mounts root filesystem.
Starts PID 1 (systemd or init).
Services start.
Login prompt appears.

Flow:

BIOS
 ↓
GRUB
 ↓
Kernel
 ↓
init/systemd
 ↓
Services
 ↓
User Login
8. How do you troubleshoot high CPU or memory usage?
CPU
top

or

htop

Find process

ps aux --sort=-%cpu
Memory
free -h

Processes

ps aux --sort=-%mem

Swap

vmstat

Disk I/O

iostat

Logs

journalctl

Interview answer:

I first identify the resource (CPU, memory, disk, or network), find the top-consuming processes using top, htop, or ps, inspect logs with journalctl, and then optimize, restart, or kill the problematic process if necessary.

9. Difference between > and >>

>

Overwrites file.

echo Hello > file.txt
Hello

Run again

echo Hi > file.txt

Output

Hi

>>

Appends.

echo Hello >> file.txt
echo Hi >> file.txt

Output

Hello
Hi
10. Cron jobs

Cron schedules jobs automatically.

Edit

crontab -e

Every 15 minutes

*/15 * * * * /home/user/script.sh

Format

Minute Hour Day Month Weekday

Example

0 2 * * * backup.sh

Runs every day at 2 AM.

Hard
11. Debug a memory leak in production

Steps

Check memory usage.
free -h
Find consuming process.
top
Check process memory.
ps aux --sort=-%mem
Inspect logs.
journalctl
If application-level:
Java → Heap dump (jmap)
C/C++ → valgrind
Python → tracemalloc
Go → pprof
Restart only if necessary after identifying the cause.

Interview answer: Use monitoring tools, identify the leaking process, inspect application memory using language-specific profilers, analyze logs, fix the root cause, and only then restart if required.

12. Zombie vs Orphan Process
Zombie

Finished process whose parent hasn't collected its exit status.

Parent
   |
Zombie

Shows as

Z

Fix

Parent calls wait()
Restart parent if required
Orphan

Parent dies before child.

Parent dies
      ↓
Child

Adopted by PID 1 (systemd).

Usually harmless.

13. Bash script to monitor disk usage
#!/bin/bash

THRESHOLD=80

usage=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')

if [ "$usage" -gt "$THRESHOLD" ]
then
echo "Disk usage crossed 80%: $usage%"
fi

For production, send an email:

mail -s "Disk Alert" admin@example.com

Schedule using cron every 15 minutes.

14. Explain inode exhaustion

Each file uses an inode.

Example

Filesystem

Space Used: 30%
Inodes Used:100%

You cannot create new files even if disk space is available.

Check

df -i

Find directories with many files

find /var -xdev -type f | wc -l

Fix

Delete unnecessary small files.
Archive logs.
Increase inode count by recreating the filesystem if needed (not usually feasible on a live filesystem).
Git & Version Control
Easy
1. Merge vs Rebase

Merge

A---B---C
     \
      D---E
           \
            Merge

Keeps history.

Command

git merge feature

Rebase

A---B---C---D---E

Linear history.

git rebase main

Interview answer: Use merge for preserving history and collaboration. Use rebase for keeping a clean, linear history before merging.

2. What is .gitignore?

Specifies files Git should ignore.

Example

*.log
.env
node_modules/
__pycache__/
3. How do you revert a commit?

Creates a new commit that undoes changes.

git revert <commit-id>

Safe for shared branches because history is preserved.

Medium
4. git reset --soft, --mixed, --hard

Suppose

Working Tree
Staging
Repository
Command	Working Tree	Staging	Commit
Soft	Keep	Keep	Move HEAD
Mixed	Keep	Reset	Move HEAD
Hard	Reset	Reset	Move HEAD

Examples

git reset --soft HEAD~1

Undo commit, keep changes staged.

git reset --mixed HEAD~1

Undo commit, keep changes unstaged (default).

git reset --hard HEAD~1

Delete commit and local changes permanently (unless recoverable via reflog).

5. Resolve merge conflict
git merge feature

Conflict markers

<<<<<<< HEAD
Current code
=======
Incoming code
>>>>>>> feature

Steps

Edit file.
Remove markers.
Save.
Stage.
git add file
Commit.
git commit
6. Git Hook

Scripts executed automatically on Git events.

Examples

pre-commit
commit-msg
pre-push
post-merge

Use case

Run tests or format code before commit.

7. Git branching strategies
GitFlow
main
develop
feature/*
release/*
hotfix/*

Best for large projects with planned releases.

Trunk-Based Development

Everyone commits frequently to main (or trunk), using feature flags if needed.

Best for CI/CD and fast releases.

Hard
8. Recover a deleted branch never pushed

Check reflog.

git reflog

Find the commit hash.

abc123

Recreate the branch.

git checkout -b feature abc123

If Git garbage collection has not removed the commit, recovery is usually possible.

9. Git internals (blobs, trees, commits)

Git stores data in .git/objects.

Blob: File contents.
Tree: Directory structure (maps names to blobs/trees).
Commit: Snapshot metadata (author, message, timestamp, parent commit, root tree).
Tag: Named reference to a commit.

Flow:

Commit
   │
 Tree
 ├── Blob (file1)
 ├── Blob (file2)
 └── Tree (subdir)
      └── Blob (file3)

This content-addressable storage (using SHA hashes) makes Git efficient and ensures object integrity.

10. Remove a large binary file from Git history

If the file is only in the latest commit and not pushed:

git rm --cached largefile.zip
git commit --amend

If it's already in history, rewrite history using:

git filter-repo --path largefile.zip --invert-paths

(or the older git filter-branch or the BFG Repo-Cleaner tool).

Then force-push:

git push --force --all
git push --force --tags
