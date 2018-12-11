from PyQt5 import QtCore, QtGui, QtWidgets
from database import Db
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QCoreApplication
from relogin import Ui_Dialog5

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(428, 333)
        Dialog.setStyleSheet("QDialog{background-image:url(images/signup.PNG);\n"
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
"font:bold 11pt;\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"color: rgb(82,86,80);"
"font-family:Arial,Microsoft YaHei,黑体,宋体,sans-serif;"
"font:  9pt;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"background: rgb(82,86,80);\n"
"color: white;\n"
"border-bottom: 2px solid rgb(210,210,210);\n"
"border-radius: 4px;\n"
"}\n"
"")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(85, 190, 151, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 220, 151, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 250, 171, 31))
        self.label_3.setObjectName("label_3")
        self.btnclose = QtWidgets.QPushButton(Dialog)
        self.btnclose.setGeometry(QtCore.QRect(395, 5, 35, 20))
        self.btnclose.setObjectName("btnclose")
        self.btnclose.clicked.connect(QCoreApplication.instance().quit)
        self.btnclose.setStyleSheet("background-color: rgba(255,255,255,0);\n"
"color:rgb(43,47,52);\n"
"border-color:rgba(255,255,255,0);\n"
"font:  bold 10pt;\n"
"")
        self.txtUsername = QtWidgets.QLineEdit(Dialog)
        self.txtUsername.setGeometry(QtCore.QRect(130, 190, 221, 25))
        self.txtUsername.setObjectName("txtUsername")
        self.txtPassword = QtWidgets.QLineEdit(Dialog)
        ################## make the password invisible ############
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        ###########################################################
        self.txtPassword.setGeometry(QtCore.QRect(130, 220, 221, 25))
        self.txtPassword.setObjectName("txtPassword")
        self.txtPassword2 = QtWidgets.QLineEdit(Dialog)
        ################## make the password2 invisible ############
        self.txtPassword2.setEchoMode(QtWidgets.QLineEdit.Password)
        ###########################################################
        self.txtPassword2.setGeometry(QtCore.QRect(130, 250, 221, 25))
        self.txtPassword2.setObjectName("txtPassword2")
        self.btnRegister = QtWidgets.QPushButton(Dialog)
        self.btnRegister.setGeometry(QtCore.QRect(190, 290, 100, 25))
        self.btnRegister.setObjectName("btnRegister")
        ################## register button#########################
        self.btnRegister.clicked.connect(self.registerButton)
        ###########################################################
        self.label_Heading = QtWidgets.QLabel(Dialog)
        self.label_Heading.setGeometry(QtCore.QRect(180, 130, 431, 61))
        self.label_Heading.setObjectName("label_Heading")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def registerButton(self):
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        password2 = self.txtPassword2.text()
        if self.checkFields(username,password):
            self.showMessage("Error", "小主，所有信息都要填写哦|д･)っ")
        else:
            if(self.checkPassword(password,password2)):
                insertDb = Db()
                Db().insertTable(username,password)
                self.showMessage("Success","注册成功啦!(⁄⁄•⁄ω⁄•⁄⁄)")
                self.clearField()
#                self.Dialog.setVisible(False)
                self.homWindow = QtWidgets.QDialog()
                self.ui = Ui_Dialog5()
                self.ui.setupUi(self.homWindow)
                self.homWindow.show()
            else:
                self.showMessage("Error","前后密码不匹配哦⊙̆̈_⊙̆̈")
       
    def showMessage(self,title,msg):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        #msgBox.setTitle(title)
        msgBox.setText(msg)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        self.btnclose.setText(_translate("Dialog", "X"))
        Dialog.setWindowTitle(_translate("Dialog", "在下AI酱•ω•"))
        self.label.setText(_translate("Dialog", "用户名:"))
        self.label_2.setText(_translate("Dialog", "输入密码:"))
        self.label_3.setText(_translate("Dialog", "确认密码:"))
        self.btnRegister.setText(_translate("Dialog", "我要注册"))
        self.label_Heading.setText(_translate("Dialog", "欢迎加入AI酱•ω•"))

#    def loginPage(self):
#        self.loginWindow = QtWidgets.QDialog()
#        self.ui = Ui_Dialog2()
#        self.ui.setupUi(self.loginWindow)
#        self.loginWindow.show()
        
    def checkFields(self,username,password):
        if(username=="" or password== ""):
            return True
    ############## check if password1 and password2 matches #############
    def checkPassword(self,password1, password2):
        return password1 == password2

    ##################### clear fields ##################
    def clearField(self):
        self.txtUsername.setText(None)
        self.txtPassword.setText(None)
        self.txtPassword2.setText(None)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

