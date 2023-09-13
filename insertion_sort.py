import matplotlib.pyplot as plt
import numpy as np
import random

amount = 30

arr = [random.randint(0, 100) for _ in range(amount)]
print(arr)

def insertion_sort(arr):
    plt.bar(list(range(amount)), arr)
    plt.pause(0.1)
    plt.clf()

    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
        colors = ['b' if k == j or k == j + 1 else 'r' for k in range(amount)]
        plt.bar(list(range(amount)), arr, color=colors)
        plt.pause(0.1)
        plt.clf()

insertion_sort(arr)
plt.bar(list(range(0, amount)), arr, color="orange")
plt.show()