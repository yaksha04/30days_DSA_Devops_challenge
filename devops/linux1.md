. The Filesystem Hierarchy
Linux follows a tree-like structure. Everything, including hardware, is treated as a file.

/etc: System-wide configuration files (e.g., /etc/passwd, /etc/shadow).

/var: Variable data (logs, mail spools, databases). Look here for /var/log/syslog.

/proc: A "virtual" filesystem containing runtime system information (process info, hardware).

/bin & /usr/bin: Executable binaries for all users.

/home: Personal directories for users.

2. File Permissions & Ownership
Linux uses a 3-tier permission system: User (u), Group (g), and Others (o).

Permission Types
Read (r): 4

Write (w): 2

Execute (x): 1

Commands to Master
chmod 755 script.sh: Sets rwx for owner, and r-x for group/others.

chown user:group file: Changes the ownership of a file.

umask: Defines the default permissions for newly created files.

3. Process Management
Interviewers love asking how to find and kill a "zombie" or "runaway" process.

ps aux: Displays every process running on the system.

top / htop: Real-time view of system resource usage (CPU, Memory).

kill -9 <PID>: Forcefully terminates a process using its Process ID.

&: Run a command in the background (e.g., ./script.sh &).

jobs: List background jobs.

fg %1: Bring job #1 to the foreground.

4. The "Holy Trinity": Grep, Awk, and Sed
These are essential for log analysis and text processing.

Grep (Global Regular Expression Print)
Used for searching patterns.

grep -i "error" log.txt: Search case-insensitive.

grep -r "main" .: Recursive search in current directory.

Sed (Stream Editor)
Used for find-and-replace or deleting lines.

sed 's/old/new/g' file.txt: Replace all occurrences of "old" with "new".

sed -i '5d' file.txt: Delete the 5th line of a file permanently.

Awk (Pattern Scanning & Processing)
Best for column-based data (like CSVs or logs).

awk '{print $1, $3}' file.txt: Print the 1st and 3rd columns.

awk '$3 > 50 {print $1}' file.txt: Print column 1 if column 3 is greater than 50.

5. Automation with Crontab
Crontab is used to schedule recurring tasks.

Format: * * * * * command_to_execute
(Minute, Hour, Day of Month, Month, Day of Week)

crontab -e: Edit the current user's cron jobs.

crontab -l: List active cron jobs.

Example: 0 0 * * * /backup.sh (Runs a backup every night at midnight).

6. System Services with Systemctl
systemctl is the interface for managing systemd, the init system for most modern Linux distros.

systemctl start/stop/restart <service>: Manage service state.

systemctl enable <service>: Ensure the service starts automatically on boot.

systemctl status <service>: Check if a service is running or why it failed.

journalctl -u <service>: View specific logs for a service.

Practice Scenarios (Interview Style)
Log Analysis: "Find all '404' errors in an Apache log and count how many times each unique IP appeared."

Solution: grep "404" access.log | awk '{print $1}' | sort | uniq -c

Permission Fix: "A script won't run because of 'Permission Denied'. How do you fix it safely?"

Solution: chmod +x script.sh

Process Cleanup: "Find the process using the most memory and kill it."

Solution: Use top, press M to sort by memory, note the PID, then kill -9 PID.
