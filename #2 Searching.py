import time

# Linear Search
def linear_search(array, n, x):
    for i in range(n):
        if array[i] == x:
            return i
    return -1

array_linear = [2, 4, 0, 1, 9]
x_linear = 1
n_linear = len(array_linear)

start_linear = time.time()
result_linear = linear_search(array_linear, n_linear, x_linear)
end_linear = time.time()

if result_linear == -1:
    print("Element not found")
else:
    print("Element found at index:", result_linear)
print("Execution Time for Linear Search:", (end_linear - start_linear) * 1000, "milliseconds")

# Binary Search
def binary_search(array, x, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

array_binary = [3, 4, 5, 6, 7, 8, 9]
x_binary = 4

start_binary = time.time()
result_binary = binary_search(array_binary, x_binary, 0, len(array_binary) - 1)
end_binary = time.time()

if result_binary != -1:
    print("Element is present at index", result_binary)
else:
    print("Not found")
print("Execution Time for Binary Search:", (end_binary - start_binary) * 1000, "milliseconds")
