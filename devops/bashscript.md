# 🐚 Bash Scripting Basics

> A beginner-friendly collection of Bash scripting concepts, commands, and examples for Linux automation.

---

## 📌 Overview

This repository contains the fundamentals of **Bash scripting**, one of the most important skills for Linux, DevOps, Cloud, and System Administration.

By completing these examples, you will learn how to automate repetitive tasks, manage files, work with variables, create reusable scripts, and write efficient shell programs.

---

## 📂 Topics Covered

- Introduction to Bash
- Creating and Running Scripts
- Comments
- Variables
- User Input
- Command Line Arguments
- Arithmetic Operations
- Conditional Statements
- Loops
- Functions
- Arrays
- Strings
- File Handling
- Case Statements
- Reading Files
- Exit Status
- Debugging Scripts
- Useful Bash Commands

---

## 📁 Project Structure

```
bash-scripting-basics/
│
├── 01-hello-world.sh
├── 02-variables.sh
├── 03-user-input.sh
├── 04-command-line-arguments.sh
├── 05-arithmetic.sh
├── 06-if-else.sh
├── 07-case.sh
├── 08-for-loop.sh
├── 09-while-loop.sh
├── 10-until-loop.sh
├── 11-functions.sh
├── 12-arrays.sh
├── 13-strings.sh
├── 14-file-handling.sh
├── 15-read-file.sh
├── 16-exit-status.sh
├── 17-debugging.sh
└── README.md
```

---

# 🚀 Getting Started

## Prerequisites

- Linux/macOS
- Git
- Bash Shell

Check Bash version:

```bash
bash --version
```

---

## Clone Repository

```bash
git clone https://github.com/yourusername/bash-scripting-basics.git

cd bash-scripting-basics
```

---

## Make Script Executable

```bash
chmod +x script.sh
```

Example

```bash
chmod +x 01-hello-world.sh
```

---

## Run Script

```bash
./01-hello-world.sh
```

or

```bash
bash 01-hello-world.sh
```

---

# 📖 Bash Basics

## Shebang

Every Bash script starts with

```bash
#!/bin/bash
```

---

## Print Output

```bash
echo "Hello World"
```

---

## Variables

```bash
name="Yaksha"

echo $name
```

---

## User Input

```bash
read name

echo "Hello $name"
```

---

## Command Line Arguments

```bash
echo $1
echo $2
echo $#
echo $@
```

Run

```bash
./script.sh DevOps AWS
```

---

## Arithmetic

```bash
a=10
b=20

echo $((a+b))
```

---

# 🔀 Conditional Statements

## If

```bash
if [ $a -gt $b ]
then
    echo "A is greater"
fi
```

---

## If Else

```bash
if [ $a -gt $b ]
then
    echo "A"
else
    echo "B"
fi
```

---

## If-Elif

```bash
if [ $marks -ge 90 ]
then
    echo "Grade A"
elif [ $marks -ge 70 ]
then
    echo "Grade B"
else
    echo "Grade C"
fi
```

---

# 🔁 Loops

## For Loop

```bash
for i in {1..5}
do
    echo $i
done
```

---

## While Loop

```bash
count=1

while [ $count -le 5 ]
do
    echo $count
    ((count++))
done
```

---

## Until Loop

```bash
count=1

until [ $count -gt 5 ]
do
    echo $count
    ((count++))
done
```

---

# ⚙️ Functions

```bash
greet(){

echo "Hello $1"

}

greet Yaksha
```

---

# 📦 Arrays

```bash
fruits=("Apple" "Banana" "Orange")

echo ${fruits[0]}
echo ${fruits[@]}
```

---

# 🔤 String Operations

Length

```bash
echo ${#name}
```

Substring

```bash
echo ${name:0:4}
```

Concatenation

```bash
full="$first $last"
```

---

# 📄 File Handling

Check if file exists

```bash
if [ -f file.txt ]
then
    echo "Exists"
fi
```

Create file

```bash
touch file.txt
```

Delete file

```bash
rm file.txt
```

---

# 📚 Reading File

```bash
while read line
do
    echo $line
done < file.txt
```

---

# 🚪 Exit Status

```bash
echo $?
```

Exit manually

```bash
exit 0
```

---

# 🐞 Debugging

Enable debugging

```bash
bash -x script.sh
```

or inside script

```bash
set -x
```

Disable

```bash
set +x
```

---

# 💡 Useful Bash Commands

| Command | Description |
|----------|-------------|
| pwd | Print current directory |
| ls | List files |
| cd | Change directory |
| mkdir | Create directory |
| rm | Remove files |
| cp | Copy files |
| mv | Move/Rename files |
| touch | Create file |
| cat | Display file |
| grep | Search text |
| find | Find files |
| chmod | Change permissions |
| chown | Change ownership |
| head | First lines |
| tail | Last lines |
| wc | Count words/lines |
| sort | Sort data |
| uniq | Remove duplicates |
| awk | Pattern scanning |
| sed | Stream editor |

---

# 🎯 Learning Outcomes

After completing this repository, you'll be able to:

- Write Bash scripts confidently
- Automate repetitive Linux tasks
- Work with variables and user input
- Implement conditions and loops
- Create reusable functions
- Manipulate files and directories
- Debug Bash scripts
- Build a strong foundation for DevOps and Linux Administration

---

# 📚 Resources

- GNU Bash Documentation
- Linux Manual Pages (`man bash`)
- ShellCheck (Linting Tool)

---

# ⭐ If you found this repository helpful

Give it a ⭐ on GitHub and share it with others learning Linux and DevOps!

---

## 👨‍💻 Author

**Yaksha Tikoria**

Aspiring DevOps & Cloud Engineer

- Linux
- Bash
- Docker
- Kubernetes
- AWS
- Terraform
- Jenkins
- CI/CD
```
