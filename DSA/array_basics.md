ARRAY BASICS (Straight to the point)
💡 What is an Array?

👉 A collection of elements stored in contiguous memory
👉 Access using index (starts from 0)

Example:

arr = [3, 7, 2, 9, 5]
Index	Value
0	3
1	7
2	2
3	9
4	5
🔑 Important Operations
1. Traversal
for i in range(len(arr)):
    print(arr[i])
2. Access Element
print(arr[2])  # 2
3. Update Element
arr[1] = 10
4. Insert (Python specific)
arr.append(8)
5. Delete
arr.pop()
🔥 FIND LARGEST ELEMENT (VERY IMPORTANT)
💡 Idea

👉 Compare each element and keep track of maximum

✅ Code (Optimized)
def find_largest(arr):
    max_element = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]

    return max_element
🧪 Dry Run
arr = [3, 7, 2, 9, 5]
Step	Current	max_element
Start	-	3
7 > 3	✔	7
2 > 7	❌	7
9 > 7	✔	9
5 > 9	❌	9

👉 Final Answer: 9

⏱ Time Complexity
O(n) → You must check all elements
👉 No shortcut here (unless sorted)
⚠️ Common Mistakes
Starting loop from 0 again ❌
Not initializing max properly ❌
Using wrong comparison ❌
💡 Shortcut (Python Built-in)
max(arr)

👉 But in interviews:
❌ Don’t use directly
✅ Show logic

🎯 Interview Insight

If interviewer asks:

“Find largest element”

And you say:

“I’ll iterate once and track max”

👉 That’s expected answer ✔️
