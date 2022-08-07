import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 5, 0.2, float)

plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'y^')
plt.show()