from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import rules


class Ui_ui_evaluate(object):
    def __init__(self):
        self.teamlist = []
        self.listplayers =[]
        self.listpoints =[]
        self.matchlist = ['match 1', 'match 2', 'match3', 'match 4', 'match 5']
        self.totalpoints = 0
        
    #to settle with the points scored by the team            
    def running(self, teamname):
        self.totalpoints = 0
        #print('running has started')
        self.listplayers = []
        self.listpoints = []
        sel = "SELECT name, players FROM teams WHERE name ='"+teamname+"';"
        cono = sqlite3.connect('gamebase.db')
        curo = cono.cursor()
        curo.execute(sel)
        while True:
            record = curo.fetchone()
            if record == None:
                break
            else:
                self.listplayers.append(record[1])
        for item in self.listplayers:
            pts = rules.tryon(item)
            self.listpoints.append(str(pts))
            self.totalpoints = self.totalpoints + pts
            

        #   self.listpoints is a list of integers which won't be inserted ina a widget
        #   widget will have only string items or list of string not any other data type
        #clear both list
        self.lw_player.clear()
        self.lw_points.clear()
        #add items 
        self.lw_player.addItems(self.listplayers)
        self.lw_points.addItems(self.listpoints)

        
        
    def setupUi(self, ui_evaluate):
        ui_evaluate.setObjectName("ui_evaluate")
        ui_evaluate.resize(500, 550)
        ui_evaluate.setMinimumSize(QtCore.QSize(420, 300))
        ui_evaluate.setMaximumSize(QtCore.QSize(500, 550))
        ui_evaluate.setWindowIcon(QtGui.QIcon('helm.png'))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        ui_evaluate.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(ui_evaluate)
        self.gridLayout.setObjectName("gridLayout")
        self.lw_points = QtWidgets.QListWidget(ui_evaluate)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        
        #points list widget
        self.lw_points.setFont(font)
        self.lw_points.setObjectName("lw_points")
        self.gridLayout.addWidget(self.lw_points, 5, 1, 1, 1)

        #player list widget
        self.lw_player = QtWidgets.QListWidget(ui_evaluate)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.lw_player.setFont(font)
        self.lw_player.setObjectName("lw_player")
        self.gridLayout.addWidget(self.lw_player, 5, 0, 1, 1)

        #team combobox
        self.e_cb_team = QtWidgets.QComboBox(ui_evaluate)
        self.e_cb_team.setObjectName("e_cb_team")
        self.gridLayout.addWidget(self.e_cb_team, 2, 0, 1, 1)
        #self.e_cb_team.addItems(self.teamlist)
        
        self.e_line1 = QtWidgets.QFrame(ui_evaluate)
        self.e_line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.e_line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.e_line1.setObjectName("e_line1")
        self.gridLayout.addWidget(self.e_line1, 1, 0, 1, 2)
        self.e_label = QtWidgets.QLabel(ui_evaluate)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.e_label.setFont(font)
        self.e_label.setAlignment(QtCore.Qt.AlignCenter)
        self.e_label.setObjectName("e_label")
        self.gridLayout.addWidget(self.e_label, 0, 0, 1, 2)

        #match combo box
        self.e_cb_match = QtWidgets.QComboBox(ui_evaluate)
        self.e_cb_match.setObjectName("e_cb_match")
        self.gridLayout.addWidget(self.e_cb_match, 2, 1, 1, 1)
        self.e_cb_match.addItems(self.matchlist)
        
        self.e_line2 = QtWidgets.QFrame(ui_evaluate)
        self.e_line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.e_line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.e_line2.setObjectName("e_line2")
        self.gridLayout.addWidget(self.e_line2, 3, 0, 1, 2)

        #evaluate button
        self.e_b_evaluate = QtWidgets.QPushButton(ui_evaluate)
        self.e_b_evaluate.setMinimumSize(QtCore.QSize(120, 30))
        self.e_b_evaluate.setObjectName("e_b_evaluate")
        self.gridLayout.addWidget(self.e_b_evaluate, 6, 0, 1, 2)
        self.e_b_evaluate.clicked.connect(self.results)
        
        self.e_label_players = QtWidgets.QLabel(ui_evaluate)
        self.e_label_players.setObjectName("e_label_players")
        self.gridLayout.addWidget(self.e_label_players, 4, 0, 1, 1)
        self.e_label_points = QtWidgets.QLabel(ui_evaluate)
        self.e_label_points.setObjectName("e_label_points")
        self.gridLayout.addWidget(self.e_label_points, 4, 1, 1, 1)

        self.retranslateUi(ui_evaluate)
        QtCore.QMetaObject.connectSlotsByName(ui_evaluate)

    def retranslateUi(self, ui_evaluate):
        _translate = QtCore.QCoreApplication.translate
        ui_evaluate.setWindowTitle(_translate("ui_evaluate", "Evaluate Team"))
        self.e_label.setText(_translate("ui_evaluate", "Evaluate the performance of your Fantasy Team"))
        self.e_b_evaluate.setText(_translate("ui_evaluate", "Evaluate"))
        self.e_label_players.setText(_translate("ui_evaluate", "Players"))
        self.e_label_points.setText(_translate("ui_evaluate", "Points"))

    #result of EVALUATE
    def results(self):
        print('Happy')
        msg=QMessageBox()
        msg.setWindowTitle('RESULT')
        msg.setText(' %s\n\t\t\t\nScore = %d' %(self.e_cb_team.currentText(),self.totalpoints))
        msg.setWindowIcon(QtGui.QIcon('helm.png'))
        msg.exec_()


        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui_evaluate = QtWidgets.QWidget()
    ui = Ui_ui_evaluate()
    ui.setupUi(ui_evaluate)
    ui_evaluate.show()
    sys.exit(app.exec_())
