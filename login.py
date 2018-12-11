from PyQt5 import QtCore, QtGui, QtWidgets
from database import Db
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QCoreApplication
from signup import Ui_Dialog
from mainwindow import Ui_Dialog4


class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(428, 333)
        Dialog.setStyleSheet("QDialog{background-image:url(images/login.PNG);\n"
"}\n"
"\n"
"QLineEdit{\n"
"border-radius: 3px;\n"
"border: 2px solid rgb(210,210,210);\n"
"border-radius: 4px;\n"
"\n"
"}\n"
"\n"
"QLabel#label_Heading{\n"
"color: white;"
"font-family:Arial,Microsoft YaHei,黑体,宋体,sans-serif;"
"font: 75 10pt;\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"color: white;"
"font-family:Arial,Microsoft YaHei,黑体,宋体,sans-serif;"
"font:  bold 11pt;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"background: rgb(82,86,80);\n"
"color: white;\n"
"font:  bold 11pt \"微软雅黑\";\n"
"border-bottom: 2px solid rgb(210,210,210);\n"
"border-radius: 4px;\n"
"}\n"
"")
#        self.label = QtWidgets.QLabel(Dialog)
#        self.label.setGeometry(QtCore.QRect(125, 150, 51, 21))
#        self.label.setObjectName("label")
#        self.label_2 = QtWidgets.QLabel(Dialog)
#        self.label_2.setGeometry(QtCore.QRect(140, 185, 51, 21))
#        self.label_2.setObjectName("label_2")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setEnabled(False)
        self.graphicsView.setMinimumSize(QtCore.QSize(100, 100))
        self.graphicsView.setMaximumSize(QtCore.QSize(100, 100))
        self.graphicsView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.graphicsView.setAutoFillBackground(True)
        self.graphicsView.setStyleSheet("background-image: url(images/bear.png);\n"
"border-radius:50px;\n"
"background-color:rgba(255,255,255,0);"
"")
        self.graphicsView.setGeometry(QtCore.QRect(168, 50, 100, 100))
        self.txtUsername = QtWidgets.QLineEdit(Dialog)
        self.txtUsername.setGeometry(QtCore.QRect(115, 200, 200, 30))
        self.txtUsername.setObjectName("txtUsername")
        self.txtPassword = QtWidgets.QLineEdit(Dialog)
        ################## make the password invisible ############
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        ###########################################################
        self.txtPassword.setGeometry(QtCore.QRect(115, 235, 200, 30))
        self.txtPassword.setObjectName("txtPassword")
        self.btnclose = QtWidgets.QPushButton(Dialog)
        self.btnclose.setGeometry(QtCore.QRect(395, 5, 35, 20))
        self.btnclose.setObjectName("btnclose")
        self.btnclose.clicked.connect(QCoreApplication.instance().quit)
        self.btnclose.setStyleSheet("background-color: rgba(255,255,255,0);\n"
"color:black;\n"
"border-color:rgba(255,255,255,0);\n"
"font:  normal 9pt;\n"
"")
        self.btnLogin = QtWidgets.QPushButton(Dialog)
        self.btnLogin.setGeometry(QtCore.QRect(115, 280, 85, 30))
        self.btnLogin.setObjectName("btnLogin")
        #################### Login Button funtion #######################
        self.btnLogin.clicked.connect(self.loginCheck)
        #################################################################
        self.btnSignup = QtWidgets.QPushButton(Dialog)
        self.btnSignup.setGeometry(QtCore.QRect(225, 280, 85, 30))
        self.btnSignup.setObjectName("btnSignup")
        #################### SignUp Button #############################
        self.btnSignup.clicked.connect(self.signupButton)
        ################################################################
#        self.label_Heading = QtWidgets.QLabel(Dialog)
#        self.label_Heading.setGeometry(QtCore.QRect(310, 210, 200, 20))
#        self.label_Heading.setObjectName("label_Heading")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.setWindowTitle(_translate("Dialog", "在下AI酱•ω•"))
        self.btnclose.setText(_translate("Dialog", "X"))
#        self.label.setText(_translate("Dialog", "用户名:"))
#        self.label_2.setText(_translate("Dialog", "密码:"))
        self.btnLogin.setText(_translate("Dialog", "登录"))
        self.btnSignup.setText(_translate("Dialog", "注册"))
#        self.label_Heading.setText(_translate("Dialog", "我们想做最懂你的OJ"))
        
    def welcomePage(self):
        self.homWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog4()
        self.ui.setupUi(self.homWindow)
        self.homWindow.show()
        
    def loginCheck(self):
        username = self.txtUsername.text()
        print(username)
        fh = open('database/username.txt', 'w+')
        fh.write(str(username))
        fh.close()
        password = self.txtPassword.text()
        getDb = Db()        
        result = getDb.loginCheck(username,password)
        if(result):
            self.welcomePage()
            self.clearField()
            print(result)
        else:
            print("密码错误哦,再输一次吧(≖ω≖✿)")
            self.showMessage("Warning","诶,这是不合理的用户名和密码哦~(¯•ω•¯)")
    def getUsername(self):
        return self.txtUsername.text()
            
    def showMessage(self,title,msg):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        #msgBox.setTitle(title)
        msgBox.setText(msg)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    def signupButton(self):   
        self.signDialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.signDialog)
        self.signDialog.show()
    def clearField(self):
        self.txtUsername.setText(None)
        self.txtPassword.setText(None) 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv) 
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

