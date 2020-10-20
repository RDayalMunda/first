#font=('Fixedsys', 20)
from tkinter import Tk, Canvas
#from math import floor
from random import choice
#from time import sleep


##flag.         ⚐⚐⚐⚐⚐⚐⚐⚑⚑⚑⚑⚑⚑⚑⚑?????

#               ֎֎֎֎     ꙮꙮꙮꙮ
##bomb unicode character
class minesweeper:
    def __init__(self,difficulty):
        self.difficulty = difficulty
        self.root = Tk()
        self.root.title('MineSweeper')
        self.ms = Canvas(self.root, height=475, width = 475)
        self.ms.pack()
        
        self.ids = {}
        #key= 'name of widgets', 'box_0'
        ##these are values ain list
        #0. rectangle id number - int
        #1. text id number
        #2. mines list - bool
        #3. number list - int
        #4. active list - bool
        #5. flag list - bool
        #6. unknown flags - bool
        self.time_min = 0
        self.time_sec = 0
        self.mines_rem = 40
        self.game_on = False
        self.first_click = False

        self.timer = None
        
        self.creator()
        self.ui_creator()
        self.reset()
        self.root.mainloop()
        
        
    #removes all bombs and reset states
    def mine_setter(self):
        i=0
        while i < 40:
            ch = choice(range(225))
            if self.ids['box_'+str(ch)][2]== False:
                self.ids['box_'+str(ch)][2] = True
                i+=1
        self.number_setter()

    #number around the mines
    def number_setter(self):
        for i in range(225):
            name = 'box_'+str(i)
            if self.ids[name][2]:
                if i%15 > 0:
                    self.ids['box_'+str(i-1)][3] += 1   #left
                    if i>14:
                        self.ids['box_'+str(i-16)][3] += 1 #topleft
                    if i<210:
                        self.ids['box_'+str(i+14)][3] += 1 #bottomleft
                if i%15 < 14:
                    self.ids['box_'+str(i+1)][3] += 1   #right
                    if i>14:
                        self.ids['box_'+str(i-14)][3] += 1 #topright
                    if i<210:
                        self.ids['box_'+str(i+16)][3] += 1 #bottomright
                if i>14:
                    self.ids['box_'+str(i-15)][3] += 1  #top
                if i<210:
                    self.ids['box_'+str(i+15)][3] += 1  #bottom    
            
    def reset(self):
        self.game_on=True
        self.first_click = False
        self.time_min = 0
        self.time_sec = 0
        self.mines_rem = 40
        self.ms.itemconfig(self.ids['mine_box'][1], text=str(self.mines_rem))
        self.ms.itemconfig(self.ids['timer_box'][1], text=str('00:00'))
        for i in range(225):
            name = 'box_'+str(i)
            ## resetting the variables
            self.ids[name][2]= False
            self.ids[name][3]= 0
            self.ids[name][4]= False
            self.ids[name][5]= False
            self.ids[name][5]= False

            ##reset the grids to back
            self.ms.itemconfig(self.ids[name][0], fill='#dddddd', outline='#000000')
            self.ms.itemconfig(self.ids[name][1], text='')
        try:
            self.time_stopper()
        except:
                pass
        self.mine_setter()
        #self.time_starter()

    ##call this to loop with time
    def time_starter(self):
        if self.game_on:
            mins = str(self.time_min)
            secs = str(self.time_sec)
            if self.time_min <=9:
                mins = '0'+mins
            if self.time_sec <=9:
                secs = '0'+secs
            clock = mins+':'+secs
            self.ms.itemconfig(self.ids['timer_box'][1], text = clock)
            self.timer = self.root.after(1000, self.time_starter)
            self.time_sec+=1
            if self.time_sec>=60:
                self.time_sec=0
                self.time_min+=1
        else:
            self.time_stopper()
            
    def time_stopper(self):
        self.root.after_cancel(self.timer)
        self.timer = None
        

    def ui_creator(self):
        ##mines counter area
        num = self.ms.create_rectangle(50,15, 150, 60, fill='#888888', tags='mine_box')
        text = self.ms.create_text(99,37, text='030', font=('Fixedsys', 25), fill='#ff2222', tags= 'mine_text')
        self.ids['mine_box']=[]
        self.ids['mine_box'].append(num)
        self.ids['mine_box'].append(text)

        ##reset button area
        num = self.ms.create_rectangle(170,18, 270, 57, fill='#888888', tags='reset_box')
        text = self.ms.create_text(220,37, text='New', font=('Fixedsys', 25), fill='#2222ff', tags= 'reset_text')
        self.ids['reset_box']=[]
        self.ids['reset_box'].append(num)
        self.ids['reset_box'].append(text)
        ##thes for rectangle
        self.ms.tag_bind(self.ids['reset_box'][0], "<Enter>", lambda event: self.cursor_hover('reset_box'))
        self.ms.tag_bind(self.ids['reset_box'][0], "<Leave>", lambda event: self.cursor_leave('reset_box'))
        self.ms.tag_bind(self.ids['reset_box'][0], "<Button-1>", lambda event: self.reset())
        ##these for the text
        self.ms.tag_bind(self.ids['reset_box'][1], "<Enter>", lambda event: self.cursor_hover('reset_box'))
        self.ms.tag_bind(self.ids['reset_box'][1], "<Leave>", lambda event: self.cursor_leave('reset_box'))
        self.ms.tag_bind(self.ids['reset_box'][1], "<Button-1>", lambda event: self.reset())

        ##timer box area
        num = self.ms.create_rectangle(290,15, 425, 60, fill='#888888', tags='time_box')
        text = self.ms.create_text(357,37, text='00:00', font=('Fixedsys', 25), fill='#22ff22', tags= 'timer_text')
        self.ids['timer_box']=[]
        self.ids['timer_box'].append(num)
        self.ids['timer_box'].append(text)
        
        

    def creator(self):
        ##easy is     9x9 grid
        #box size = 24x24
        #distance b/w them = 1
        for i in range(15):
            for j in range(15):
                num = i*15+j
                name = 'box_'+str(num)
                x1= 50+j*25
                x2= x1+23
                y1= 75+i*25
                y2 = y1+23
                #print(name,x1,x2,y1,y2)
                self.ids[name]=[]
                num=self.ms.create_rectangle(x1,y1,x2,y2,
                                                        fill='#dddddd',
                                                        tags=name)
                text= self.ms.create_text((x1+x2)/2, (y1+y2)/2, text = '',font=('', 15))
                self.ids[name].append(num)      #0 added the ID in 0
                self.ids[name].append(text)     #1 text id number
                self.ids[name].append(False)    #2 mines
                self.ids[name].append(0)        #3 numbers
                self.ids[name].append(False)    #4 active
                self.ids[name].append(False)    #5 flags
                self.ids[name].append(False)    #6 unknown
            
        for i in self.ids:
            self.anims(i)
            #print(i)

    #for binding all the 255 boxes with events like hover and clicks
    def anims(self,x):
        ##these for the box
        self.ms.tag_bind(self.ids[x][0], "<Enter>", lambda event: self.cursor_hover(x))
        self.ms.tag_bind(self.ids[x][0], "<Leave>", lambda event: self.cursor_leave(x))
        self.ms.tag_bind(self.ids[x][0], "<Button-1>", lambda event: self.left_clicked(x))
        self.ms.tag_bind(self.ids[x][0], "<Button-3>", lambda event: self.right_clicked(x))
        ##these for the text
        self.ms.tag_bind(self.ids[x][1], "<Enter>", lambda event: self.cursor_hover(x))
        self.ms.tag_bind(self.ids[x][1], "<Leave>", lambda event: self.cursor_leave(x))
        self.ms.tag_bind(self.ids[x][1], "<Button-1>", lambda event: self.left_clicked(x))
        self.ms.tag_bind(self.ids[x][1], "<Button-3>", lambda event: self.right_clicked(x))
        

        
    def cursor_hover(self,name):
        if self.game_on:
            if name == 'reset_box':
                self.ms.itemconfig(self.ids[name][0], fill='#aaaaaa')
            elif not self.ids[name][4]:
                self.ms.itemconfig(self.ids[name][0], fill='#eeffee')

    def cursor_leave(self,name):
        if self.game_on:
            if name == 'reset_box':
                self.ms.itemconfig(self.ids[name][0], fill='#888888')
            elif not self.ids[name][4]:
                self.ms.itemconfig(self.ids[name][0], fill='#dddddd')

    def left_clicked(self,name):
        if self.game_on:
            if not self.ids[name][5] and not self.ids[name][6]:#to not accept click over flag or mark
                if self.ids[name][2]==True and not self.first_click:#iif clicked on mine
                    self.reset()
                elif self.ids[name][2] and self.first_click:
                    self.stepped_on_mine(name)
                    return
                else:
                    if not self.first_click:
                        self.first_click = True
                        self.time_starter()
                    #print('left', name)
                    if not self.ids[name][4]:
                        self.ids[name][4] = True
                        self.ms.itemconfig(self.ids[name][0], fill='#eeeeee', outline = '#777777')
                        if self.ids[name][3] != 0:
                            self.ms.itemconfig(self.ids[name][1], text= str(self.ids[name][3]))
                        num=int(name[name.index('_')+1:])
                        if self.ids[name][3]==0:
                            #print(num//15, num%15)
                            self.stepped_on_blank(num)
    
    def right_clicked(self,name):
        if not self.ids[name][4]:
            if self.ids[name][5]== False and self.ids[name][6]== False:
                self.ms.itemconfig(self.ids[name][1], text = '⚐')
                self.ids[name][5] = True
                self.mines_rem-=1
                self.ms.itemconfig(self.ids['mine_box'][1], text=str(self.mines_rem))
                self.win_check()
                
            elif self.ids[name][5]== True and self.ids[name][6]== False:
                self.ms.itemconfig(self.ids[name][1], text = '?')
                self.ids[name][5] = False
                self.ids[name][6] = True
                self.mines_rem+=1
                self.ms.itemconfig(self.ids['mine_box'][1], text=str(self.mines_rem))

            elif self.ids[name][5]== False and self.ids[name][6]== True:
                self.ms.itemconfig(self.ids[name][1], text = '')
                self.ids[name][5] = False
                self.ids[name][6] = False

            else:#if any other case arrises
                self.ms.itemconfig(self.ids[name][1], text = '')
                self.ids[name][5] = False
                self.ids[name][6] = False
                
    #this function would find the nearby blank positions and activate them
    def stepped_on_blank(self, i):
        ##in 'i' position the [name][3] == 0
        #print(i)
        if i%15 < 14: ##rights boxes
            if not self.ids['box_'+str(i+1)][4]:
                print(i//15, i%15)
                self.left_clicked('box_'+str(i+1))
        if i%15 > 0: ##left boxes
            if not self.ids['box_'+str(i-1)][4]:
                print(i//15, i%15)
                self.left_clicked('box_'+str(i-1))
        if i > 14: ##up boxes
            if not self.ids['box_'+str(i-15)][4]:
                print(i//15, i%15)
                self.left_clicked('box_'+str(i-15))
        if i < 210: ##down boxes
            if not self.ids['box_'+str(i+15)][4]:
                print(i//15, i%15)
                self.left_clicked('box_'+str(i+15))
        if i>14 and i%15 > 0:##up left
            if not self.ids['box_'+str(i-16)][4]:
                print(i//15, i%15)
                self.left_clicked('box_'+str(i-16))
        if i>14 and i%14 <14:##up right
            if not self.ids['box_'+str(i-14)][4]:
                print(i//15, i%15)
                self.left_clicked('box_'+str(i-14))
        if i<210 and i%15 > 0: #down left
            if not self.ids['box_'+str(i+14)][4]:
                print(i//15, i%15)
                self.left_clicked('box_'+str(i+14))
        if i<210 and i%15 < 14: #down left
            if not self.ids['box_'+str(i+16)][4]:
                print(i//15, i%15)
                self.left_clicked('box_'+str(i+16))


    def win_check(self):
        check = 40
        if self.mines_rem == 0:
            for i in range(225):
                if self.ids['box_'+str(i)][2] and self.ids['box_'+str(i)][5]:
                    check-=1
                    print(self.mines_rem, check)
                    
        if check == 0:
            self.game_on = False
            self.win_game()
            
                    
                
        
    def win_game(self):
        for i in range(225):
            if self.ids['box_'+str(i)][2]:
                self.ms.itemconfig(self.ids['box_'+str(i)][0], fill='#7777ff')
                self.ms.itemconfig(self.ids['mine_box'][0], fill='#33ff33')
                self.ms.itemconfig(self.ids['mine_box'][1], text='Won')
                
                
                
    
    def stepped_on_mine(self, name):
        self.game_on = False
        for i in range(225):
            if self.ids['box_'+str(i)][2]:
                self.ms.itemconfig(self.ids['box_'+str(i)][0], fill = '#cc0000')
        self.ms.itemconfig(self.ids[name][0], fill = '#ff0000')


m1 = minesweeper('Easy')
