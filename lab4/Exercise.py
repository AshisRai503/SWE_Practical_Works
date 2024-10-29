import math
import time

#Linear Search
def linear_search(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices if indices else -1

#Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Finding insertion point for a target in a sorted list
def find_insertion_point(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

#Jump Search algorithm
def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[prev] == target:
        return prev
    return -1

# Comparision
def compare_search_algorithms(arr, target):
    # Linear Search
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time

    # Binary Search (sorted array)
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time

    # Jump Search (sorted array)
    start_time = time.time()
    jump_result = jump_search(arr_sorted, target)
    jump_time = time.time() - start_time

    print(f"Linear Search: Found at {linear_result}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at {binary_result}, Time: {binary_time:.6f} seconds")
    print(f"Jump Search: Found at {jump_result}, Time: {jump_time:.6f} seconds")

# Testing the functions
def main():
    test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    test_list_sorted = sorted(test_list)
    target = 5

    print("Testing Linear Search (All Indices):")
    linear_result = linear_search(test_list, target)
    print(f"Linear Search: Indices of {target} are {linear_result}")

    print("\nTesting Binary Search:")
    binary_result = binary_search(test_list_sorted, target)
    print(f"Binary Search: Index of {target} in sorted list is {binary_result}")

    print("\nTesting Jump Search:")
    jump_result = jump_search(test_list_sorted, target)
    print(f"Jump Search: Index of {target} in sorted list is {jump_result}")

    print("\nTesting Insertion Point Finder:")
    insertion_point = find_insertion_point(test_list_sorted, target)
    print(f"Insertion point for {target} in sorted list is at index {insertion_point}")

    print("\nPerformance Comparison:")
    large_list = list(range(10000))
    compare_search_algorithms(large_list, 8888)

if __name__ == "__main__":
    main()
