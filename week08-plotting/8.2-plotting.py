import matplotlib.pyplot as plt
import numpy as np

xpoints = np.arange(1, 101)
ypoints = xpoints**2

plt.plot(xpoints,ypoints)
plt.show()