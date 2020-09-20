from PyQt5 import QtCore, QtGui, QtWidgets

#importing  message box / popup menu
from PyQt5.QtWidgets import QMessageBox


#there are other UI's created
from UInew import Ui_ui_new as New
#print('new loaded')
from UIopen import Ui_ui_open as Open
#print('open loaded')
from UIevaluate import Ui_ui_evaluate as Eva
#print('evaluate loaded')
import rules
#SQLite3 is joined here
import sqlite3
#Confirmation box
from UIconfirm import Ui_Confirm as Con


class Ui_MainWindow(object):

    def __init__(self):
        self.team_name = None
    
        #define New TEAM ui
        self.newui = QtWidgets.QWidget()
        self.nui = New()
        self.nui.setupUi(self.newui)
        self.newui.setWindowModality(QtCore.Qt.ApplicationModal) #blocking
        self.nui.b_create.clicked.connect(self.newteam)    #clicked
        self.nui.n_l_teamname.returnPressed.connect(self.nui.b_create.click)
        
        
        #define Load Or Open A team UI
        self.openui = QtWidgets.QWidget()
        self.oui = Open()
        self.oui.setupUi(self.openui)
        self.openui.setWindowModality(QtCore.Qt.ApplicationModal)    #blocking

        #define evaluation UI
        self.evaui = QtWidgets.QWidget()
        self.eui = Eva()
        self.eui.setupUi(self.evaui)
        self.evaui.setWindowModality(QtCore.Qt.ApplicationModal) # blocking

        #define confirmation UI
        self.conui = QtWidgets.QWidget()
        self.cui = Con()
        self.cui.setupUi(self.conui)
        self.conui.setWindowModality(QtCore.Qt.ApplicationModal) # to block previous window

    

    #method NEW
    def NewUI(self):
        self.newui.show()                                #display new window

    #method LOAD    
    def OpenUI(self):
        self.openui.show()                  #display open window
        self.getteamlist()
        self.oui.b_load.clicked.connect(self.loadteam)
        return
        
    #method EVALUATE   
    def EvaUI(self):
        self.evaui.show()                   #display evaluate window
        self.evaluateteam()
        print(teamlist)
        self.getteamlist()
        self.eui.e_cb_team.currentTextChanged.connect(self.evaluateteam)
        
        return

    #method CONFIRM
    def ConUI(self):
        self.conui.show()
        self.cui.b_return.clicked.connect(self.closeconui)#return Close
        self.cui.b_overwrite.clicked.connect(self.deleter)  #overrite
        self.cui.label_teamname.setText(teamname)
        print('4')
        
    def closeconui(self):
        print('6')
        self.conui.close()

    #error not savesd message box
    def msgbox(self):
        msg=QMessageBox()
        msg.setWindowTitle('Not Saved')
        msg.setText("The Team could not be saved.\nFollowing might be the issue.\n\t1. Check the number of players you selected is 11.\n\t2. Check if you have only 1 wicket-keeper.\n\t3. Check if you have used more points than 1000.")
        msg.setWindowIcon(QtGui.QIcon('icons/icon.png'))
        msg.exec_()
        
    
    #method SAveClicked
    def SaveUI(self):
        if len(listselected) != 11 or nwk != 1 or ptsrem < 0:
            self.msgbox()
        else:
            cono = sqlite3.connect('gamebase.db')
            curo = cono.cursor()
            cono.commit()
            curo.execute("SELECT name FROM teams WHERE name = '"+teamname+"';")
            #print('bugtest1')
            record = curo.fetchall()
            if len(record) == 0:    #if there are no record
                curo.close()
                cono.close()
                #print('2')
                self.savedata()
                return
            else:                   #if there are data present
                print('3')          
                curo.close()
                cono.close()
                self.ConUI()


        ##learned that cursor oject shhould be closed first then the connection object
    
    #savedata in the database        
    def savedata(self):
        global listselected, listpoints
        #print('8')
        listpoints.clear()
        #print('now for saving')
        for i in listselected:
            listpoints.append(rules.tryon(i))
        for i in range(11):
            self.inserter(i)
        #print('all inserted')
        return
    ##inserter
    def inserter(self, i):
        #print('10')
        cono = sqlite3.connect('gamebase.db')
        curo = cono.cursor()
        curo.execute("INSERT INTO teams (name, players, value) VALUES(?,?,?);",(teamname, listselected[i], listpoints[i]))
        cono.commit()
        curo.close()
        cono.close()
        
    ##deleter
    def deleter(self):
        #print('5')
        cono = sqlite3.connect('gamebase.db')
        curo = cono.cursor()
        curo.execute("DELETE FROM teams WHERE name = '"+teamname+"';")
        cono.commit()
        self.conui.close()
        curo.close()
        cono.close()
        #print('7')
        self.savedata()
        return

    
    
    ##the evaluateteam method
    def evaluateteam(self):
        #self.eui.getcbitems()
        self.eui.running(self.eui.e_cb_team.currentText())
        #print('ok')
               
    
    ##loading the team method
    def loadteam(self):
        global teamlist, teamname, listbat, listbwl, listwk, listar, listselected
        global nbat, nbwl, nwk, nar, ptsused, ptsrem
        
        self.clearall()                     #clear values and enable radio
        teamname = self.oui.cb_select.currentText() #get name of selected team
        self.g_team.setText(teamname)
        #to fetch data from database and set it accordingly
        cono = sqlite3.connect('gamebase.db')
        curo = cono.cursor()
        sel = "SELECT name, players FROM teams WHERE name='"+teamname+"';"
        curo.execute(sel)
        
        #list of players in the team has been set
        while True:
            record = curo.fetchone()
            if record == None:
                break
            listselected.append(record[1])
            
        #add player in the listwidget nuber2 and deleting duplicate records
        for item in listselected:
            sel = "SELECT player, value, ctg FROM stats WHERE player='"+item+"';"
            curo.execute(sel)
            record = curo.fetchone()
            ptsused = ptsused + record[1]       #to increase the pts used by the team
            ptsrem = ptsrem - record[1]
            if record == None:
                break
            elif record[2].upper() == 'BAT':
                nbat = nbat + 1
                listbat.remove(record[0])
            elif record[2].upper() == 'BWL':
                nbwl = nbwl + 1
                listbwl.remove(record[0])
            elif record[2].upper() == 'WK':
                nwk = nwk + 1
                listwk.remove(record[0])
            elif record[2].upper() == 'AR':
                nar = nar + 1
                listar.remove(record[0])
            
        #calling function to display points and numbers  ' dis_num_pts '
        self.dis_num_pts()
        
        
                        #REPEATED CODE tranfered to a method
        
        #displaying the points used and remaining
        #self.n_pts_rem.setText(str(ptsrem))
        #self.n_pts_used.setText(str(ptsused))

        # displayinng how many players have been selected
        #self.n_bat.setText(str(nbat))
        #self.n_bwl.setText(str(nbwl))
        #self.n_wk.setText(str(nwk))
        #self.n_ar.setText(str(nar))

        #to diplay the items in list2 when LOAD button is pressed
        self.list2.addItems(listselected)
        self.rb_bat.isChecked()
        #self.list1.addItems(listbat)

        self.openui.close()              #close window after seleection
        return
        
    #how new ceate button deals with the sql and gui
    def newteam(self):
        global teamlist, teamname
        if self.nui.n_l_teamname.text() == '':        #for blank entry
            print('Enter a team name buddy!')
            msg=QMessageBox()               ##already  name exit dialog box
            msg.setWindowTitle('Error')
            msg.setText("Please Enter a Name.")
            msg.setWindowIcon(QtGui.QIcon('icons/icon.png'))
            msg.exec_()
            return
        else:
            teamlist = []
            cono = sqlite3.connect('gamebase.db')   
            curo = cono.cursor()
            sel = 'SELECT name FROM teams;'
            curo.execute(sel)
           #getting teamlist and cthe create button task
            while True:
                record = curo.fetchone()
                if record == None:
                   break
                record = list(record)[0]
                if record not in teamlist:
                    teamlist.append(record)
            #print(teamlist)
            if self.nui.n_l_teamname.text() in teamlist:
                print('Sorry\nThat Team name Already Exist!')
                msg=QMessageBox()               ##already  name exit dialog box
                msg.setWindowTitle('Error')
                msg.setText("That Name is already present.\n\tTry another please.")
                msg.setWindowIcon(QtGui.QIcon('icons/icon.png'))
                msg.exec_()
                return
                
            else:
                self.newui.close()          #closing window after succesfull inpit
                teamname = self.nui.n_l_teamname.text()
                
                self.clearall()                 #clear blocks and getlists
                #print('cleared')
                self.g_team.setText(teamname)   #set name
                #print('name is displayed')    # to clear all widgets and get them enabled           
        return
    
    ##
    #transfer from list1 to list2 DOUBLECLICK
    def transfer12(self, item):
        global listbat, listbwl, listar, listwk, listselected, ptsused, ptsrem
        global nbat, nbwl, nwk, nar
        
        self.list1.takeItem(self.list1.row(item))   #pop
        self.list2.addItem(item.text())             #pushed

        listselected.append(item.text())            #list od selected players got updated
        cono = sqlite3.connect('gamebase.db')
        curo = cono.cursor()
        curo.execute('SELECT player, ctg FROM stats;')
        while True:
            record = curo.fetchone()
            if record == None:
                break
            elif item.text() == record[0]:
                if record[1].upper() == 'BAT':
                    listbat.remove(record[0])
                    nbat = nbat + 1
                elif record[1].upper() == 'BWL':
                    listbwl.remove(record[0])
                    nbwl = nbwl + 1
                elif record[1].upper() == 'WK':
                    listwk.remove(record[0])
                    nwk = nwk + 1
                elif record[1].upper() == 'AR':
                    listar.remove(record[0])
                    nar = nar + 1
        pts=self.func_pts(item.text())          #call function that would change points
        #print(pts)
        ptsrem = ptsrem - pts
        ptsused = ptsused + pts

        #calling display of points and numbers   ' dis_num_pts '
        self.dis_num_pts()
            #       REPEATED codes transfered to a method  #
        #set the display of pts
        #self.n_pts_rem.setText(str(ptsrem))
        #self.n_pts_used.setText(str(ptsused))

        # displayinng how many players have been selected
        #self.n_bat.setText(str(nbat))
        #self.n_bwl.setText(str(nbwl))
        #self.n_wk.setText(str(nwk))
        #self.n_ar.setText(str(nar))

    #display nummber and points
    def dis_num_pts(self):
        #set the display of pts
        self.n_pts_rem.setText(str(ptsrem))
        self.n_pts_used.setText(str(ptsused))

        # displayinng how many players have been selected
        self.n_bat.setText(str(nbat))
        self.n_bwl.setText(str(nbwl))
        self.n_wk.setText(str(nwk))
        self.n_ar.setText(str(nar))

        #displaying red labels
        if nwk > 1:
            self.n_wk.setStyleSheet("color: red;")      #wk number
            self.label_wk.setStyleSheet("color: red;")  #wk label
        else:
            self.n_wk.setStyleSheet("color: black;")      #wk number
            self.label_wk.setStyleSheet("color: black;")  #wk label
        if ptsrem < 0:
            self.pts_rem.setStyleSheet("color: red;")   # -ve points
            self.n_pts_rem.setStyleSheet("color: red;") # -ve pts label
        else:
            self.pts_rem.setStyleSheet("color: black;")   # valid points
            self.n_pts_rem.setStyleSheet("color: black;") # valid pts label
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_wk.setFont(font)
        self.n_wk.setFont(font)
        self.pts_rem.setFont(font)
        self.n_pts_rem.setFont(font)
        return
                    
                
   #function that would change the values of PTS and number of players.
    def func_pts(self, x):
        #print(x)
        name = x
        pts = 0
        cono = sqlite3.connect('gamebase.db')
        curo = cono.cursor()
        sel = "SELECT player, value FROM stats where player ='"+name+"';"
        curo.execute(sel)
        record = curo.fetchone()
        pts = int(record[1])            #got the value of the player
        return pts

    
    #tranfer from list2 to list1 DOUBLECLICK
    def transfer21(self, item):
        global listbat, listbwl, listar, listwk, listselected, ptsrem, ptsused
        global nbat, nbwl, nwk, nar
        
        self.list2.takeItem(self.list2.row(item))   #pop
        self.list1.addItem(item.text())             #pushed

        listselected.remove(item.text())            #list od selected player list removed player
        cono = sqlite3.connect('gamebase.db')
        curo = cono.cursor()
        curo.execute('SELECT player, ctg FROM stats;')
        while True:
            record = curo.fetchone()
            if record == None:
                break
            elif item.text() == record[0]:
                if record[1].upper() == 'BAT':
                    listbat.append(record[0])
                    nbat = nbat-1
                elif record[1].upper() == 'BWL':
                    listbwl.append(record[0])
                    nbwl = nbwl -1
                elif record[1].upper() == 'WK':
                    listwk.append(record[0])
                    nwk = nwk - 1
                elif record[1].upper() == 'AR':
                    listar.append(record[0])
                    nar = nar -1
        pts = self.func_pts(item.text())
        ptsused = ptsused - pts
        ptsrem = ptsrem + pts

        #call function to display points    ' des_num_pts '
        self.dis_num_pts()
        #displaying how many poins has been used
        #self.n_pts_rem.setText(str(ptsrem))
        #self.n_pts_used.setText(str(ptsused))

        # displayinng how many players have been selected
        #self.n_bat.setText(str(nbat))
        #self.n_bwl.setText(str(nbwl))
        #self.n_wk.setText(str(nwk))
        #self.n_ar.setText(str(nar))
        

    ##for getting data RB_button
    def getall(self):
        global listbat, listbwl, listar, listwk, listselected, nbat, nbwl, nwk, nar
        global ptsrem, ptsused
        #clear all items in the list1 and list2
        self.list1.clear()
        self.list2.clear()

        #to items in List2
        self.list2.addItems(listselected)
        
        
        #put values when rb_ are pressed TO LIST1
        if self.rb_bat.isChecked():
            self.list1.addItems(listbat)
        elif self.rb_bwl.isChecked():
            self.list1.addItems(listbwl)
        elif self.rb_ar.isChecked():
            self.list1.addItems(listar)
        elif self.rb_wk.isChecked():
            self.list1.addItems(listwk)

    
    #for cleating the base
    def clearall(self):
        global listbat, listbwl, listar, listwk, listselected, nbat, nbwl, nwk, nar
        global ptsrem, ptsused

        #clear all list
        listbat.clear()
        listbwl.clear()
        listar.clear()
        listwk.clear()
        listselected.clear()
        #clear all numebrs
        nbat = 0
        nbwl = 0
        nwk = 0
        nar = 0

        #clearpoints
        ptsrem = 1000
        ptsused = 0

        #enable save button
        self.mb_save.setDisabled(False)
        
        
        #enable all radio buttons
        self.rb_bat.setEnabled(True)
        self.rb_bwl.setEnabled(True)
        self.rb_wk.setEnabled(True)
        self.rb_ar.setEnabled(True)
        
        #clear all items in the list
        self.list1.clear()
        self.list2.clear()

        #to fill the list from the gamebase
        cono = sqlite3.connect('gamebase.db')
        curo = cono.cursor()
        sel = 'SELECT player, ctg FROM stats;'
        curo.execute(sel)
        while True:
            record = curo.fetchone()
            if record == None:
                break
            elif record[1].upper() == 'BAT':
                listbat.append(list(record)[0])
            elif record[1].upper() == 'BWL':
                listbwl.append(list(record)[0])
            elif record[1].upper() == 'AR':
                listar.append(list(record)[0])
            elif record[1].upper() == 'WK':
                listwk.append(list(record)[0])

        #calling function to display the number sand points ' dis_num_pts '
        self.dis_num_pts()
        # rest displayinng how many players have been selected
        #self.n_bat.setText(str(nbat))
        #self.n_bwl.setText(str(nbwl))
        #self.n_wk.setText(str(nwk))
        #self.n_ar.setText(str(nar))
        ##displaying the points used and remaining
        #self.n_pts_rem.setText(str(ptsrem))
        #self.n_pts_used.setText(str(ptsused))


    #method for quitting
    #it sounds so......
    #lets go on
    def Quitmb(self):
        print('I worked so hard on this.\nOk Bye')
        sys.exit()

    ##to change the values of the list widget whenever a radio button is selected
    #getting list of team current
    def getteamlist(self):
        global teamlist
        teamlist.clear()
        self.eui.e_cb_team.clear()
        self.oui.cb_select.clear()
        cono = sqlite3.connect('gamebase.db')
        curo = cono.cursor()
        curo.execute("SELECT name FROM teams;")
        while True:
            record = curo.fetchone()
            if record == None:
                break
            elif record[0] not in teamlist:
                teamlist.append(record[0])
        self.eui.e_cb_team.addItems(teamlist)
        self.oui.cb_select.addItems(teamlist)
        return

    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 510)
        MainWindow.setMinimumSize(QtCore.QSize(480, 480))
        MainWindow.setMaximumSize(QtCore.QSize(550, 550))
        MainWindow.setWindowIcon(QtGui.QIcon('icons/ball.png'))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        

                        #radio buttons
        #Batsman Radio
        self.rb_bat = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_bat.setObjectName("rb_bat")
        self.horizontalLayout.addWidget(self.rb_bat)
        self.rb_bat.setEnabled(False)
        self.rb_bat.clicked.connect(self.getall)

        #Bowler Rario
        self.rb_bwl = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_bwl.setObjectName("rb_bwl")
        self.horizontalLayout.addWidget(self.rb_bwl)
        self.rb_bwl.setEnabled(False)
        self.rb_bwl.clicked.connect(self.getall)

        #wicket radio
        self.rb_wk = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_wk.setObjectName("rb_wk")
        self.horizontalLayout.addWidget(self.rb_wk)
        self.rb_wk.setEnabled(False)
        self.rb_wk.clicked.connect(self.getall)

        #alrounder radio
        self.rb_ar = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_ar.setObjectName("rb_ar")
        self.horizontalLayout.addWidget(self.rb_ar)
        self.rb_ar.setEnabled(False)
        self.rb_ar.clicked.connect(self.getall)

        
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 2)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 4, 3, 1, 2)

        #list1
        self.list1 = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.list1.setFont(font)
        self.list1.setObjectName("list1")
                        #testing insert widget
        #item = QtWidgets.QListWidgetItem()
        #self.list1.addItem(item)

        self.gridLayout.addWidget(self.list1, 5, 0, 1, 2)
        self.list1.itemDoubleClicked.connect(self.transfer12)

        
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setMinimumSize(QtCore.QSize(0, 0))
        self.label_image.setMaximumSize(QtCore.QSize(16777215, 70))
        self.label_image.setText("")
        self.label_image.setPixmap(QtGui.QPixmap("back2.jpg"))
        self.label_image.setScaledContents(True)
        self.label_image.setObjectName("label_image")
        self.gridLayout.addWidget(self.label_image, 2, 0, 1, 5)
        self.arrow = QtWidgets.QLabel(self.centralwidget)
        self.arrow.setMaximumSize(QtCore.QSize(26, 245))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.arrow.setFont(font)
        self.arrow.setObjectName("arrow")
        self.gridLayout.addWidget(self.arrow, 5, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.n_pts_rem = QtWidgets.QLabel(self.centralwidget)
        self.n_pts_rem.setObjectName("n_pts_rem")
        self.gridLayout.addWidget(self.n_pts_rem, 3, 1, 1, 2)
        self.g_team = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.g_team.setFont(font)
        self.g_team.setAlignment(QtCore.Qt.AlignCenter)
        self.g_team.setObjectName("g_team")
        self.gridLayout.addWidget(self.g_team, 0, 0, 1, 5)
        self.pts_used = QtWidgets.QLabel(self.centralwidget)
        self.pts_used.setMinimumSize(QtCore.QSize(140, 30))
        self.pts_used.setObjectName("pts_used")
        self.gridLayout.addWidget(self.pts_used, 3, 3, 1, 1)
        self.n_pts_used = QtWidgets.QLabel(self.centralwidget)
        self.n_pts_used.setObjectName("n_pts_used")
        self.gridLayout.addWidget(self.n_pts_used, 3, 4, 1, 1)
        #list2
        self.list2 = QtWidgets.QListWidget(self.centralwidget)
        self.list2.setMinimumSize(QtCore.QSize(204, 0))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.list2.setFont(font)
        self.list2.setObjectName("list2")
        self.gridLayout.addWidget(self.list2, 5, 3, 1, 2)
        self.list2.itemDoubleClicked.connect(self.transfer21)
        
        self.label_constituent = QtWidgets.QLabel(self.centralwidget)
        self.label_constituent.setMinimumSize(QtCore.QSize(140, 30))
        self.label_constituent.setObjectName("label_constituent")
        self.gridLayout.addWidget(self.label_constituent, 1, 0, 1, 1)
        self.pts_rem = QtWidgets.QLabel(self.centralwidget)
        self.pts_rem.setObjectName("pts_rem")
        self.gridLayout.addWidget(self.pts_rem, 3, 0, 1, 1)
        self.label_bwl = QtWidgets.QLabel(self.centralwidget)
        self.label_bwl.setGeometry(QtCore.QRect(70, 110, 140, 30))
        self.label_bwl.setMinimumSize(QtCore.QSize(140, 30))
        self.label_bwl.setObjectName("label_bwl")
        self.label_ar = QtWidgets.QLabel(self.centralwidget)
        self.label_ar.setGeometry(QtCore.QRect(280, 80, 140, 30))
        self.label_ar.setMinimumSize(QtCore.QSize(140, 30))
        self.label_ar.setObjectName("label_ar")
        self.label_wk = QtWidgets.QLabel(self.centralwidget)
        self.label_wk.setGeometry(QtCore.QRect(280, 110, 140, 30))
        self.label_wk.setMinimumSize(QtCore.QSize(140, 30))
        self.label_wk.setObjectName("label_wk")
        self.n_bat = QtWidgets.QLabel(self.centralwidget)
        self.n_bat.setGeometry(QtCore.QRect(210, 80, 31, 31))
        self.n_bat.setObjectName("n_bat")
        self.n_bwl = QtWidgets.QLabel(self.centralwidget)
        self.n_bwl.setGeometry(QtCore.QRect(210, 110, 31, 31))
        self.n_bwl.setObjectName("n_bwl")
        self.n_ar = QtWidgets.QLabel(self.centralwidget)
        self.n_ar.setGeometry(QtCore.QRect(420, 80, 31, 31))
        self.n_ar.setObjectName("n_ar")
        self.n_wk = QtWidgets.QLabel(self.centralwidget)
        self.n_wk.setGeometry(QtCore.QRect(420, 110, 31, 31))
        self.n_wk.setObjectName("n_wk")
        self.label_bat = QtWidgets.QLabel(self.centralwidget)
        self.label_bat.setGeometry(QtCore.QRect(70, 80, 140, 30))
        self.label_bat.setMinimumSize(QtCore.QSize(140, 30))
        self.label_bat.setObjectName("label_bat")
        self.label_image.raise_()
        self.g_team.raise_()
        self.pts_used.raise_()
        self.n_pts_rem.raise_()
        self.n_pts_used.raise_()
        self.list1.raise_()
        self.arrow.raise_()
        self.list2.raise_()
        self.label_15.raise_()
        self.n_bwl.raise_()
        self.label_wk.raise_()
        self.label_bwl.raise_()
        self.n_bat.raise_()
        self.label_ar.raise_()
        self.n_ar.raise_()
        self.n_wk.raise_()
        self.label_bat.raise_()
        self.label_constituent.raise_()
        self.pts_rem.raise_()
        MainWindow.setCentralWidget(self.centralwidget)


        #menu bar is starting mhere
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage = QtWidgets.QMenu(self.menubar)
        self.menuManage.setObjectName("menuManage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #defining creating new team menu button
        self.mb_new = QtWidgets.QAction(MainWindow)
        self.mb_new.setVisible(True)
        self.mb_new.setObjectName("mb_new")
        self.mb_new.triggered.connect(self.NewUI)       #trigger new

        #defining loading a team menu button
        self.mb_load = QtWidgets.QAction(MainWindow)
        self.mb_load.setObjectName("mb_load")
        self.mb_load.triggered.connect(self.OpenUI)     #triggereg OPen        
        
        #defining saving a team menu button
        self.mb_save = QtWidgets.QAction(MainWindow)
        self.mb_save.setObjectName("mb_save")
        self.mb_save.setDisabled(True)                  #grey out save menubutton
        self.mb_save.triggered.connect(self.SaveUI)     #trigger SAVE

        #defining evaluate team menu button
        self.mb_evaluate = QtWidgets.QAction(MainWindow)
        self.mb_evaluate.setObjectName("mb_evaluate")
        self.mb_evaluate.triggered.connect(self.EvaUI)  #trigger Evaluate


        #defining quit application menu button
        self.mb_quit = QtWidgets.QAction(MainWindow)
        self.mb_quit.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.mb_quit.setMenuRole(QtWidgets.QAction.QuitRole)
        self.mb_quit.setObjectName("mb_quit")
        self.mb_quit.triggered.connect(self.Quitmb)     #trigger Quit
        
        self.menuManage.addAction(self.mb_new)
        self.menuManage.addAction(self.mb_load)
        self.menuManage.addAction(self.mb_save)
        self.menuManage.addSeparator()
        self.menuManage.addAction(self.mb_evaluate)
        self.menuManage.addSeparator()
        self.menuManage.addAction(self.mb_quit)
        self.menubar.addAction(self.menuManage.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #new window clicked button action        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fantasy Cricket Game"))
        self.rb_bat.setText(_translate("MainWindow", "BAT"))
        self.rb_bwl.setText(_translate("MainWindow", "BWL"))
        self.rb_wk.setText(_translate("MainWindow", "WK"))
        self.rb_ar.setText(_translate("MainWindow", "AR"))
        self.label_15.setText(_translate("MainWindow", "Player Selected"))
        __sortingEnabled = self.list1.isSortingEnabled()
        self.list1.setSortingEnabled(False)
        #item = self.list1.item(0)
        #item.setText(_translate("MainWindow", "New Item"))

        self.list1.setSortingEnabled(__sortingEnabled)
        self.arrow.setText(_translate("MainWindow", "-->"))
        self.n_pts_rem.setText(_translate("MainWindow", "#"))
        self.g_team.setText(_translate("MainWindow", "#team name"))
        self.pts_used.setText(_translate("MainWindow", "Points Used:"))
        self.n_pts_used.setText(_translate("MainWindow", "#"))
        self.label_constituent.setText(_translate("MainWindow", "Team Constitents"))
        self.pts_rem.setText(_translate("MainWindow", "Points remaining:"))
        self.label_bwl.setText(_translate("MainWindow", "Bowlers (BWL):"))
        self.label_ar.setText(_translate("MainWindow", "All-rounders (AR):"))
        self.label_wk.setText(_translate("MainWindow", "Wicket-Keepers (WK):"))
        self.n_bat.setText(_translate("MainWindow", "#"))
        self.n_bwl.setText(_translate("MainWindow", "#"))
        self.n_ar.setText(_translate("MainWindow", "#"))
        self.n_wk.setText(_translate("MainWindow", "#"))
        self.label_bat.setText(_translate("MainWindow", "Batsmen (BAT):"))

        #display of menu bar
        self.menuManage.setTitle(_translate("MainWindow", "Manage"))

        #New button
        self.mb_new.setText(_translate("MainWindow", "New"))
        self.mb_new.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.mb_new.setStatusTip('Create a New Team.')
        

        #Load button
        self.mb_load.setText(_translate("MainWindow", "Load"))
        self.mb_load.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.mb_load.setStatusTip('Load an existing team from the database.')

        #save button
        self.mb_save.setText(_translate("MainWindow", "Save"))
        self.mb_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.mb_save.setStatusTip("Save the team you've just created.")

        #evaluate button
        self.mb_evaluate.setText(_translate("MainWindow", "Evaluate"))
        self.mb_evaluate.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.mb_evaluate.setStatusTip("Evaluate any team from the database.")

        #quit buttin
        self.mb_quit.setText(_translate("MainWindow", "Quit"))
        self.mb_quit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.mb_quit.setStatusTip("Don't click this please. You don't want to quit do you?")

 


if __name__ == "__main__":
    import sys
    teamlist =[]                #list of teams
    teamname =''                #teamname is new or load
    listbat = []                #list of batsmen
    listbwl = []                #list of bowlers
    listwk = []                 #list of wcket keepers
    listar = []                 #list of allrounders
    listselected = []           #list of selected
    listpoints = []             #list of points
    nbat = 0
    nbwl = 0
    nar = 0
    nwk = 0
    ptsused = 0
    ptsrem = 1000
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
