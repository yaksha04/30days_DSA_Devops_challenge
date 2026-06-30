1. Process Life Cycle & States

A process is simply a running instance of a program.

Example:

python app.py

creates a process.

A process goes through several states during its lifetime.

           +---------+
           | Created |
           +---------+
                 |
                 v
          +--------------+
          |   Runnable   |
          +--------------+
                 |
      Scheduler selects it
                 |
                 v
          +--------------+
          |   Running    |
          +--------------+
           |     |      |
           |     |      |
     Waiting   Exit   Stopped
Process States

Run

ps aux

or

ps -eo pid,ppid,state,cmd

Example

PID  PPID S CMD
1010   1  S nginx
1022   1  R python
1040   1  D mysql
1055   1  Z java

The S column represents the process state.

R = Running / Runnable
R

Means

currently executing on CPU
OR waiting for CPU scheduling

Linux has many more runnable processes than CPUs.

Example

Suppose

4 CPU cores
100 processes

Only 4 actually execute.

The remaining 96 are still R because they are ready to run.

Example

Chrome
VS Code
Docker
Python

All waiting for CPU

The Linux scheduler continuously switches between them.

S = Interruptible Sleep

Most common state.

S

Means

The process is waiting for something.

Examples

keyboard input
network packet
database response
user request
timer

Example

Web server

Nginx

After sending a webpage it waits for another request.

It enters

S

When a client connects

Kernel wakes it instantly.

This is called interruptible because an event interrupts the sleep.

D = Uninterruptible Sleep

One of the most important interview concepts.

D

Means

Waiting for kernel I/O.

Usually

Disk
NFS
SAN Storage
EBS volume
Filesystem

The kernel does not allow interruption because stopping the process in the middle of a critical disk operation could leave data corrupted.

Example

Application

↓

Write 5GB file

↓

Disk becomes slow

↓

Process enters D state
Why SIGKILL doesn't work

Interviewers love asking this.

Example

kill -9 1245

Nothing happens.

Why?

Because the kernel isn't scheduling the process in user space. It's blocked inside a kernel system call waiting for I/O to complete. Signals are only acted upon when the process returns to a point where the kernel can deliver them.

Usually the only fix is

wait for I/O
repair storage
reboot if storage is permanently hung
T = Stopped
T

Paused.

Example

CTRL + Z

or

kill -STOP PID

Resume

kill -CONT PID

Useful for debugging.

Z = Zombie

Extremely popular interview question.

Zombie means

Process finished.

But parent hasn't collected exit status.

Example

Parent
   |
   +---- Child

Child exits.

Kernel keeps

PID
exit code

until parent executes

wait()

After wait()

Zombie disappears.

Why keep Zombie?

Because parent may need to know

Did child succeed?

Exit code?

Error?

Without storing it temporarily, the information would be lost.

Example

Parent creates child

fork()

Child

Downloads file

↓

Exits

Parent never calls

wait()

Result

Zombie

Check

ps aux | grep Z

or

ps -el | grep Z
Problems caused by Zombies

Zombie uses almost no CPU or RAM.

But it still occupies

PID

Process table entry

Thousands of zombies can exhaust available process IDs or fill the process table, preventing new processes from being created.

Fix

Find parent

ps -o ppid= -p <zombie_pid>

Option 1

Restart parent.

Option 2

Kill parent

kill parentPID

When the parent exits, the zombie is adopted and reaped by PID 1 (or another designated init process such as systemd), which calls wait() and removes it.

Sending SIGCHLD to the parent may help only if the parent is programmed to handle it correctly. It is not a universal fix.

Orphan Process

Suppose

Parent

↓

Child

Parent crashes.

Child still running.

Kernel automatically assigns

PPID = 1

(or to the system's init/subreaper such as systemd).

PID 1 eventually cleans it up after it exits.

No memory leak.

No issue.

Interview question

Difference?

Zombie

Dead process

Still in process table

Orphan

Alive process

Parent dead

Adopted by PID 1
2. Kernel Signals

Signals are asynchronous notifications sent to a process to tell it something happened or request a particular action.

Think of them as operating system messages.

SIGTERM (15)

Default

kill PID

actually sends

SIGTERM

Purpose

Please exit nicely.

Application gets time to

close files
flush logs
close database connections
release locks
save data
clean temporary files

This is always the preferred first choice.

Example

Java application

Receives SIGTERM

↓

Stops accepting traffic

↓

Completes active requests

↓

Writes logs

↓

Disconnects database

↓

Exit

Graceful shutdown.

SIGKILL (9)
kill -9 PID

Kernel immediately destroys the process.

Cannot be

ignored
caught
handled

No cleanup.

Example

File half written

↓

kill -9

↓

Program disappears

Data loss possible.

Use only when necessary.

Interview question

Why can't process catch SIGKILL?

Because the kernel never gives the process a chance to run signal-handling code. The kernel terminates it immediately.

SIGSTOP

Pauses execution.

Example

kill -STOP PID

Program freezes.

Resume

kill -CONT PID

Useful during debugging.

Other important signals
Signal	Number (common on Linux)	Purpose
SIGINT	2	Sent by Ctrl+C to interrupt a foreground process
SIGTERM	15	Graceful termination request
SIGKILL	9	Immediate, uncatchable termination
SIGSTOP	19	Pause process (uncatchable)
SIGCONT	18	Resume a stopped process
SIGHUP	1	Traditionally terminal hangup; often used by daemons to reload configuration
SIGCHLD	17	Sent to a parent when a child exits or changes state

Note: Signal numbers can vary slightly across Unix-like systems, but the signal names and meanings are portable.

3. Production Troubleshooting Scenario

Interview

EC2 instance is slow. SSH hangs. Users complain.

How do you debug?

Step 1

Login

Run

top

See

load average

CPU

Memory

Processes
CPU Section

Example

%Cpu(s):

80 us
10 sy
5 id
5 wa

Meaning

Field	Meaning
us	User processes
sy	Kernel work
id	Idle
wa	Waiting for disk I/O
High CPU

Sort

P

or

top

then press

Shift + P

Find

Python 300%

Java 250%

Node 150%

Investigate

ps -fp PID
High Memory

Press

Shift + M

Largest memory first.

Step 2

If RAM nearly full

Example

Mem

31GB used

32GB total

Linux may invoke the Out Of Memory (OOM) Killer.

Check

dmesg -T | grep -i oom

Possible output

Out of memory

Killed process 1456 java

The kernel killed a process to free memory.

Ask

Why memory leak?

Cache?

Huge JVM heap?

Container limits?
Step 3

CPU low

But machine slow.

Look

%wa

Suppose

40%

Huge problem.

CPU is idle because it's waiting for disk operations to complete.

Check

iostat -x 1 10

Important fields

Field	Meaning
%util	Disk busy percentage. Near 100% indicates saturation.
await	Average time (ms) for I/O requests to complete. High values indicate slow storage.
r/s	Reads per second
w/s	Writes per second

Example

%util

100%

await

700ms

Storage bottleneck.

Find process

iotop

Output

mysqld

150 MB/s

Now you know

Database overwhelming EBS
If SSH hangs completely

Possible causes

CPU saturated
Memory exhausted and heavy swapping
Disk stuck (high %wa)
Network issues
Storage problems (EBS/NFS)
Kernel deadlock or driver issues

Useful commands

uptime          # Check load average
free -h         # Memory and swap usage
vmstat 1        # CPU, memory, swap, I/O overview
top             # Process activity
iostat -x 1     # Disk performance
iotop           # Per-process disk I/O
dmesg -T        # Kernel messages
journalctl -xe  # System logs (on systemd systems)
