# Python Basics for Beginners 🐍
## Input, Output, Loops, Conditions, and Functions

---

# 1. Input and Output

## 🔹 Output in Python
Python uses the `print()` function to display output.

### Example:
```python
print("Hello World")
Multiple Values:
name = "Yaksha"
age = 20
print("Name:", name, "Age:", age)
🔹 Input in Python

Python uses the input() function to take user input.

Example:
name = input("Enter your name: ")
print("Hello", name)
Important:
input() always takes data as string
Convert Input:
age = int(input("Enter age: "))
salary = float(input("Enter salary: "))
2. Conditional Statements (if, else, elif)

Used to make decisions.

🔹 Syntax:
if condition:
    # code
elif condition:
    # code
else:
    # code
🔹 Example:
age = int(input("Enter age: "))

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
🔹 Multiple Conditions:
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
3. Loops in Python

Loops are used to repeat tasks.

🔁 3.1 While Loop
🔹 Syntax:
while condition:
    # code
🔹 Example:
i = 1
while i <= 5:
    print(i)
    i += 1
🔹 Infinite Loop (Be Careful ⚠️)
while True:
    print("This runs forever")
🔹 Break Statement:

Stops the loop

i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1
🔹 Continue Statement:

Skips current iteration

i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
🔁 3.2 For Loop

Used for iterating over sequences.

🔹 Example:
for i in range(5):
    print(i)
Output:
0 1 2 3 4
🔹 Range Variations:
range(start, stop, step)
Example:
for i in range(1, 10, 2):
    print(i)
4. Functions in Python

Functions help reuse code.

🔹 Syntax:
def function_name(parameters):
    # code
    return value
🔹 Example:
def greet():
    print("Hello User")

greet()
🔹 Function with Parameters:
def greet(name):
    print("Hello", name)

greet("Yaksha")
🔹 Function with Return Value:
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
🔹 Default Parameters:
def greet(name="User"):
    print("Hello", name)

greet()
greet("Yaksha")
🔹 Keyword Arguments:
def student(name, age):
    print(name, age)

student(age=20, name="Yaksha")
5. Summary
Topic	Key Concept
Input	input()
Output	print()
Conditions	if, elif, else
Loops	while, for
Functions	def, return
