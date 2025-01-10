import numpy as np
import matplotlib.pyplot as plt

q = np.arange(-2 * np.pi, 2 * np.pi, np.pi / 20)
eq_1 = -2 * np.cos(q) + np.sin(q)
eq_2 = 2 * np.cos(q) + 5 * np.sin(q)

fig = plt.figure(figsize=(8, 8))
pl = fig.add_subplot(111)
pl.set_xlabel("Q")
pl.set_ylabel("p")

pl.plot(q, eq_1, label='eq 1')
pl.plot(q, eq_2, label='eq 2')
q_intersect = -1 * np.pi / 4
pl.plot(q_intersect, -2 * np.cos(q_intersect) + np.sin(q_intersect), marker="x", markersize=10,
          label='intersection')

pl.grid()
pl.legend()
plt.show()
