# Complexity Guide

## 1. What is Complexity?

When we write a program, we want to know:

- How much time will the program take?
- How much memory will the program use?

This is where complexity analysis comes in.

There are two main types:

- **Time Complexity** → How the running time grows as input gets bigger.
- **Space Complexity** → How the memory usage grows as input gets bigger.

## 2. First Understand "Input Size"

Suppose you have a list:

```python
[10, 20, 30, 40, 50]
```

There are 5 elements. We call the number of elements `n`.

```text
n = 5
```

If the list is:

```python
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```

Then:

```text
n = 10
```

If there are 1,000 elements:

```text
n = 1000
```

So `n` simply means the size of the input.

## 3. Time Complexity

Time complexity tells us how the number of operations in our program grows when the input size increases.

It does not usually mean exact seconds.

For example, this program:

```python
print("Hello")
```

performs roughly one simple operation.

Whether your computer is fast or slow, the basic amount of work doesn't depend on the size of some input.

We call this:

```text
O(1)
```

Read it as: **Big O of 1**.

## 4. What is Big O?

Big O notation is a way of describing complexity.

The most common ones you'll see in DSA are:

| Big O | Name | Simple Meaning |
| --- | --- | --- |
| `O(1)` | Constant | Same amount of work |
| `O(log n)` | Logarithmic | Work grows very slowly |
| `O(n)` | Linear | Work grows with `n` |
| `O(n log n)` | Linearithmic | Common in efficient sorting |
| `O(n²)` | Quadratic | Work grows roughly `n × n` |
| `O(2ⁿ)` | Exponential | Becomes very large very quickly |
| `O(n!)` | Factorial | Extremely fast growth |

For beginners, focus first on:

```text
O(1), O(n), O(n²), O(log n), O(n log n)
```

## 5. O(1) - Constant Time

Consider:

```python
def get_first(arr):
    return arr[0]
```

Suppose:

```python
arr = [10, 20, 30, 40, 50]
```

We get the first element.

Now suppose:

```python
arr = [10, 20, 30, ..., 1,000,000]
```

We still only access `arr[0]`.

The size of the list doesn't significantly change the amount of work.

Therefore:

```text
Time Complexity = O(1)
```

### Example

```python
x = 10
y = 20
z = x + y
```

Constant number of operations: `O(1)`.

Think: **Input grows, work stays roughly the same.**

## 6. O(n) - Linear Time

Now consider:

```python
def print_all(arr):
    for x in arr:
        print(x)
```

Suppose `n = 5`. We print:

```text
10
20
30
40
50
```

That's approximately 5 operations.

If `n = 100`, approximately 100 operations. If `n = 1,000`, approximately 1,000 operations.

So:

```text
n elements → n operations
```

Therefore:

```text
Time Complexity = O(n)
```

### Easy way to remember

One loop over `n` elements = `O(n)`.

```python
for i in range(n):
    print(i)
```

is `O(n)`.

## 7. O(n²) - Quadratic Time

Now look at this:

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

We have two loops.

Suppose `n = 5`. First loop runs 5 times. For every first-loop iteration, the second loop runs 5 times.

```text
5 × 5 = 25 operations
```

If `n = 100`:

```text
100 × 100 = 10,000 operations
```

Therefore: `O(n²)`.

### Important rule

Two nested loops often mean `O(n²)`.

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

```text
= O(n²)
```

## 8. Visualize O(n) vs O(n²)

Suppose:

| `n = 10` | Operations |
| --- | ---: |
| `O(n)` | 10 operations |
| `O(n²)` | `10 × 10 = 100` operations |

Now:

| `n = 1000` | Operations |
| --- | ---: |
| `O(n)` | 1,000 operations |
| `O(n²)` | `1,000 × 1,000 = 1,000,000` operations |

This is why we care about complexity. An algorithm that works fine for 10 elements may become extremely slow for 1 million elements.

## 9. O(log n) - Logarithmic Time

This one is extremely important in DSA.

Think about a dictionary. Suppose you're searching for the word:

```text
"computer"
```

You don't normally start from the first word and check every word. Instead, you might open somewhere in the middle.

If your word comes before that page, you go to the first half. If it comes after, you go to the second half.

You repeatedly divide the search area. This is the basic idea behind Binary Search.

### Example

```text
1 2 3 4 5 6 7 8
```

Looking for 7. Check middle:

```text
4
```

7 is bigger, so ignore:

```text
1 2 3
```

Now search:

```text
5 6 7 8
```

Check middle. You keep eliminating approximately half of the remaining elements.

Therefore:

```text
Binary Search = O(log n)
```

### Key idea

Every step cuts the problem roughly in half.

## 10. O(n log n)

This is commonly seen in efficient sorting algorithms.

For example:

```text
Merge Sort → O(n log n)
```

You don't need to understand Merge Sort yet. Just remember `O(n log n)` is generally much better than `O(n²)` for large inputs.

## 11. Comparing Common Complexities

Imagine `n = 1000`.

Roughly:

| Complexity | Amount of work |
| --- | ---: |
| `O(1)` | 1 |
| `O(log n)` | ~10 |
| `O(n)` | 1,000 |
| `O(n log n)` | ~10,000 |
| `O(n²)` | 1,000,000 |
| `O(2ⁿ)` | Enormous |

The exact number isn't the main point. The important thing is how quickly the work grows.

## 12. A Very Important Rule: Ignore Constants

Suppose:

```python
for i in range(n):
    print(i)

for i in range(n):
    print(i)
```

First loop: `O(n)`

Second loop: `O(n)`

Together:

```text
O(n) + O(n)
= O(2n)
```

But in Big O we normally ignore the constant 2:

```text
O(2n) → O(n)
```

Therefore: `O(n)`.

## 13. Another Example

```python
for i in range(n):
    print(i)

for j in range(n):
    print(j)

for k in range(n):
    print(k)
```

Technically:

```text
O(n) + O(n) + O(n)
= O(3n)
```

Ignore the constant: `O(n)`.

So the answer is: `O(n)`.

## 14. Nested Loops Are Different

Look at:

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Here the loops are inside each other. Therefore:

```text
O(n) × O(n)
= O(n²)
```

Remember this:

**Separate loops** → usually ADD

```text
O(n) + O(n) = O(n)
```

**Nested loops** → usually MULTIPLY

```text
O(n) × O(n) = O(n²)
```

This is one of the most useful beginner rules.

## 15. What is Space Complexity?

Now let's talk about memory.

Space complexity asks: **How much extra memory does our algorithm need as the input gets bigger?**

For example:

```python
def print_numbers(arr):
    for x in arr:
        print(x)
```

We aren't creating another large data structure. We're simply using a variable: `x`.

So the extra space is constant.

```text
Space Complexity = O(1)
```

## 16. Example of O(n) Space

Consider:

```python
def copy_array(arr):
    new_arr = []

    for x in arr:
        new_arr.append(x)

    return new_arr
```

Suppose the input contains `n = 5`. We create another array containing 5 elements.

If `n = 1000`, we create an array containing 1000 elements.

Therefore:

```text
Space Complexity = O(n)
```

Because the extra memory grows with `n`.

## 17. Time vs Space

This distinction is extremely important.

**Time Complexity** asks: How much work does the program do?

**Space Complexity** asks: How much extra memory does the program need?

Example:

```python
def find_number(arr, target):
    for x in arr:
        if x == target:
            return True

    return False
```

Worst case, we check every element:

```text
Time = O(n)
```

But we don't create another array:

```text
Space = O(1)
```

So:

```text
Time Complexity:  O(n)
Space Complexity: O(1)
```

## 18. Another Example

```python
def duplicate(arr):
    result = []

    for x in arr:
        result.append(x)

    return result
```

The loop runs `n` times:

```text
Time = O(n)
```

We create another array of size `n`:

```text
Space = O(n)
```

Therefore:

```text
Time Complexity:  O(n)
Space Complexity: O(n)
```

## 19. Best Case, Average Case, Worst Case

Suppose we have:

```python
def search(arr, target):
    for x in arr:
        if x == target:
            return True

    return False
```

Array:

```python
[10, 20, 30, 40, 50]
```

Searching for `10`, we find it immediately. That's the best case: `O(1)`.

Now search for `50`. We check:

```text
10
20
30
40
50
```

That's the worst case: `O(n)`.

For DSA questions, when they don't specify otherwise, worst-case complexity is commonly what you're expected to give.

## 20. Best, Average, Worst

| Case | Meaning |
| --- | --- |
| Best Case | Luckiest situation |
| Average Case | Typical situation |
| Worst Case | Maximum work required |

For the search example:

```text
Best:    O(1)
Average: O(n)
Worst:   O(n)
```

## 21. Why Do We Use Big O?

Suppose one computer takes 0.001 seconds and another takes 0.01 seconds.

Exact execution time depends on many things:

- Computer speed
- Processor
- Programming language
- Operating system
- Compiler
- Other running programs

So instead of focusing on exact seconds, DSA focuses on growth.

For example:

```text
Algorithm A → O(n)
Algorithm B → O(n²)
```

For small input, both might seem fast. For huge input, `O(n²)` can become much slower.

## 22. Simple Real-Life Example

Imagine you have 100 students and want to find a student named Rahul.

### Method 1: Check one by one

```text
Student 1
Student 2
Student 3
...
```

Could require checking all 100. That's `O(n)`.

### Method 2: Students are sorted alphabetically

You can repeatedly divide the list in half. That's similar to binary search: `O(log n)`.

So the second method scales much better.

## 23. Complexity Cheat Sheet

### O(1)

```python
arr[0]
```

Constant work.

### O(n)

```python
for i in range(n):
    print(i)
```

One loop.

### O(n²)

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Nested loops.

### O(log n)

Binary Search. Problem repeatedly gets divided.

### O(n log n)

Merge Sort and Heap Sort. Common efficient sorting complexity.

## 24. How to Find Time Complexity Step by Step

When you see code, follow this process.

### Step 1: Find the input size

Usually: `n`

### Step 2: Look at loops

One loop: `O(n)`

Two nested loops: `O(n²)`

### Step 3: Look for repeated division

Something like:

```text
n → n/2 → n/4 → n/8
```

usually indicates: `O(log n)`.

### Step 4: Ignore constants

```text
O(5n) → O(n)
O(100n²) → O(n²)
```

### Step 5: Keep the dominant term

For example:

```text
O(n² + n + 10)
```

The biggest-growing term is `n²`.

Therefore: `O(n²)`.

## 25. Dominant Term

This is very important.

Suppose:

```text
O(n² + n)
```

As `n` becomes very large, `n²` grows much faster than `n`. So we keep: `O(n²)`.

Similarly:

```text
O(n³ + n² + n) → O(n³)
O(n log n + n) → O(n log n)
```

## 26. One More Important Example

Consider:

```python
for i in range(n):
    print(i)

for i in range(n):
    for j in range(n):
        print(i, j)
```

First part: `O(n)`

Second part: `O(n²)`

Together:

```text
O(n + n²)
```

Keep the dominant term: `O(n²)`.

Therefore:

```text
Time Complexity = O(n²)
```

## 27. The Most Important Things to Remember

If you're starting DSA, remember these rules first:

1. `O(1)` — Constant work
2. `O(n)` — One loop over `n`
3. `O(n²)` — Two nested loops
4. `O(log n)` — Repeatedly divide by 2
5. `O(n log n)` — Common efficient sorting
6. Ignore constants: `O(5n) → O(n)`
7. Keep the biggest term: `O(n² + n) → O(n²)`

And:

```text
Time Complexity → How work grows
Space Complexity → How extra memory grows
```