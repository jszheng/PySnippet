import matplotlib.pyplot as plt
import numpy as np

class ZoomPlot():

    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.xmin = -2.5; self.xmax = 1.0;
        self.ymin = -1.5; self.ymax = 1.5;
        self.xpress = self.xmin
        self.xrelease = self.xmax
        self.ypress = self.ymin
        self.yrelease = self.ymax
        self.resolution = 200
        self.maxiters = 30

        self.fig.canvas.mpl_connect('button_press_event', self.onpress)
        self.fig.canvas.mpl_connect('button_release_event', self.onrelease)
        self.plot_fixed_resolution(self.xmin, self.xmax,
                                   self.ymin, self.ymax)

    def mandlebrot(self, X, Y):
        C = X + Y*1j
        Z = C
        divtime = self.maxiters + np.zeros(Z.shape, dtype=int)
        for n in range(self.maxiters):
            Z = Z**2 + C
            diverge = Z*np.conj(Z) > 2**2
            div_now = diverge & (divtime == self.maxiters)
            divtime[div_now] = n
            Z[diverge] = 2

        return divtime

    def plot_fixed_resolution(self, x1, x2, y1, y2):
        x = np.linspace(x1, x2, self.resolution)
        y = np.linspace(y1, y2, self.resolution)
        X, Y = np.meshgrid(x, y)
        C = self.mandlebrot(X, Y)
        self.ax.clear()
        self.ax.set_xlim(x1, x2)
        self.ax.set_ylim(y1, y2)
        self.ax.pcolormesh(X, Y, C)
        self.fig.canvas.draw()

    def onpress(self, event):
        if event.button != 1: return
        self.xpress = event.xdata
        self.ypress = event.ydata

    def onrelease(self, event):
        if event.button != 1: return
        self.xrelease = event.xdata
        self.yrelease = event.ydata
        self.xmin = min(self.xpress, self.xrelease)
        self.xmax = max(self.xpress, self.xrelease)
        self.ymin = min(self.ypress, self.yrelease)
        self.ymax = max(self.ypress, self.yrelease)
        self.plot_fixed_resolution(self.xmin, self.xmax,
                                   self.ymin, self.ymax)


plot = ZoomPlot()
plt.show()