import matplotlib.pyplot as plt
import time
import random

# Optimized Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # Stop if the array is already sorted
            break
    return arr

# In-place Quick Sort
def quick_sort_in_place(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    if low < high:
        pi = partition(arr, low, high)
        quick_sort_in_place(arr, low, pi - 1)
        quick_sort_in_place(arr, pi + 1, high)

# Hybrid Merge Sort with Insertion Sort for small subarrays
def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort_hybrid(arr, threshold=10):
    if len(arr) <= 1:
        return arr
    if len(arr) <= threshold:
        insertion_sort(arr)
        return arr

    mid = len(arr) // 2
    left = merge_sort_hybrid(arr[:mid])
    right = merge_sort_hybrid(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Visualization function for sorting algorithms
def visualize_sorting_algorithm(algorithm, arr, title):
    fig, ax = plt.subplots()
    ax.set_title(title)
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")

    def update_fig(arr):
        for rect, val in zip(bar_rects, arr):
            rect.set_height(val)
        plt.pause(0.05)

    algorithm(arr, update_fig)
    plt.show()

# Sorting algorithm wrappers for visualization
def bubble_sort_visual(arr, update_fig):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            update_fig(arr)
        if not swapped:
            break

def quick_sort_in_place_visual(arr, update_fig, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                update_fig(arr)
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        update_fig(arr)
        return i + 1

    if low < high:
        pi = partition(arr, low, high)
        quick_sort_in_place_visual(arr, update_fig, low, pi - 1)
        quick_sort_in_place_visual(arr, update_fig, pi + 1, high)

def merge_sort_hybrid_visual(arr, update_fig, threshold=10):
    if len(arr) <= 1:
        return arr
    if len(arr) <= threshold:
        insertion_sort(arr)
        update_fig(arr)
        return arr

    mid = len(arr) // 2
    left = merge_sort_hybrid_visual(arr[:mid], update_fig, threshold)
    right = merge_sort_hybrid_visual(arr[mid:], update_fig, threshold)
    merged = merge(left, right)
    for i in range(len(arr)):
        arr[i] = merged[i]
    update_fig(arr)
    return arr

# Test and visualize each sorting algorithm
test_arr = [64, 34, 25, 12, 22, 11, 90]
visualize_sorting_algorithm(bubble_sort_visual, test_arr.copy(), "Bubble Sort Visualization")
visualize_sorting_algorithm(quick_sort_in_place_visual, test_arr.copy(), "Quick Sort (In-Place) Visualization")
visualize_sorting_algorithm(merge_sort_hybrid_visual, test_arr.copy(), "Hybrid Merge Sort Visualization")

# Compare Performance
def compare_sorting_algorithms(arr):
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Quick Sort (In-Place)", quick_sort_in_place),
        ("Hybrid Merge Sort", merge_sort_hybrid)
    ]
    
    for name, func in algorithms:
        arr_copy = arr.copy()
        start_time = time.time()
        func(arr_copy)
        end_time = time.time()
        print(f"{name} took {end_time - start_time:.6f} seconds")

# Generate a large random array
large_arr = [random.randint(1, 1000) for _ in range(1000)]
# Compare the algorithms
compare_sorting_algorithms(large_arr)
