from tkinter import Tk, Canvas, E, PhotoImage
#import time
from math import floor
from random import choice

class puzzle():
    # x is number of rows, y = number of columns
    def __init__(self, x=3, y=3):
        #name of the window
        self.root = Tk()
        self.root.title('Number Puzzle')
        self.root.iconphoto(False, PhotoImage(file='info.png'))
        #name of canvas = 'puzz'
        self.puzz = Canvas(self.root, width= 720, height = 550, bg='#cccccc')
        self.puzz.pack()

        self.ids = {}
        self.timer=[0,0]
        self.timejob = None#after function
        self.timeshuffle = None#after function
        self.shufflepoints = 0 #counting shuffles

        self.x = x
        self.y = y
        self.grids ={}

        self.allowables = {}# this gives the allowable swap
        
        self.__grid_creator__()
        self.__clock_creator__()
        #self.__timer_clock__()
        self.__get_allowables__()
        self.root.mainloop()


    ##get allowables swap positions
    def __get_allowables__(self):
        for i in self.allowables:
            if i%self.y!=0:
                self.allowables[i].append(i-1)
            if i%self.y!=self.y-1:
                self.allowables[i].append(i+1)
            if i>=self.y:
                self.allowables[i].append(i-self.y)
            if i//self.y!=self.x-1:
                self.allowables[i].append(i+self.y)
            

    #refreshes the time_text  
    def __timer_clock__(self):
        self.timer[1]+=1
        #getting mis and secs
        if self.timer[1]>=60:
            self.timer[1]=0
            self.timer[0]+=1 
        #converting them into displayanle format
        if self.timer[1]<=9:
            secs = '0'+str(self.timer[1])
        else:
            secs = str(self.timer[1])
        if self.timer[0]<=9:
            mins = '0'+str(self.timer[0])
        else:
            mins = str(self.timer[0])
        timer=mins+':'+secs
        #time over condition
        if self.timer[0]>=59:
            self.__time_stopper__("Stop")
        else:
            self.puzz.itemconfig(self.ids['clock_time'], text =timer, fill= '#000000')
            self.timejob=self.root.after(1000, self.__timer_clock__)
    
            
    def __time_stopper__(self,msg):
        self.root.after_cancel(self.timejob)
        self.timejob = None
        self.puzz.itemconfig(self.ids['clock_time'], text =msg, fill='#ff4444')

        
    def __clock_creator__(self):
        ##for creating clock and other button
        #name used for clock_text = 'clock_time' and box is = 'clock_box'
        self.ids['clock_box']=self.puzz.create_rectangle(520,300,700,350, fill='#eeeeee', tag ='clock_box')
        self.ids['clock_time']= self.puzz.create_text(610,325, text='Timer', font = 'tester 20',tag = 'clock_time')

        self.ids['shuffle_box']=self.puzz.create_rectangle(520,200,700,250, fill='#eeeeee', tag ='shuffle_box')
        self.ids['shuffle_text']= self.puzz.create_text(610,225, text='shuffle', font = 'tester 20',tag = 'shuffle_text')
        self.puzz.tag_bind(self.ids['shuffle_box'], "<Enter>", lambda event: self.Entered('shuffle_box'))
        self.puzz.tag_bind(self.ids['shuffle_box'], "<Leave>", lambda event: self.Leaved('shuffle_box')) 
        self.puzz.tag_bind(self.ids['shuffle_text'], "<Enter>", lambda event: self.Entered('shuffle_box'))
        self.puzz.tag_bind(self.ids['shuffle_text'], "<Leave>", lambda event: self.Leaved('shuffle_box'))
        self.puzz.tag_bind(self.ids['shuffle_box'], "<Button-1>", self.__shuffler__)
        self.puzz.tag_bind(self.ids['shuffle_text'], "<Button-1>",self.__shuffler__)
        

    def clock_reset(self):
        self.timer[0]=0
        self.timer[1]=0

    def __grid_creator__(self):
        #getting row and column number
        for i in range(self.x):
            for j in range(self.y):
                self.grids[i*self.y+j]=[i,j]

        #for getting the coordinates
        for i in self.grids:
            x1 = self.grids[i][1] * 500/self.y+20
            x1 = floor(x1)
            x2 = x1 + 500/self.y -5
            x2 = floor(x2)
            y1 = self.grids[i][0] * 500/self.x+20
            y1 = floor(y1)
            y2 = y1 + 500/self.x -5
            y2 = floor(y2)
            self.grids[i].append(x1)
            self.grids[i].append(y1)
            self.grids[i].append(x2)
            self.grids[i].append(y2)
            bname = 'slot_'+str(i)
            tname = 'text_'+str(i)
            self.ids[bname]=self.puzz.create_rectangle(self.grids[i][2],self.grids[i][3],self.grids[i][4],self.grids[i][5], tags = bname, fill='#eeeeee')
            self.ids[tname]=self.puzz.create_text((self.grids[i][2]+self.grids[i][4])/2, (self.grids[i][3]+self.grids[i][5])/2, text=i, tags=tname, font = 'tester 20')
            bname = 'slot_'+str(i)
            tname = 'text_'+str(i)
            self.event_binder(bname, tname)
            self.grids[i].append(i)
            self.allowables[i]=[]

    # with the last box made empty
        self.puzz.itemconfig(self.ids['slot_'+str(self.x*self.y-1)], fill='', outline='')
        self.puzz.delete('text_'+str(self.x*self.y-1))

    #to bind the slots with the Enter and leave events and click
    def event_binder(self,x,y):
        self.puzz.tag_bind(self.ids[x], "<Enter>", lambda event: self.Entered(x))   
        self.puzz.tag_bind(self.ids[x], "<Leave>", lambda event: self.Leaved(x))   
        self.puzz.tag_bind(self.ids[y], "<Enter>", lambda event: self.Entered(x))
        self.puzz.tag_bind(self.ids[y], "<Leave>", lambda event: self.Leaved(x))
        self.puzz.tag_bind(self.ids[x], "<Button-1>", lambda event: self.clicked(x))
        self.puzz.tag_bind(self.ids[y], "<Button-1>", lambda event: self.clicked(x))
        
        

    #when cursor hovers over the slot
    def Entered(self, x):
        if x != 'slot_'+str(self.x*self.y-1):
            self.puzz.itemconfig(self.ids[x], fill='#ffffff')
        else:
            self.puzz.itemconfig(self.ids['slot_'+str(self.x*self.y-1)], fill='', outline='')
    
    #when cursor leaved the slot
    def Leaved(self, x):
        if x != 'slot_'+str(self.x*self.y-1):
            self.puzz.itemconfig(self.ids[x], fill='#eeeeee')
        else:
            self.puzz.itemconfig(self.ids['slot_'+str(self.x*self.y-1)], fill='', outline='')

    # notices the click and decides if the swapper fuction is to be called   
    def clicked(self, x):
        cid = int(x[5:])#it is the actual name of the box that is clicked on
        cpos = self.grids[cid][6]#it is its position on the canvas
        bpos = self.grids[self.x*self.y-1][6] # it is postion of blank in canvas
        if cpos in self.allowables[bpos]:
            self.swapper(cid)
            


    #swappes the clicked slot with the blank slot
    def swapper(self, x):
        ##print(x,self.grids[x][6], '\t',self.grids[self.x*self.y-1][6])
        ccoor=self.puzz.coords('slot_'+str(x))
        bcoor=self.puzz.coords('slot_'+str(self.x*self.y-1))
        #now moving the slots
        # and changing their data respectively
        #blank moving left
        if ccoor[0] < bcoor[0]:
            self.puzz.move(self.ids['slot_'+str(self.x*self.y-1)],-100, 0)
            self.puzz.move(self.ids['slot_'+str(x)], 100, 0)
            self.puzz.move(self.ids['text_'+str(x)], 100, 0)
            self.grids[self.x*self.y-1][6]=self.grids[self.x*self.y-1][6]-1
            self.grids[x][6]=self.grids[x][6]+1
        elif ccoor[1] < bcoor[1]:
            self.puzz.move(self.ids['slot_'+str(self.x*self.y-1)], 0,-100)
            self.puzz.move(self.ids['slot_'+str(x)], 0, 100)
            self.puzz.move(self.ids['text_'+str(x)], 0, 100)
            self.grids[self.x*self.y-1][6]=self.grids[self.x*self.y-1][6]-self.y
            self.grids[x][6]=self.grids[x][6]+self.y
        elif ccoor[0] > bcoor[0]:
            self.puzz.move(self.ids['slot_'+str(self.x*self.y-1)], 100, 0)
            self.puzz.move(self.ids['slot_'+str(x)], -100, 0)
            self.puzz.move(self.ids['text_'+str(x)], -100, 0)
            self.grids[self.x*self.y-1][6]=self.grids[self.x*self.y-1][6]+1
            self.grids[x][6]=self.grids[x][6]-1
        elif ccoor[1] > bcoor[1]:
            self.puzz.move(self.ids['slot_'+str(self.x*self.y-1)], 0, 100)
            self.puzz.move(self.ids['slot_'+str(x)], 0, -100)
            self.puzz.move(self.ids['text_'+str(x)], 0, -100)
            self.grids[self.x*self.y-1][6]=self.grids[self.x*self.y-1][6]+self.y
            self.grids[x][6]=self.grids[x][6]-self.y

        ###checking if all the slots are in positions
        self.__checker__()
    
    def __shuffler__(self,x):
        #print('shuffle was called')
        self.timer = [0,0]
        try:
            self.__time_stopper__('wait')
        except:
            self.__timer_clock__()
            self.__time_stopper__('wait')
        #current poition of blanks          self.grids[24][6]
        #getting available swapsposition    self.allowables[self.grids[24][6]]
        if self.timeshuffle == None:
            self.shuffler2()
        

    def shuffler2(self):
        if self.shufflepoints <= 10:
            ch = []
            for i in self.allowables[self.grids[24][6]]:
                for j in range(25):
                    if self.grids[j][6]==i:
                        ch.append(j)
            ch=choice(ch)
            ch = 'slot_'+str(ch)
            self.clicked(ch)
            ##print(self.timeshuffle)
            self.shufflepoints+=1
            self.timeshuffle=self.root.after(100, self.shuffler2)
        else:
            self.root.after_cancel(self.timeshuffle)
            self.shufflepoints = 0
            self.timeshuffle=None
            self.__timer_clock__()


    def __checker__(self):
        'checking if the grid has been restored'
        if self.timeshuffle==None:
            correct=0
            for i in range(25):
                if i == self.grids[i][6]:
                    correct+=1
            if correct == 25:
                #print('completed')
                #converting them into displayanle format
                if self.timer[1]<=9:
                    secs = '0'+str(self.timer[1])
                else:
                    secs = str(self.timer[1])
                if self.timer[0]<=9:
                    mins = '0'+str(self.timer[0])
                else:
                    mins = str(self.timer[0])
                timer=mins+':'+secs
                try:
                    self.__time_stopper__(timer)
                except:
                    pass

    def __reset__(self, x):
        pass
        #del game
        #print('game deleted')
        #still working on it
    
    def __del__(self):
        pass
        #still working on  it
        #print('Destructor was called')

game= puzzle(5,5)
del game
