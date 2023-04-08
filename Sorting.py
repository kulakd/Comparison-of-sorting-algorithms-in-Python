import random
import time

# Define the sorting algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

# Generate random data
n = random.randint(500, 1000)
data = [random.randint(1, 1000) for _ in range(n)]
repeats = random.randint(500, 1000)

# Time the sorting algorithms
start = time.time()
for i in range(repeats):
    bubble_sort(data.copy())
print(f"Bubblesort: {time.time() - start:.6f} seconds")

start = time.time()
for i in range(repeats):
    insertion_sort(data.copy())
print(f"InsertionSort: {time.time() - start:.6f} seconds")

start = time.time()
for i in range(repeats):
    shell_sort(data.copy())
print(f"ShellSort: {time.time() - start:.6f} seconds")

start = time.time()
for i in range(repeats):
    quick_sort(data.copy(), 0, n-1)
print(f"QuickSort: {time.time() - start:.6f} seconds")
