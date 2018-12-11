# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\mac\Desktop\2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QWidget,QTableWidget, QApplication,QTableWidgetItem,QFont,QBrush,Qt,QColor,QAbstractItemView,QCoreApplication
import sqlite3
class Ui_Dialog4(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(795, 520)
        Dialog.setStyleSheet("background-color:rgb(252,253,253);")
        self.verticalWidget = QtWidgets.QWidget(Dialog)
        self.verticalWidget.setGeometry(QtCore.QRect(0, 30, 200, 490))
        self.verticalWidget.setMinimumSize(QtCore.QSize(200, 490))
        self.verticalWidget.setMaximumSize(QtCore.QSize(200, 490))
        self.verticalWidget.setStyleSheet("background: rgb(52,56,60);\n"
"")
            
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        
        self.graphicsView = QtWidgets.QGraphicsView(self.verticalWidget)
        self.graphicsView.setEnabled(False)
        self.graphicsView.setMinimumSize(QtCore.QSize(100, 100))
        self.graphicsView.setMaximumSize(QtCore.QSize(100, 100))
        self.graphicsView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.graphicsView.setAutoFillBackground(True)
        self.graphicsView.setStyleSheet("background-image: url(images/bear.png);\n"
"border-radius:50px;\n"
"")
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView, 0, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.verticalWidget)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font:bold;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
#        self.label_2 = QtWidgets.QLabel(self.verticalWidget)
#        self.label_2.setStyleSheet("color: rgb(242, 242, 242);")
#        self.label_2.setObjectName("label_2")
#        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignLeft)
        self.recommend = QtWidgets.QPushButton(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.recommend.sizePolicy().hasHeightForWidth())
        self.recommend.setSizePolicy(sizePolicy)
        self.recommend.setMinimumSize(QtCore.QSize(190, 23))
        self.recommend.setMaximumSize(QtCore.QSize(190, 16777215))
#        self.recommend.setGeometry(QtCore.QRect(0, 10, 190, 30))
        self.recommend.setStyleSheet("background: rgb(137,199,161);\n"
"color: rgb(250,250,250);\n"
"border-radius:4px;\n"
"font:\"微软雅黑\";\n"
"margin-left:10px;\n"
"font:bold;")
        self.recommend.setIconSize(QtCore.QSize(8, 8))
        self.recommend.setObjectName("recommend")
        self.recommend.clicked.connect(self.getRecommend)
        self.verticalLayout.addWidget(self.recommend)
        self.record = QtWidgets.QPushButton(self.verticalWidget)
        self.record.setMinimumSize(QtCore.QSize(190, 23))
        self.record.setMaximumSize(QtCore.QSize(180, 16777215))
        self.record.setStyleSheet("background: rgb(137,199,161);\n"
"color: rgb(250,250,250);\n"
"border-radius:4px;\n"
"font:\"微软雅黑\";\n"
"margin-left:10px;\n"
"font:bold;")
        self.record.setObjectName("record")
        self.verticalLayout.addWidget(self.record)
        self.record.clicked.connect(self.getRecord)
        self.problems = QtWidgets.QPushButton(self.verticalWidget)
        self.problems.setMinimumSize(QtCore.QSize(190, 23))
        self.problems.setMaximumSize(QtCore.QSize(190, 16777215))
        self.problems.setStyleSheet("background: rgb(137,199,161);\n"
"color: rgb(250,250,250);\n"
"border-radius:4px;\n"
"font:\"微软雅黑\";\n"
"margin-left:10px;\n"
"font:bold;")
        self.problems.setObjectName("problems")
        self.verticalLayout.addWidget(self.problems)
        self.problems.clicked.connect(self.getProblems)
        
        self.searchuser = QtWidgets.QPushButton(self.verticalWidget)
        self.searchuser.setMinimumSize(QtCore.QSize(190, 23))
        self.searchuser.setMaximumSize(QtCore.QSize(180, 16777215))
        self.searchuser.setStyleSheet("background: rgb(137,199,161);\n"
"color: rgb(250,250,250);\n"
"border-radius:4px;\n"
"font:\"微软雅黑\";\n"
"margin-left:10px;\n"
"font:bold;")
        self.searchuser.setObjectName("searchuser")
        self.verticalLayout.addWidget(self.searchuser)
        self.searchuser.clicked.connect(self.searchUser)
        
        self.searchpro = QtWidgets.QPushButton(self.verticalWidget)
        self.searchpro.setMinimumSize(QtCore.QSize(190, 23))
        self.searchpro.setMaximumSize(QtCore.QSize(180, 16777215))
        self.searchpro.setStyleSheet("background: rgb(137,199,161);\n"
"color: rgb(250,250,250);\n"
"border-radius:4px;\n"
"font:\"微软雅黑\";\n"
"margin-left:10px;\n"
"font:bold;")
        self.searchpro.setObjectName("searchpro")
        self.verticalLayout.addWidget(self.searchpro)
        self.searchpro.clicked.connect(self.searchPro)
        
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.main = QtWidgets.QWidget(Dialog)
        self.main.setGeometry(QtCore.QRect(200, 30, 595, 490))
        self.main.setObjectName("main")
        self.main.setStyleSheet("background: rgb(252,253,253);\n")
        self.aboutcontent = QtWidgets.QLabel(self.main)
        self.aboutcontent.setGeometry(QtCore.QRect(220, -130, 500, 400))
        self.aboutcontent.setStyleSheet("background: rgb(252,253,253);\n"
"color: black;\n"
"border-radius:4px;\n"
"font:bold;")
        self.aboutcontent.setObjectName("aboutcontent")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setGeometry(QtCore.QRect(0, 0, 595, 330))
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.recommendLabel=QtWidgets.QLabel(self.main)
        self.recommendLabel.setMaximumSize(QtCore.QSize(200, 28))
#        self.recommendLabel.setGeometry(QtCore.QRect(10, 30, 200, 28))
        self.recommendLabel.setStyleSheet("color: rgb(28,28,28);\n"
                                   "font: 10pt \"微软雅黑\";\n"
                                   "font:bold;")
        self.recommendLabel.setObjectName("label_4")
        self.recommendLabel.setVisible(False)
        self.verticalLayout_2.addWidget(self.recommendLabel, 1, QtCore.Qt.AlignHCenter)
        self.remindLabel=QtWidgets.QLabel(self.main)
        self.remindLabel.setMaximumSize(QtCore.QSize(200, 28))
        self.remindLabel.setStyleSheet("color: rgb(28,28,28);\n"
                                   "font: 11pt \"微软雅黑\";\n"
                                   "font:bold;")
        self.remindLabel.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.remindLabel, 1, QtCore.Qt.AlignHCenter)
        self.table = QtWidgets.QTableWidget(self.main)
        
#        self.table.setGeometry(QtCore.QRect(30, 30, 400, 490))
        self.table.setStyleSheet("border:1px\n"
"")
        self.table.setStyleSheet("background: rgb(252,253,253);\n"
                                 "border:1px;\n"
"")
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.verticalLayout_2.addWidget(self.table)
        self.table.verticalScrollBar().setStyleSheet("background:rgb(137,199,161,25%);border:1px;width:20px;font:black;")

        self.newrecord = QtWidgets.QTableWidget(self.main)
        self.newrecord.setGeometry(QtCore.QRect(0, 443, 595, 100))
        self.newrecord.setStyleSheet("border:1px\n"
"")
        self.newrecord.setObjectName("newrecord")
        self.newrecord.setColumnCount(3)
        self.newrecord.setRowCount(1)
        self.table.setSelectionMode(QTableWidget.NoSelection)
        self.newrecord.setSelectionMode(QTableWidget.NoSelection)
#        self.verticalLayout_2.addWidget(self.newrecord)
        self.horizontalFrame_2 = QtWidgets.QFrame(Dialog)
        
        self.horizontalFrame_2.setGeometry(QtCore.QRect(0, 0, 795, 35))
        self.horizontalFrame_2.setMinimumSize(QtCore.QSize(0, 35))
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalFrame_2.setStyleSheet("background: rgb(137,199,161);\n"
"")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
#        self.label = QtWidgets.QLabel(self.horizontalFrame_2)
#        self.label.setMinimumSize(QtCore.QSize(100, 0))
#        self.label.setMaximumSize(QtCore.QSize(100, 20))
#        self.label.setStyleSheet("font: 10pt \"华文琥珀\";\n"
#"font: 11pt \"华文彩云\";\n"
#"")
#        self.label.setObjectName("label")
#        self.horizontalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignVCenter)
        
        self.icon = QtWidgets.QGraphicsView(self.verticalWidget)
        self.icon.setEnabled(False)
        self.icon.setMaximumSize(QtCore.QSize(16, 16))
        self.icon.setAutoFillBackground(True)
        self.icon.setStyleSheet("background-image: url(images/AI.png);\n"
"border-radius:1px;\n")
        self.icon.setObjectName("graphicsView2")
        self.horizontalLayout_2.addWidget(self.icon, 0, QtCore.Qt.AlignLeft)
        
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalFrame_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(70, 20))
        self.pushButton_2.setStyleSheet("background: rgb(250,250,250);\n"
"color: rgb(137,199,161);\n"
"font:bold;\n"
"border-bottom: 2px solid rgb(137,199,161);\n"
"border-radius: 2px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(QCoreApplication.instance().quit)
        self.horizontalLayout_2.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignLeft)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.remindLabel.setVisible(False)
        self.aboutcontent.setVisible(False)
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        f=open(r'database/username.txt')
        username=f.read()
        f.close()
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", username))
#        self.label_2.setText(_translate("Dialog", " Navigation"))
        self.recommend.setText(_translate("Dialog", "推荐习题"))
        self.record.setText(_translate("Dialog", "做题记录"))
        self.problems.setText(_translate("Dialog", "AI酱题库"))
        self.searchuser.setText(_translate("Dialog", "查找用户"))
        self.searchpro.setText(_translate("Dialog", "查找题目"))
        self.recommendLabel.setText(_translate("Dialog", "算法练习题推荐"))
        self.remindLabel.setText(_translate("Dialog", "暂无做题记录"))
        self.pushButton_2.setText(_translate("Dialog", "关闭"))
#        self.aboutcontent.setText(_translate("Dialog", ""))
        self.newrecord.setVisible(False)
        self.recommendLabel.setVisible(True)
        self.recommendLabel.setVisible(True)
        self.connection = sqlite3.connect("database/oj.db")
        f=open(r'database/username.txt')
        username=f.read()
        f.close()
        Data2=self.connection.execute("SELECT id,proname,level,tags,round(acrate,9) FROM newrecord where username= '%s'"%username) 
        topTen=self.connection.execute("SELECT user1,user2,user3,user4,user5,user6,user7,user8,user9,user10 FROM firstrecommend WHERE username = '%s'"%username)
        topTen=topTen.fetchall()
        print(topTen)
        if topTen!=[]:
            self.connection.commit()
    #        print(Data)
            self.table.setRowCount(10)
            self.table.setColumnCount(6)
            self.table.setHorizontalHeaderLabels(['编号','题目名字','题目等级','题目标签','AC率','AC人数'])
            self.table.verticalHeader().setVisible(False)
    #        self.table.horizontalHeader().setVisible(False)
            self.table.horizontalHeader().setFixedHeight(25)
            for index in range(self.table.columnCount()):
                headItem = self.table.horizontalHeaderItem(index)
                headItem.setFont(QFont("song", 9, QFont.Bold))
                headItem.setForeground(QBrush(QColor( 137,199,161)))
                headItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) 
            self.table.setColumnWidth(0,40)
            self.table.setColumnWidth(1,120)
            self.table.setColumnWidth(2,90)
            self.table.setColumnWidth(3,186)
            self.table.setColumnWidth(4,98)
            self.table.setColumnWidth(5,60)
            self.table.setRowHeight(0,38)
            self.table.setRowHeight(1,38)
            self.table.setRowHeight(2,38)
            self.table.setRowHeight(3,38)
            self.table.setRowHeight(4,38)
            self.table.setRowHeight(5,38)
            self.table.setRowHeight(6,38)
            self.table.setRowHeight(7,38)
            self.table.setRowHeight(8,38)
            self.table.setRowHeight(9,38)
            for i in range(10):
                Data=self.connection.execute("SELECT id,name,level,tags,ACrate,AC FROM problem where id = '%s'"%topTen[0][i])
                Data=Data.fetchall()
                if i%2==0:
                    for j in range(6):
                        temp_data=Data[0][j]  #临时记录，不能直接插入表格
                        data=QTableWidgetItem(str(temp_data)) #转换后可插入表格
                        data.setBackground(QBrush(QColor(245, 245, 244)))
                        self.table.setItem(i,j,data)
                else:
                    for j in range(6):
                        temp_data=Data[0][j]  #临时记录，不能直接插入表格
                        data=QTableWidgetItem(str(temp_data)) #转换后可插入表格
                        data.setBackground(QBrush(QColor(254, 254, 254)))
                        self.table.setItem(i,j,data)
                    
            Data2=Data2.fetchall()
            row=len(Data2)  #取得记录个数，用于设置表格的行数
            vol=len(Data2[0])+1  #取得字段数，用于设置表格的列数
    #        print(row)
    #        print(vol)
            self.newrecord.setRowCount(row)
            self.newrecord.setColumnCount(vol)
            self.newrecord.setHorizontalHeaderLabels(['编号','题目名字','题目等级','标签','AC率','是否提交'])
            self.newrecord.verticalHeader().setVisible(False)
            self.newrecord.horizontalHeader().setVisible(False)
    #        self.table.horizontalHeader().setVisible(False)
            self.newrecord.horizontalHeader().setFixedHeight(40)
            for index in range(self.newrecord.columnCount()):
                headItem = self.newrecord.horizontalHeaderItem(index)
                headItem.setFont(QFont("song", 9, QFont.Bold))
                headItem.setForeground(QBrush(QColor( 137,199,161)))
                headItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.newrecord.setEditTriggers(QAbstractItemView.NoEditTriggers) 
            self.newrecord.setColumnWidth(0,40)
            self.newrecord.setColumnWidth(1,120)
            self.newrecord.setColumnWidth(2,90)
            self.newrecord.setColumnWidth(3,186)
            self.newrecord.setColumnWidth(4,98)
            self.newrecord.setColumnWidth(5,60)
            self.newrecord.setRowHeight(0,43)#设置i行的高度  
            for i in range(row):
                for j in range(vol-1):
                    if j<vol:
                        temp_data=Data2[i][j]  #临时记录，不能直接插入表格
                        print(temp_data)
                        data2=QTableWidgetItem(str(temp_data)) #转换后可插入表格
                        data2.setBackground(QBrush(QColor(250, 250, 250)))
                        self.newrecord.setItem(i,j,data2)
                    else:
                        data2=QTableWidgetItem(str(0)) #转换后可插入表格
                        self.newrecord.setItem(i,j,data2)    
            self.addButton = QtWidgets.QPushButton()
            self.addButton.setStyleSheet("background: rgb( 137,199,161);\n"
    "color: white;\n"
    "border-bottom: 2px solid rgb( 137,199,161);\n"
    "border-radius: 2px;"
    "font:bold;")
            self.addButton.setObjectName("pushButton1")
            self.addButton.setText("提交")
            self.addButton.clicked.connect(self.addbutton)
            self.newrecord.setCellWidget(0,5,self.addButton)  
            
            self.newrecord.setVisible(True)
            self.table.setVisible(True)
            self.aboutcontent.setVisible(False)
        else:
            self.table.setRowCount(10)
            self.table.setColumnCount(6)
            self.table.setHorizontalHeaderLabels(['编号','题目名字','题目等级','题目标签','AC率','AC人数'])
            self.table.verticalHeader().setVisible(False)
    #        self.table.horizontalHeader().setVisible(False)
            self.table.horizontalHeader().setFixedHeight(25)
            for index in range(self.table.columnCount()):
                headItem = self.table.horizontalHeaderItem(index)
                headItem.setFont(QFont("song", 9, QFont.Bold))
                headItem.setForeground(QBrush(QColor( 137,199,161)))
                headItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) 
            self.table.setColumnWidth(0,40)
            self.table.setColumnWidth(1,120)
            self.table.setColumnWidth(2,90)
            self.table.setColumnWidth(3,186)
            self.table.setColumnWidth(4,98)
            self.table.setColumnWidth(5,60)
            self.table.setRowHeight(0,38)
            self.table.setRowHeight(1,38)
            self.table.setRowHeight(2,38)
            self.table.setRowHeight(3,38)
            self.table.setRowHeight(4,38)
            self.table.setRowHeight(5,38)
            self.table.setRowHeight(6,38)
            self.table.setRowHeight(7,38)
            self.table.setRowHeight(8,38)
            self.table.setRowHeight(9,38)
            for i in range(10):
                Data=self.connection.execute("SELECT id,name,level,tags,ACrate,AC FROM begin;")
                Data=Data.fetchall()
                print(Data)
                if i%2==0:
                    for j in range(6):
                        temp_data=Data[i][j]  #临时记录，不能直接插入表格
                        data=QTableWidgetItem(str(temp_data)) #转换后可插入表格
                        data.setBackground(QBrush(QColor(245, 245, 244)))
                        self.table.setItem(i,j,data)
                else:
                    for j in range(6):
                        temp_data=Data[i][j]  #临时记录，不能直接插入表格
                        data=QTableWidgetItem(str(temp_data)) #转换后可插入表格
                        data.setBackground(QBrush(QColor(254, 254, 254)))
                        self.table.setItem(i,j,data)
            self.newrecord.setVisible(False)
            self.table.setVisible(True)
            self.aboutcontent.setVisible(False)
    def getRecommend(self):
        self.remindLabel.setVisible(False)
        self.recommendLabel.setVisible(True)
        self.aboutcontent.setVisible(False)
        self.connection = sqlite3.connect("database/oj.db")
        f=open(r'database/username.txt')
        username=f.read()
        f.close()
        Data2=self.connection.execute("SELECT id,proname,level,tags,round(acrate,9) FROM newrecord where username= '%s'"%username) 
        topTen=self.connection.execute("SELECT user1,user2,user3,user4,user5,user6,user7,user8,user9,user10 FROM firstrecommend WHERE username = '%s'"%username)
        topTen=topTen.fetchall()
        print(topTen)
        if topTen!=[]:
            self.connection.commit()
    #        print(Data)
            self.table.setRowCount(10)
            self.table.setColumnCount(6)
            self.table.setHorizontalHeaderLabels(['编号','题目名字','题目等级','题目标签','AC率','AC人数'])
            self.table.verticalHeader().setVisible(False)
    #        self.table.horizontalHeader().setVisible(False)
            self.table.horizontalHeader().setFixedHeight(25)
            for index in range(self.table.columnCount()):
                headItem = self.table.horizontalHeaderItem(index)
                headItem.setFont(QFont("song", 9, QFont.Bold))
                headItem.setForeground(QBrush(QColor( 137,199,161)))
                headItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) 
            self.table.setColumnWidth(0,40)
            self.table.setColumnWidth(1,120)
            self.table.setColumnWidth(2,90)
            self.table.setColumnWidth(3,186)
            self.table.setColumnWidth(4,98)
            self.table.setColumnWidth(5,60)
            self.table.setRowHeight(0,38)
            self.table.setRowHeight(1,38)
            self.table.setRowHeight(2,38)
            self.table.setRowHeight(3,38)
            self.table.setRowHeight(4,38)
            self.table.setRowHeight(5,38)
            self.table.setRowHeight(6,38)
            self.table.setRowHeight(7,38)
            self.table.setRowHeight(8,38)
            self.table.setRowHeight(9,38)
            for i in range(10):
                Data=self.connection.execute("SELECT id,name,level,tags,ACrate,AC FROM problem where id = '%s'"%topTen[0][i])
                Data=Data.fetchall()
                if i%2==0:
                    for j in range(6):
                        temp_data=Data[0][j]  #临时记录，不能直接插入表格
                        data=QTableWidgetItem(str(temp_data)) #转换后可插入表格
                        data.setBackground(QBrush(QColor(245, 245, 244)))
                        self.table.setItem(i,j,data)
                else:
                    for j in range(6):
                        temp_data=Data[0][j]  #临时记录，不能直接插入表格
                        data=QTableWidgetItem(str(temp_data)) #转换后可插入表格
                        data.setBackground(QBrush(QColor(254, 254, 254)))
                        self.table.setItem(i,j,data)
                    
            Data2=Data2.fetchall()
            row=len(Data2)  #取得记录个数，用于设置表格的行数
            vol=len(Data2[0])+1  #取得字段数，用于设置表格的列数
    #        print(row)
    #        print(vol)
            self.newrecord.setRowCount(row)
            self.newrecord.setColumnCount(vol)
            self.newrecord.setHorizontalHeaderLabels(['编号','题目名字','题目等级','标签','AC率','是否提交'])
            self.newrecord.verticalHeader().setVisible(False)
            self.newrecord.horizontalHeader().setVisible(False)
    #        self.table.horizontalHeader().setVisible(False)
            self.newrecord.horizontalHeader().setFixedHeight(40)
            for index in range(self.newrecord.columnCount()):
                headItem = self.newrecord.horizontalHeaderItem(index)
                headItem.setFont(QFont("song", 9, QFont.Bold))
                headItem.setForeground(QBrush(QColor( 137,199,161)))
                headItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.newrecord.setEditTriggers(QAbstractItemView.NoEditTriggers) 
            self.newrecord.setColumnWidth(0,40)
            self.newrecord.setColumnWidth(1,120)
            self.newrecord.setColumnWidth(2,90)
            self.newrecord.setColumnWidth(3,186)
            self.newrecord.setColumnWidth(4,98)
            self.newrecord.setColumnWidth(5,60)
            self.newrecord.setRowHeight(0,43)#设置i行的高度  
            for i in range(row):
                for j in range(vol-1):
                    if j<vol:
                        temp_data=Data2[i][j]  #临时记录，不能直接插入表格
                        print(temp_data)
                        data2=QTableWidgetItem(str(temp_data)) #转换后可插入表格
                        data2.setBackground(QBrush(QColor(250, 250, 250)))
                        self.newrecord.setItem(i,j,data2)
                    else:
                        data2=QTableWidgetItem(str(0)) #转换后可插入表格
                        self.newrecord.setItem(i,j,data2)    
            self.addButton = QtWidgets.QPushButton()
            self.addButton.setStyleSheet("background: rgb( 137,199,161);\n"
    "color: white;\n"
    "border-bottom: 2px solid rgb( 137,199,161);\n"
    "border-radius: 2px;"
    "font:bold;")
            self.addButton.setObjectName("pushButton1")
            self.addButton.setText("提交")
            self.addButton.clicked.connect(self.addbutton)
            self.newrecord.setCellWidget(0,5,self.addButton)  
            
            self.newrecord.setVisible(True)
            self.table.setVisible(True)
            self.aboutcontent.setVisible(False)
        else:
            self.table.setRowCount(10)
            self.table.setColumnCount(6)
            self.table.setHorizontalHeaderLabels(['编号','题目名字','题目等级','题目标签','AC率','AC人数'])
            self.table.verticalHeader().setVisible(False)
    #        self.table.horizontalHeader().setVisible(False)
            self.table.horizontalHeader().setFixedHeight(25)
            for index in range(self.table.columnCount()):
                headItem = self.table.horizontalHeaderItem(index)
                headItem.setFont(QFont("song", 9, QFont.Bold))
                headItem.setForeground(QBrush(QColor( 137,199,161)))
                headItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) 
            self.table.setColumnWidth(0,40)
            self.table.setColumnWidth(1,120)
            self.table.setColumnWidth(2,90)
            self.table.setColumnWidth(3,186)
            self.table.setColumnWidth(4,98)
            self.table.setColumnWidth(5,60)
            self.table.setRowHeight(0,38)
            self.table.setRowHeight(1,38)
            self.table.setRowHeight(2,38)
            self.table.setRowHeight(3,38)
            self.table.setRowHeight(4,38)
            self.table.setRowHeight(5,38)
            self.table.setRowHeight(6,38)
            self.table.setRowHeight(7,38)
            self.table.setRowHeight(8,38)
            self.table.setRowHeight(9,38)
            for i in range(10):
                Data=self.connection.execute("SELECT id,name,level,tags,ACrate,AC FROM begin;")
                Data=Data.fetchall()
                print(Data)
                if i%2==0:
                    for j in range(6):
                        temp_data=Data[i][j]  #临时记录，不能直接插入表格
                        data=QTableWidgetItem(str(temp_data)) #转换后可插入表格
                        data.setBackground(QBrush(QColor(245, 245, 244)))
                        self.table.setItem(i,j,data)
                else:
                    for j in range(6):
                        temp_data=Data[i][j]  #临时记录，不能直接插入表格
                        data=QTableWidgetItem(str(temp_data)) #转换后可插入表格
                        data.setBackground(QBrush(QColor(254, 254, 254)))
                        self.table.setItem(i,j,data)
            self.newrecord.setVisible(False)
            self.table.setVisible(True)
            self.aboutcontent.setVisible(False)
    def addbutton(self):
        self.connection = sqlite3.connect("database/oj.db")
        f=open(r'database/username.txt')
        username=f.read()
        f.close()
        topTen=self.connection.execute("SELECT user1,user2,user3,user4,user5,user6,user7,user8,user9,user10 FROM secondrecommend WHERE username = '%s'"%username)
#        print(topTen)
        self.connection.commit()
#        print(Data)
        topTen=topTen.fetchall()
        self.table.setRowCount(10)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(['编号','题目名字','题目等级','题目标签','AC率','AC人数'])
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setFixedHeight(25)
        for index in range(self.table.columnCount()):
            headItem = self.table.horizontalHeaderItem(index)
            headItem.setFont(QFont("song", 9, QFont.Bold))
            headItem.setForeground(QBrush(QColor( 137,199,161)))
            headItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        self.table.setColumnWidth(0,40)
        self.table.setColumnWidth(1,120)
        self.table.setColumnWidth(2,90)
        self.table.setColumnWidth(3,186)
        self.table.setColumnWidth(4,98)
        self.table.setColumnWidth(5,60)
        self.table.setRowHeight(0,38)
        self.table.setRowHeight(1,38)
        self.table.setRowHeight(2,38)
        self.table.setRowHeight(3,38)
        self.table.setRowHeight(4,38)
        self.table.setRowHeight(5,38)
        self.table.setRowHeight(6,38)
        self.table.setRowHeight(7,38)
        self.table.setRowHeight(8,38)
        self.table.setRowHeight(9,38)
        for i in range(10):
            Data=self.connection.execute("SELECT id,name,level,tags,ACrate,AC FROM problem where id = '%s'"%topTen[0][i])
            Data=Data.fetchall()
            if i%2==0:
                for j in range(6):
                    temp_data=Data[0][j]  #临时记录，不能直接插入表格
                    data=QTableWidgetItem(str(temp_data)) #转换后可插入表格
                    data.setBackground(QBrush(QColor(245, 245, 244)))
                    self.table.setItem(i,j,data)
            else:
                for j in range(6):
                    temp_data=Data[0][j]  #临时记录，不能直接插入表格
                    data=QTableWidgetItem(str(temp_data)) #转换后可插入表格
                    data.setBackground(QBrush(QColor(254, 254, 254)))
                    self.table.setItem(i,j,data)
    def getProblems(self):
        self.remindLabel.setVisible(False)
        self.recommendLabel.setVisible(False)
        self.newrecord.setVisible(False)
        self.table.setVisible(True)
        self.aboutcontent.setVisible(False)
        print('heregetproblem')
        self.connection = sqlite3.connect("database/oj.db")
        Data=self.connection.execute("SELECT id,name,level,tags,AC,ACrate FROM problem Order By id")
        self.connection.commit()
        Data=Data.fetchall()
        row=len(Data)  #取得记录个数，用于设置表格的行数
        vol=len(Data[0])  #取得字段数，用于设置表格的列数
        print(row)
        print(vol)
        self.table.setRowCount(row)
        self.table.setColumnCount(vol)
        self.table.setHorizontalHeaderLabels(['编号','题目名字','题目等级','题目标签','AC人数','AC率'])
        self.table.verticalHeader().setVisible(False)
#        self.table.horizontalHeader().setVisible(False)
        self.table.horizontalHeader().setFixedHeight(25) 
        for index in range(self.table.columnCount()):
            headItem = self.table.horizontalHeaderItem(index)
#            headItem.setBackground(QBrush(QColor(28, 28, 28)))
            headItem.setFont(QFont("song", 9, QFont.Bold))
            headItem.setForeground(QBrush(QColor(137,199,161)))
            headItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        self.table.setColumnWidth(0,40)
        self.table.setColumnWidth(1,80)
        self.table.setColumnWidth(2,90)
        self.table.setColumnWidth(3,230)
        self.table.setColumnWidth(4,50)
        self.table.setColumnWidth(5,85)
        self.table.setRowHeight(0,30)
        self.table.setRowHeight(1,30)
        self.table.setRowHeight(2,30)
        self.table.setRowHeight(3,30)
        self.table.setRowHeight(4,30)
        self.table.setRowHeight(5,30)
        self.table.setRowHeight(6,30)
        self.table.setRowHeight(7,30)
        self.table.setRowHeight(8,30)
        self.table.setRowHeight(9,30)
        for i in range(row):
            if i%2==0:
                for j in range(vol):
                    temp_data=Data[i][j]  #临时记录，不能直接插入表格
                    data=QTableWidgetItem(str(temp_data)) #转换后可插入表格
                    data.setBackground(QBrush(QColor(245, 245, 244)))
                    self.table.setItem(i,j,data)
            else:
                for j in range(vol):
                    temp_data=Data[i][j]  #临时记录，不能直接插入表格
                    data=QTableWidgetItem(str(temp_data)) #转换后可插入表格
                    data.setBackground(QBrush(QColor(254, 254, 254)))
                    self.table.setItem(i,j,data)
    def getRecord(self):
        self.remindLabel.setVisible(False)
        self.recommendLabel.setVisible(False)
        self.newrecord.setVisible(False)
        self.table.setVisible(True)
        self.aboutcontent.setVisible(False)
        print('heregetrecord')
        f=open(r'database/username.txt')
        username=f.read()
        f.close()
        self.connection = sqlite3.connect("database/oj.db")
        Data=self.connection.execute("SELECT id,proname,runmodel,time FROM userhistory WHERE username = '%s'" %username)
        self.connection.commit()
        Data=Data.fetchall()
        if Data!=[]:
            row=len(Data)  #取得记录个数，用于设置表格的行数
            vol=len(Data[0])  #取得字段数，用于设置表格的列数
            print(row)
            print(vol)
            self.table.setRowCount(row)
            self.table.setColumnCount(vol)
            self.table.setHorizontalHeaderLabels(['编号','题目名字','测评结果','提交时间'])
            self.table.verticalHeader().setVisible(False)
    #        self.table.horizontalHeader().setVisible(False)
            self.table.horizontalHeader().setFixedHeight(25)
            for index in range(self.table.columnCount()):
                headItem = self.table.horizontalHeaderItem(index)
                headItem.setFont(QFont("song", 9, QFont.Bold))
                headItem.setForeground(QBrush(QColor(137,199,161)))
                headItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) 
            self.table.setColumnWidth(0,55)
            self.table.setColumnWidth(1,175)
            self.table.setColumnWidth(2,185)
            self.table.setColumnWidth(3,160)
            self.table.setRowHeight(0,30)
            self.table.setRowHeight(1,30)
            self.table.setRowHeight(2,30)
            self.table.setRowHeight(3,30)
            self.table.setRowHeight(4,30)
            self.table.setRowHeight(5,30)
            self.table.setRowHeight(6,30)
            self.table.setRowHeight(7,30)
            self.table.setRowHeight(8,30)
            self.table.setRowHeight(9,30)
            for i in range(row):
                if i%2==0:
                    for j in range(vol):
                        temp_data=Data[i][j]  #临时记录，不能直接插入表格
                        data=QTableWidgetItem(str(temp_data)) #转换后可插入表格
                        data.setBackground(QBrush(QColor(245, 245, 244)))
                        self.table.setItem(i,j,data)
                else:
                    for j in range(vol):
                        temp_data=Data[i][j]  #临时记录，不能直接插入表格
                        data=QTableWidgetItem(str(temp_data)) #转换后可插入表格
                        data.setBackground(QBrush(QColor(254, 254, 254)))
                        self.table.setItem(i,j,data)
        else:
            self.recommendLabel.setVisible(False)
            self.newrecord.setVisible(False)
            self.table.setVisible(False)
            self.remindLabel.setVisible(True)
    def getUser(self):
        self.remindLabel.setVisible(False)
        self.recommendLabel.setVisible(False)
        self.newrecord.setVisible(False)
        self.table.setVisible(True)
        self.aboutcontent.setVisible(False)
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog4()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


