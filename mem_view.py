import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from zoom_pan import ZoomPan
from heatmap import heatmap

# Memory Configuration
n_channel = 32
n_bank = 16
n_row_size = 2^10
n_col_size = 2^10

# r/g
harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                    [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                    [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                    [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])
harvest = np.random.rand(128, 300)
ysize, xsize = harvest.shape
ylabel = [str(i) for i in range(ysize)]
xlabel = [str(i) for i in range(xsize)]


fig, ax = plt.subplots()
zp = ZoomPan()
figZoom = zp.zoom_factory(ax)
figPan = zp.pan_factory(ax)

im = ax.imshow(harvest)

# Turn spines off and create white grid.
for edge, spine in ax.spines.items():
    spine.set_visible(False)

#im, cbar = heatmap(harvest)
ax.grid(which="minor", color="w", linestyle='-', linewidth=3)

ax.set_title("Harvest of local farmers (in tons/year)")
fig.tight_layout()
plt.show()
