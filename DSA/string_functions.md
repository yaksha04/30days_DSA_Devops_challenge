What is a String?

A string is a sequence of characters.

s = "hello"
Strings are immutable (cannot be changed directly)
Indexed starting from 0
🔹 Basic String Operations
s = "hello"

print(s[0])        # h
print(s[-1])       # o
print(len(s))      # 5
print(s.upper())   # HELLO
print(s.lower())   # hello
🔹 String Traversal
for ch in "hello":
    print(ch)
🔹 String Slicing
s = "hello world"

print(s[0:5])   # hello
print(s[6:])    # world
print(s[::-1])  # reverse
🔥 IMPORTANT STRING DSA QUESTIONS
✅ 1. Reverse a String
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))
✅ 2. Check Palindrome
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # True
✅ 3. Count Vowels
def count_vowels(s):
    count = 0
    vowels = "aeiouAEIOU"
    
    for ch in s:
        if ch in vowels:
            count += 1
            
    return count
✅ 4. Remove Duplicates
def remove_duplicates(s):
    result = ""
    
    for ch in s:
        if ch not in result:
            result += ch
            
    return result
✅ 5. Check Anagram
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))
✅ 6. Find First Non-Repeating Character
def first_unique(s):
    for ch in s:
        if s.count(ch) == 1:
            return ch
    return None
✅ 7. Frequency of Characters
def char_frequency(s):
    freq = {}
    
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
        
    return freq
✅ 8. Longest Word in Sentence
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)
✅ 9. Convert String to Integer
def string_to_int(s):
    num = 0
    for ch in s:
        num = num * 10 + (ord(ch) - ord('0'))
    return num
✅ 10. Check Substring
def is_substring(s, sub):
    return sub in s
⚙️ FUNCTIONS IN DSA
🔹 What is a Function?

A function is a reusable block of code.

def greet():
    print("Hello")
🔹 Types of Functions
1. No parameters
def say_hi():
    print("Hi")
2. With parameters
def add(a, b):
    return a + b
3. Default parameters
def greet(name="User"):
    print("Hello", name)
4. Return multiple values
def calc(a, b):
    return a+b, a-b
🔥 IMPORTANT FUNCTION-BASED DSA QUESTIONS
✅ 1. Factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
✅ 2. Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
✅ 3. Power Function
def power(a, b):
    return a ** b
✅ 4. Sum of Array
def array_sum(arr):
    return sum(arr)
✅ 5. Find Maximum
def find_max(arr):
    return max(arr)
✅ 6. Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr)-1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1
