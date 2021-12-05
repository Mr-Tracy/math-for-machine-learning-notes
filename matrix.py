import numpy as np
from matplotlib import pyplot as plt
a = np.array([[-1, 0],
              [0, 1]])

data = np.array([[1, 0], [0, 1]])
origin = np.array([[0, 0], [0, 0]])

res = np.matmul(a, data)
plt.quiver(*origin, data[:, 0], data[:, 1],
           color=['black'], label="x", scale=5)

plt.quiver(*origin, res[:, 0], res[:, 1],
           color=['blue', ], scale=5)

plt.margins(1.3, 1.4)
plt.autoscale()
plt.show()
print("done")
