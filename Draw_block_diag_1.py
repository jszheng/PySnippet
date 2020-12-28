# plan to draw floorplan

from zoom_pan import *
import matplotlib.pyplot as plt


if __name__ == '__main__':
    fig, ax = plt.subplots()
    fig.canvas.set_window_title("L1VK")
    fig.set_tight_layout(True)

    scale = 1.1
    zp = ZoomPan()
    figZoom = zp.zoom_factory(ax, base_scale=scale)
    figPan = zp.pan_factory(ax)

