import matplotlib.pyplot as plt
import numpy as np

amount = 15

lst = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)

n = len(lst)
for i in range(n-1):
    for j in range(0, n-i-1):
        plt.bar(x, lst)
        plt.pause(0.01)
        plt.clf()
        mini = i
        for j in range(i+1, n):
            if lst[j] < lst[mini]:
                mini = j
                lst[i], lst[mini] = lst[mini], lst[i]

plt.show()