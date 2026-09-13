# Time Complexity Examples

# 1. O(1) - Constant
def constant_time(numbers):
    return numbers[0]


# 2. O(log n) - Logarithmic
def logarithmic_time(n):
    while n > 1:
        n = n // 2


# 3. O(n) - Linear
def linear_time(numbers):
    for number in numbers:
        print(number)


# 4. O(n log n) - Linearithmic
def n_log_n_time(numbers):
    return sorted(numbers)


# 5. O(n²) - Quadratic
def quadratic_time(numbers):
    for i in numbers:
        for j in numbers:
            print(i, j)


# 6. O(n³) - Cubic
def cubic_time(numbers):
    for i in numbers:
        for j in numbers:
            for k in numbers:
                print(i, j, k)


# 7. O(2ⁿ) - Exponential
def exponential_time(n):
    if n <= 1:
        return n

    return exponential_time(n - 1) + exponential_time(n - 2)


# 8. O(n!) - Factorial
def factorial_time(n):
    if n == 0:
        return 1

    return n * factorial_time(n - 1)

# Main Program

numbers = [10, 20, 30, 40, 50]

print("O(1):", constant_time(numbers))

logarithmic_time(100)
print("O(log n): Completed")

print("O(n):")
linear_time(numbers)

print("O(n log n):", n_log_n_time(numbers))

print("O(n²):")
quadratic_time([1, 2, 3])

print("O(n³):")
cubic_time([1, 2])

print("O(2ⁿ):", exponential_time(5))

print("O(n!):", factorial_time(5))
