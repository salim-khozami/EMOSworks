import numpy as np
# import HyperProTool as hyper
import scipy.io as sio
#from LRSR_1 import LRSR

import matplotlib.pyplot as plt
from matplotlib.collections import EventCollection

# data pre-precessing
data = sio.loadmat("Sandiego.mat")
data3d = np.array(data["Sandiego"], dtype=float)

# normalise data set [0,1]
for idx in range(400):
    norm = np.linalg.norm(data3d[idx][:][:])
    normal_array = data3d[idx][:][:]/norm
    data3d[idx][:][:] = normal_array

xdata = np.linspace(400, 2500, num=224)
ydata = data3d[120,120,...].tolist()

# plot the data
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(xdata, ydata, color='tab:blue')

# set the limits
ax.set_xlim([400, 2500])
ax.set_ylim([0, 0.006])

ax.set_xlabel("Longueur d'onde (nm)", fontsize=15)
ax.set_ylabel("Valeur de transmittance", fontsize=15)

ax.set_title("Signature spectrale d'un pixel")

# display the plot
plt.show()
