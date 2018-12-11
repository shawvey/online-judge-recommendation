import sys

# 这里为了方便，直接全部Import进来
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ExampleWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 去窗口边框
        self.setWindowFlags(Qt.FramelessWindowHint)
    def mousePressEvent(self, event):
        if event.button()== Qt.LeftButton:
            self.m_drag=True
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag=False

    def drawShadow(self,painter):
        #绘制左上角、左下角、右上角、右下角、上、下、左、右边框
        self.pixmaps=list()
        self.pixmaps.append(str("images/left_top.png"))
        self.pixmaps.append(str("images/left_bottom.png"))
        self.pixmaps.append(str("images/right_top.png"))
        self.pixmaps.append(str("images/right_bottom.png"))
        self.pixmaps.append(str("images/top_mid.png"))
        self.pixmaps.append(str("images/bottom_mid.png"))
        self.pixmaps.append(str("images/left_mid.png"))
        self.pixmaps.append(str("images/right_mid.png"))

        painter.drawPixmap(0, 0, self.SHADOW_WIDTH, self.SHADOW_WIDTH, QPixmap(self.pixmaps[0]))   #左上角
        painter.drawPixmap(self.width()-self.SHADOW_WIDTH, 0, self.SHADOW_WIDTH, self.SHADOW_WIDTH, QPixmap(self.pixmaps[2]))   #右上角
        painter.drawPixmap(0,self.height()-self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.SHADOW_WIDTH, QPixmap(self.pixmaps[1]))   #左下角
        painter.drawPixmap(self.width()-self.SHADOW_WIDTH, self.height()-self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.SHADOW_WIDTH, QPixmap(self.pixmaps[3]))  #右下角
        painter.drawPixmap(0, self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.height()-2*self.SHADOW_WIDTH, QPixmap(self.pixmaps[6]).scaled(self.SHADOW_WIDTH, self.height()-2*self.SHADOW_WIDTH)) #左
        painter.drawPixmap(self.width()-self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.height()-2*self.SHADOW_WIDTH, QPixmap(self.pixmaps[7]).scaled(self.SHADOW_WIDTH, self.height()- 2*self.SHADOW_WIDTH)) #右
        painter.drawPixmap(self.SHADOW_WIDTH, 0, self.width()-2*self.SHADOW_WIDTH, self.SHADOW_WIDTH, QPixmap(self.pixmaps[4]).scaled(self.width()-2*self.SHADOW_WIDTH, self.SHADOW_WIDTH)) #上
        painter.drawPixmap(self.SHADOW_WIDTH, self.height()-self.SHADOW_WIDTH, self.width()-2*self.SHADOW_WIDTH, self.SHADOW_WIDTH, QPixmap(self.pixmaps[5]).scaled(self.width()-2*self.SHADOW_WIDTH, self.SHADOW_WIDTH))   #下

    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawShadow(painter)
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.white)
        painter.drawRect(QRect(self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.width()-2*self.SHADOW_WIDTH, self.height()-2*self.SHADOW_WIDTH))

if __name__ == '__main__':

    #sys.argv参数是一个来自命令行的参数列表。Python脚本可以在shell中运行
    app = QApplication(sys.argv)

    w = ExampleWindow()
    sys.exit(app.exec_())
