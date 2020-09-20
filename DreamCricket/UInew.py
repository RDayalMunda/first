# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3


class Ui_ui_new(object):
    def setupUi(self, ui_new):
        ui_new.setObjectName("ui_new")
        ui_new.setEnabled(True)
        ui_new.resize(360, 150)
        ui_new.setMinimumSize(QtCore.QSize(360, 150))
        ui_new.setMaximumSize(QtCore.QSize(500, 200))
        ui_new.setWindowIcon(QtGui.QIcon('icons/star.png'))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        ui_new.setFont(font)
        self.formLayout = QtWidgets.QFormLayout(ui_new)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.formLayout.setObjectName("formLayout")

        #label Or title.
        self.n_label = QtWidgets.QLabel(ui_new)
        self.n_label.setMinimumSize(QtCore.QSize(0, 30))
        self.n_label.setAlignment(QtCore.Qt.AlignCenter)
        self.n_label.setObjectName("n_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.n_label)

        #team name input area
        self.n_l_teamname = QtWidgets.QLineEdit(ui_new)
        self.n_l_teamname.setMinimumSize(QtCore.QSize(0, 30))
        self.n_l_teamname.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.n_l_teamname.setFont(font)
        self.n_l_teamname.setAlignment(QtCore.Qt.AlignCenter)
        self.n_l_teamname.setObjectName("n_l_teamname")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.n_l_teamname)

        #create button
        self.b_create = QtWidgets.QPushButton(ui_new)
        self.b_create.setEnabled(True)
        self.b_create.setMinimumSize(QtCore.QSize(0, 0))
        self.b_create.setMaximumSize(QtCore.QSize(500, 555))
        self.b_create.setObjectName("b_create")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.b_create)

        self.retranslateUi(ui_new)
        QtCore.QMetaObject.connectSlotsByName(ui_new)

    def retranslateUi(self, ui_new):
        _translate = QtCore.QCoreApplication.translate
        ui_new.setWindowTitle(_translate("ui_new", "Create Team"))
        self.n_label.setText(_translate("ui_new", "Enter a New Team Name"))
        self.n_l_teamname.setPlaceholderText(_translate("ui_new", "team name"))
        self.b_create.setText(_translate("ui_new", "Create"))


iteam = 'wow'
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui_new = QtWidgets.QWidget()
    ui = Ui_ui_new()
    ui.setupUi(ui_new)
    ui_new.show()
    sys.exit(app.exec_())
