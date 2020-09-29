# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3


class Ui_Library(object):
    def setupUi(self, Library):
        Library.setObjectName("Library")
        Library.resize(515, 260)
        font = QtGui.QFont()
        font.setPointSize(8)
        #testing out functions
        #font.setItalic(False)
        #font.setUnderline(False)
        #font.setStrikeOut(False)
        #font.setKerning(True)
        Library.setFont(font)
        Library.setAutoFillBackground(False)
        self.gridLayout = QtWidgets.QGridLayout(Library)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 6, 1, 1)
        self.label_price = QtWidgets.QLabel(Library)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(16)
        self.label_price.setFont(font)
        self.label_price.setObjectName("label_price")
        self.gridLayout.addWidget(self.label_price, 3, 1, 1, 2, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.label_total = QtWidgets.QLabel(Library)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(16)
        self.label_total.setFont(font)
        self.label_total.setObjectName("label_total")
        self.gridLayout.addWidget(self.label_total, 6, 1, 1, 2, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 7, 3, 1, 1)
        self.label_title = QtWidgets.QLabel(Library)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(16)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.gridLayout.addWidget(self.label_title, 1, 1, 1, 2, QtCore.Qt.AlignRight)
        self.b_price = QtWidgets.QPushButton(Library)
        self.b_price.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(16)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.b_price.setFont(font)
        self.b_price.setObjectName("b_price")
        self.gridLayout.addWidget(self.b_price, 1, 5, 1, 1, QtCore.Qt.AlignLeft)
        spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.label_quantity = QtWidgets.QLabel(Library)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(16)
        self.label_quantity.setFont(font)
        self.label_quantity.setObjectName("label_quantity")
        self.gridLayout.addWidget(self.label_quantity, 5, 1, 1, 2, QtCore.Qt.AlignRight)
        self.label_total_return = QtWidgets.QLabel(Library)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(16)
        self.label_total_return.setFont(font)
        self.label_total_return.setObjectName("label_total_return")
        self.gridLayout.addWidget(self.label_total_return, 6, 3, 1, 2, QtCore.Qt.AlignTop)
        self.line_quantity = QtWidgets.QLineEdit(Library)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.line_quantity.setFont(font)
        self.line_quantity.setMaxLength(4)
        self.line_quantity.setObjectName("line_quantity")
        self.gridLayout.addWidget(self.line_quantity, 5, 3, 1, 2)
        self.line_title = QtWidgets.QLineEdit(Library)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.line_title.setFont(font)
        self.line_title.setObjectName("line_title")
        self.gridLayout.addWidget(self.line_title, 1, 3, 1, 2)
        self.label_price_return = QtWidgets.QLabel(Library)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(16)
        self.label_price_return.setFont(font)
        self.label_price_return.setObjectName("label_price_return")
        self.gridLayout.addWidget(self.label_price_return, 3, 3, 1, 2, QtCore.Qt.AlignTop)
        self.b_total = QtWidgets.QPushButton(Library)
        self.b_total.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(16)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.b_total.setFont(font)
        self.b_total.setObjectName("b_total")
        self.gridLayout.addWidget(self.b_total, 5, 5, 1, 1, QtCore.Qt.AlignLeft)
        spacerItem3 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 0, 3, 1, 1)
        self.line = QtWidgets.QFrame(Library)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 2, 1, 4)

        self.retranslateUi(Library)
        QtCore.QMetaObject.connectSlotsByName(Library)

        #to make the 'Find Price' button to get the title name and check with the database
        self.b_price.clicked.connect(self.chk_price)

        #to make the 'Find Total' button to get the total
        self.b_total.clicked.connect(self.chk_total)


    def retranslateUi(self, Library):
        _translate = QtCore.QCoreApplication.translate
        Library.setWindowTitle(_translate("Library", "Book Shop"))
        self.label_price.setText(_translate("Library", "Price:"))
        self.label_total.setText(_translate("Library", "Total:"))
        self.label_title.setText(_translate("Library", "Book Title:"))
        self.b_price.setText(_translate("Library", "Find Price"))
        self.label_quantity.setText(_translate("Library", "Quantity:"))
        self.label_total_return.setText(_translate("Library", "₹ 0.00"))
        self.line_quantity.setInputMask(_translate("Library", "0999"))
        self.line_quantity.setText(_translate("Library", "1"))
        self.line_title.setText(_translate("Library", "text"))
        self.label_price_return.setText(_translate("Library", "₹ 0.00"))
        self.b_total.setText(_translate("Library", "Find Total"))

    #taking Title from the line_title LINEWIDGET when 'Find_price' is clicked
    def chk_price(self):
        global g_price
        global g_total
        txt = self.line_title.text()
        txt = txt.lower()
        sel = "SELECT * FROM books where lower(title) = '"+txt+"';"
        price = "₹ 0.00"
        #no to check if 'txt' has the title required
        #first setting up the sqlite3 db
        Library=sqlite3.connect('Library.db')   #'library' connection object is created
        curbook=Library.cursor()                #'curbook' cursor object is created

        curbook.execute(sel)
        record = curbook.fetchone()
        #conditions
        if record == None:
            print("No books with that name available yet!")
            self.label_price_return.setText("₹ 0.00")
            self.label_total_return.setText("₹ 0.00")
            g_total = 0
            g_price = 0

            #this is the message box/ popup mesg that will pop when a book is not found in the database
            #this is defining the message box
            msg=QMessageBox()
            msg.setWindowTitle('Book not Found')
            msg.setText("The book you are trying to find is not available yet!\nTry again after the next stock arrives.")
            msg.exec_()                 #this executes the messagebox
            
        else:
            g_price = record[3]
            price = "₹ {:.2f}".format(g_price)
            print('price = ', price)
            #to set the label to the 'price' provided in the database
            self.label_price_return.setText(price)

        Library.close()

    def chk_total(self):
        global g_price
        global g_total
        copies = self.line_quantity.text()
        copies = int(copies)
        g_total = g_price * copies
        total = "₹ {:.2f}".format(g_total)
        self.label_total_return.setText(total)

        
if __name__ == "__main__":
    import sys
    g_price = 0
    g_total = 0
    app = QtWidgets.QApplication(sys.argv)
    Library = QtWidgets.QWidget()
    ui = Ui_Library()
    ui.setupUi(Library)
    Library.show()
    sys.exit(app.exec_())
