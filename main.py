import timeit
import random

# https://www.geeksforgeeks.org/python-program-for-insertion-sort/
def insertionSort(arr):
    n = len(arr)  # Get the length of the array

    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j + 1] = key  # Insert the key in the correct position

# https://www.programiz.com/dsa/merge-sort
def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

size = 250

test_list = list(range(1, size+1))
random.shuffle(test_list)

def run_insertionSort(arr):
    insertionSort(arr.copy())

def run_mergeSort(arr):
    mergeSort(arr.copy())

insertionSort_times = timeit.repeat(lambda: run_insertionSort(test_list), number=1, repeat=10)
mergeSort_times = timeit.repeat(lambda: run_mergeSort(test_list), number=1, repeat=10)

print(f"Average Insertion Sort time: {sum(insertionSort_times) / len(insertionSort_times)}")
print(f"Average Merge Sort time:     {sum(mergeSort_times) / len(mergeSort_times)}")


