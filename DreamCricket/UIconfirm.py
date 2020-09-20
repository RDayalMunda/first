# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_confirm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Confirm(object):
    def setupUi(self, Confirm):
        Confirm.setObjectName("Confirm")
        Confirm.resize(300, 150)
        Confirm.setMaximumSize(QtCore.QSize(393, 261))
        Confirm.setWindowIcon(QtGui.QIcon('icons/bat.png'))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        Confirm.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Confirm)
        self.gridLayout.setObjectName("gridLayout")
        self.label_overwrite = QtWidgets.QLabel(Confirm)
        self.label_overwrite.setAlignment(QtCore.Qt.AlignCenter)
        self.label_overwrite.setObjectName("label_overwrite")
        self.gridLayout.addWidget(self.label_overwrite, 0, 0, 1, 2)

        #return button
        self.b_return = QtWidgets.QPushButton(Confirm)
        self.b_return.setObjectName("b_return")
        self.gridLayout.addWidget(self.b_return, 4, 1, 1, 1)

        #team name
        self.label_teamname = QtWidgets.QLabel(Confirm)
        self.label_teamname.setMaximumSize(QtCore.QSize(380, 68))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_teamname.setFont(font)
        self.label_teamname.setAlignment(QtCore.Qt.AlignCenter)
        self.label_teamname.setObjectName("label_teamname")
        self.gridLayout.addWidget(self.label_teamname, 2, 0, 1, 2)

        #overrite button
        self.b_overwrite = QtWidgets.QPushButton(Confirm)
        self.b_overwrite.setObjectName("b_overwrite")
        self.gridLayout.addWidget(self.b_overwrite, 4, 0, 1, 1)
        
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)

        self.retranslateUi(Confirm)
        QtCore.QMetaObject.connectSlotsByName(Confirm)

    def retranslateUi(self, Confirm):
        _translate = QtCore.QCoreApplication.translate
        Confirm.setWindowTitle(_translate("Confirm", "Form"))
        self.label_overwrite.setText(_translate("Confirm", "Do you want to Overwrite this team"))
        self.b_return.setText(_translate("Confirm", "Return"))
        self.label_teamname.setText(_translate("Confirm", "#teamname"))
        self.b_overwrite.setText(_translate("Confirm", "Overwrite"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Confirm = QtWidgets.QWidget()
    ui = Ui_Confirm()
    ui.setupUi(Confirm)
    Confirm.show()
    sys.exit(app.exec_())
