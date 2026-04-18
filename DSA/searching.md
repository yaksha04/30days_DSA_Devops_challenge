1. Linear Search
💡 Theory

Linear Search is the simplest searching technique.

👉 Idea:
You go element by element from start to end until you find the target.

Think like:
You’re searching your name in an attendance sheet — you don’t jump, you check one by one.

🧠 Algorithm Steps
Start from index 0
Compare each element with target
If found → return index
If not found till end → return -1
⏱ Time Complexity
Best Case: O(1) (found at first index)
Worst Case: O(n)
Average: O(n)

👉 Brutally honest:
This is slow for large data. Only useful when:

Data is small
Data is unsorted
💻 Python Code
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
🧪 Dry Run
arr = [4, 2, 7, 1, 9]
target = 7
Step	i	arr[i]	Compare with 7
1	0	4	❌
2	1	2	❌
3	2	7	✅ Found

👉 Output: 2

⚠️ When to Use

✔ Unsorted array
✔ Small datasets
❌ Large datasets (you’ll waste time like scrolling reels)

⚡ 2. Binary Search
💡 Theory

Binary Search is smart searching.

👉 Idea:
Divide the array into half again and again.

But condition:
🚨 Array must be sorted

🧠 Algorithm Steps
Take middle element
Compare with target
If equal → return
If target < mid → search left
If target > mid → search right
⏱ Time Complexity
Best Case: O(1)
Worst Case: O(log n) 🔥

👉 Honest truth:
This is what companies expect you to use when possible.

💻 Python Code (Iterative)
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
🧪 Dry Run
arr = [1, 2, 4, 7, 9]
target = 7
Step 1:
left = 0, right = 4
mid = 2 → arr[2] = 4
👉 7 > 4 → move right
Step 2:
left = 3, right = 4
mid = 3 → arr[3] = 7
👉 Found

👉 Output: 3
