# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'del.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(216, 98)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 60, 71, 21))
        self.pushButton_3.setStyleSheet("\n"
"QPushButton \n"
"{\n"
"    background:#868eff;\n"
"    border-radius:60px;\n"
"}\n"
"QToolButton \n"
"{\n"
"    background:#868eff;\n"
"    border-radius:50px;\n"
"}\n"
"\n"
"QPushButton \n"
"{\n"
"    color:white;\n"
"    border-radius:15px;\n"
"}\n"
"QPushButton:hover \n"
"{\n"
"    color:#333;\n"
"    border-radius:15px;\n"
"    background:#49ebff;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 60, 81, 21))
        self.pushButton_4.setStyleSheet("\n"
"QPushButton \n"
"{\n"
"    background:#868eff;\n"
"    border-radius:60px;\n"
"}\n"
"QToolButton \n"
"{\n"
"    background:#868eff;\n"
"    border-radius:50px;\n"
"}\n"
"\n"
"QPushButton \n"
"{\n"
"    color:white;\n"
"    border-radius:15px;\n"
"}\n"
"QPushButton:hover \n"
"{\n"
"    color:#333;\n"
"    border-radius:15px;\n"
"    background:#49ebff;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 10, 47, 13))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_3.setText(_translate("Form", "Ok"))
        self.pushButton_4.setText(_translate("Form", "Cancel"))
        self.label.setText(_translate("Form", "Удалить:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
