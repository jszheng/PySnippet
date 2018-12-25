'''
Created on 2018年8月9日

@author: Freedom
'''
from PyQt5.QtWidgets import QWidget
from PyQt5.Qt import QPixmap, QPainter, QPoint, QPaintEvent, QMouseEvent, QPen,\
    QColor, QSize
from PyQt5.QtCore import Qt

class PaintBoard(QWidget):


    def __init__(self, Parent=None):
        '''
        Constructor
        '''
        super().__init__(Parent)

        self.__InitData() #先初始化数据，再初始化界面
        self.__InitView()
        
    def __InitView(self):
        self.setFixedSize(self.__size)
        
    def __InitData(self):
        
        self.__size = QSize(480,460)
        
        self.__board = QPixmap(self.__size) #新建QPixmap作为画板，宽350px,高250px
        self.__board.fill(Qt.white) #用白色填充画板
        
        self.__IsEmpty = True #默认为空画板 
        self.EraserMode = False #默认为禁用橡皮擦模式
        
        self.__lastPos = QPoint(0,0)
        self.__currentPos = QPoint(0,0)
        
        self.__painter = QPainter()
        
        self.__thickness = 10       #默认画笔粗细为10px
        self.__penColor = QColor("black")       #设置默认画笔颜色为黑色
        self.__colorList = QColor.colorNames() #获取颜色列表
        
    def Clear(self):
        #清空画板
        self.__board.fill(Qt.white)
        self.update()
        self.__IsEmpty = True
        
    def ChangePenColor(self, color="black"):
        #改变画笔颜色
        self.__penColor = QColor(color)
        
    def ChangePenThickness(self, thickness=10):
        #改变画笔粗细
        self.__thickness = thickness
        
    def IsEmpty(self):
        #返回画板是否为空
        return self.__IsEmpty
    
    def GetContentAsQImage(self):
        #获取画板内容（返回QImage）
        image = self.__board.toImage()
        return image
        
    def paintEvent(self, paintEvent):

        self.__painter.begin(self)
        self.__painter.drawPixmap(0,0,self.__board)
        self.__painter.end()
        
    def mousePressEvent(self, mouseEvent):
        
        self.__currentPos =  mouseEvent.pos()
        self.__lastPos = self.__currentPos
        
        
    def mouseMoveEvent(self, mouseEvent):
        self.__currentPos =  mouseEvent.pos()
        self.__painter.begin(self.__board)
        
        if self.EraserMode == False:
            #非橡皮擦模式
            self.__painter.setPen(QPen(self.__penColor,self.__thickness)) #设置画笔颜色，粗细
        else:
            #橡皮擦模式下画笔为纯白色，粗细为10
            self.__painter.setPen(QPen(Qt.white,10))
            
        self.__painter.drawLine(self.__lastPos, self.__currentPos)
        self.__painter.end()
        self.__lastPos = self.__currentPos
                
        self.update() #更新显示
        
    def mouseReleaseEvent(self, mouseEvent):
        self.__IsEmpty = False #画板不再为空
        