import matplotlib.pyplot as plt
import numpy as np

amount = 20

lst = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)

n = len(lst)
for i in range(n):
    for j in range(0, n-i-1):
        colors = ['b' if k == j or k == j + 1 else 'r' for k in range(amount)]
        plt.bar(x, lst, color=colors)
        plt.pause(0.0001)
        plt.clf()
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

plt.show()