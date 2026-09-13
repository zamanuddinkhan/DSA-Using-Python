# Space_Complexity.py

# O(1) - Constant Space
def constant_space(n):
    result = n * 2
    return result


# O(n) - Linear Space
def linear_space(n):
    numbers = []
    for i in range(n):
        numbers.append(i)
    return numbers


# O(n^2) - Quadratic Space
def quadratic_space(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        matrix.append(row)
    return matrix


# O(log n) - Logarithmic Space
def logarithmic_space(n):
    if n <= 1:
        return
    logarithmic_space(n // 2)


# O(n) - Recursive Space
def recursive_space(n):
    if n <= 0:
        return
    recursive_space(n - 1)


# O(1) Auxiliary Space - In-Place
def reverse_in_place(numbers):
    left = 0
    right = len(numbers) - 1

    while left < right:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left += 1
        right -= 1

    return numbers


# O(n) Auxiliary Space
def copy_list(numbers):
    new_list = []

    for number in numbers:
        new_list.append(number)

    return new_list


# O(n) Space - Set
def create_set(numbers):
    result = set()

    for number in numbers:
        result.add(number)

    return result


# O(n) Space - Dictionary
def create_dictionary(numbers):
    result = {}

    for number in numbers:
        result[number] = number

    return result


# O(n) Recursive Space
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


# O(1) Space - Iterative Fibonacci
def fibonacci_iterative(n):
    a = 0
    b = 1

    for i in range(n):
        a, b = b, a + b

    return a


# Main Program
if __name__ == "__main__":

    n = 5
    numbers = [1, 2, 3, 4, 5]

    print("O(1):", constant_space(n))

    print("O(n):", linear_space(n))

    print("O(n^2):")
    for row in quadratic_space(n):
        print(row)

    logarithmic_space(16)
    print("O(log n): Completed")

    recursive_space(n)
    print("O(n) Recursion: Completed")

    print("In-Place Reverse:", reverse_in_place(numbers))

    print("Copy List:", copy_list(numbers))

    print("Set:", create_set(numbers))

    print("Dictionary:", create_dictionary(numbers))

    print("Recursive Fibonacci:", fibonacci(5))

    print("Iterative Fibonacci:", fibonacci_iterative(5))
