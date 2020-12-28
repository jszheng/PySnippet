class ZoomPan:
    def __init__(self):
        self.press = None
        self.cur_xlim = None
        self.cur_ylim = None
        self.x0 = None
        self.y0 = None
        self.x1 = None
        self.y1 = None
        self.xpress = None
        self.ypress = None

    def zoom_factory(self, ax, base_scale=1.1):
        def zoom(event):
            cur_xlim = ax.get_xlim()
            cur_ylim = ax.get_ylim()

            xdata = event.xdata  # get event x location
            ydata = event.ydata  # get event y location
            if xdata is None:
                return
            if ydata is None:
                return

            if event.button == 'up':
                # deal with zoom in
                scale_factor = 1 / base_scale
            elif event.button == 'down':
                # deal with zoom out
                scale_factor = base_scale
            else:
                # deal with something that should never happen
                scale_factor = 1
                print(event.button)

            new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
            new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor

            relx = (cur_xlim[1] - xdata) / (cur_xlim[1] - cur_xlim[0])
            rely = (cur_ylim[1] - ydata) / (cur_ylim[1] - cur_ylim[0])

            ax.set_xlim([xdata - new_width * (1 - relx), xdata + new_width * (relx)])
            ax.set_ylim([ydata - new_height * (1 - rely), ydata + new_height * (rely)])
            ax.figure.canvas.draw()

        fig = ax.get_figure()  # get the figure of interest
        fig.canvas.mpl_connect('scroll_event', zoom)

        return zoom

    def pan_factory(self, ax):
        def onPress(event):
            if event.inaxes != ax: return
            self.cur_xlim = ax.get_xlim()
            self.cur_ylim = ax.get_ylim()
            self.press = self.x0, self.y0, event.xdata, event.ydata
            self.x0, self.y0, self.xpress, self.ypress = self.press

        def onRelease(event):
            self.press = None
            ax.figure.canvas.draw()

        def onMotion(event):
            if self.press is None: return
            if event.inaxes != ax: return
            dx = event.xdata - self.xpress
            dy = event.ydata - self.ypress
            self.cur_xlim -= dx
            self.cur_ylim -= dy
            ax.set_xlim(self.cur_xlim)
            ax.set_ylim(self.cur_ylim)

            ax.figure.canvas.draw()

        fig = ax.get_figure()  # get the figure of interest

        # attach the call back
        fig.canvas.mpl_connect('button_press_event', onPress)
        fig.canvas.mpl_connect('button_release_event', onRelease)
        fig.canvas.mpl_connect('motion_notify_event', onMotion)

        # return the function
        return onMotion


# def on_draw(event):
#     bboxes = []
#     for label in labels:
#         bbox = label.get_window_extent()
#         # the figure transform goes from relative coords->pixels and we
#         # want the inverse of that
#         bboxi = bbox.inverse_transformed(fig.transFigure)
#         bboxes.append(bboxi)
#
#     # this is the bbox that bounds all the bboxes, again in relative
#     # figure coords
#     bbox = mtransforms.Bbox.union(bboxes)
#     if fig.subplotpars.left < bbox.width:
#         # we need to move it over
#         fig.subplots_adjust(left=1.1 * bbox.width)  # pad a little
#         fig.canvas.draw()
#     return False


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import matplotlib.transforms as mtransforms

    fig, ax = plt.subplots()
    fig.canvas.set_window_title("test zoom")
    fig.set_tight_layout(True)

    # ax.set_aspect('equal')

    # ax.spines['top'].set_color('none')
    # ax.spines['right'].set_color('none')
    # ax.xaxis.set_ticks_position('bottom')
    # ax.spines['bottom'].set_position(('data', 0))
    # ax.yaxis.set_ticks_position('left')
    # ax.spines['left'].set_position(('data', 0))
    # ax.set_title("")

    #scale = 1.1
    zp = ZoomPan()
    figZoom = zp.zoom_factory(ax)
    figPan = zp.pan_factory(ax)

    ############################################################
    rect1 = plt.Rectangle((0.1, 0.2), 0.2, 0.3, color='r')
    # 创建一个矩形，参数：(x,y),width,height
    circ1 = plt.Circle((0.7, 0.2), 0.15, color='r', alpha=0.3)
    # 创建一个椭圆，参数：中心点，半径，默认这个圆形会跟随窗口大小进行长宽压缩
    pgon1 = plt.Polygon([[0.45, 0.45], [0.65, 0.6], [0.2, 0.6]])
    # 创建一个多边形，参数：每个顶点坐标

    ax.add_patch(rect1)  # 将形状添加到子图上
    ax.add_patch(circ1)  # 将形状添加到子图上
    ax.add_patch(pgon1)  # 将形状添加到子图上

    ax.axis('equal')
    fig.canvas.draw()  # 子图绘制
    fig.tight_layout()
    ############################################################

    # maximize for Qt backend
    # figManager = plt.get_current_fig_manager()
    # figManager.window.showMaximized()

    # fig.canvas.mpl_connect('draw_event', on_draw)

    plt.show()
