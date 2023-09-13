import matplotlib.pyplot as plt
import numpy as np
import random

amount = 50

arr = [random.randint(0, 1000) for _ in range(amount)]

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    l = [0] * (n1)
    r = [0] * (n2)

    for i in range(n1):
        l[i] = arr[left + i]
    
    for j in range(n2):
        r[j] = arr[mid + j + 1]
    
    i, j, k = 0, 0, left

    while i < n1 and j < n2:
        if l[i] < r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = l[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = r[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2
        colors = ['r' if left <= i <= mid else 'g' if mid < i <= right else 'b' for i in range(amount)]
        plt.bar(list(range(amount)), arr, color=colors)
        plt.pause(0.0001)
        plt.clf()

        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)

        merge(arr, left, mid, right)

        plt.bar(list(range(amount)), arr, color=colors)
        plt.pause(0.0001)
        plt.clf()

merge_sort(arr, 0, len(arr)-1)

print(arr)

plt.bar(list(range(amount)), arr, color="g")
plt.show()