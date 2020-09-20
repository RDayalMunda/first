# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_open.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_ui_open(object):
    def __init__(self):
        self.teamlist = []
        
        #
        
    def setupUi(self, ui_open):
        ui_open.setObjectName("ui_open")
        ui_open.resize(360, 150)
        ui_open.setMinimumSize(QtCore.QSize(360, 150))
        ui_open.setMaximumSize(QtCore.QSize(500, 200))
        ui_open.setWindowIcon(QtGui.QIcon('icons/open.png'))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        ui_open.setFont(font)
        self.formLayout = QtWidgets.QFormLayout(ui_open)
        self.formLayout.setObjectName("formLayout")
        self.o_label = QtWidgets.QLabel(ui_open)
        self.o_label.setAlignment(QtCore.Qt.AlignCenter)
        self.o_label.setObjectName("o_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.o_label)

        #combo box for selecting team
        #changes cb name to cb_select from o_cb_select
        self.cb_select = QtWidgets.QComboBox(ui_open)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_select.setFont(font)
        self.cb_select.setObjectName("cb_select")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cb_select)
        #load button
        self.b_load = QtWidgets.QPushButton(ui_open)
        self.b_load.setObjectName("b_load")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.b_load)
        
        
        
        self.retranslateUi(ui_open)
        QtCore.QMetaObject.connectSlotsByName(ui_open)

        #adding elements in combo box
        #self.getcbitems()
        #self.cb_select.addItems(self.teamlist)

    def retranslateUi(self, ui_open):
        _translate = QtCore.QCoreApplication.translate
        ui_open.setWindowTitle(_translate("ui_open", "Load Team"))
        self.o_label.setText(_translate("ui_open", "Choose Team"))
        self.b_load.setText(_translate("ui_open", "Load"))


if __name__ == "__main__":
    import sys
    ##global variables
    ##sqlloadigs
    
    app = QtWidgets.QApplication(sys.argv)
    ui_open = QtWidgets.QWidget()
    ui = Ui_ui_open()
    ui.setupUi(ui_open)
    ui_open.show()
    sys.exit(app.exec_())
