from tkinter import Tk, Canvas
from math import sin, cos, radians

class Game:
    def __init__(self):
        self.root = Tk()
        self.area = Canvas(self.root, width=500, height=500, bg='lightgreen')
        self.area.pack()
        self.ballid = self.area.create_oval(30,50,50,70, fill='red')
        self.paddleid = self.area.create_rectangle(210,400,310,410, fill="blue")
        self.points_text = self.area.create_text(250,450, text='0', font=('times', 20))
        self.speed=12.0 ##speed of ball
        self.xspeed=self.speed*sin(radians(40)) ##speed of ball horizontally
        self.yspeed=self.speed*sin(radians(40)) ##speed of ball vertically
        self.pspeed=0 ##speed of paddle
        self.recall='' ##for AFTER method
        self.points=0 ##ponits counter
        self.gameon = True
        
        self.redraw_screen()
        ##controls for paddle
        self.area.bind_all('<KeyPress-Left>', self.turn_left)
        self.area.bind_all('<KeyPress-Right>', self.turn_right)
        #self.area.bind_all('<Control-n>', self.new_game)
        self.root.mainloop()

    def draw_points(self):
        self.points=self.points + self.speed/50
        self.area.itemconfig(self.points_text, text=round(self.points), fill="#991122")
            

    def redraw_screen(self):
        self.draw_ball()
        self.paddle_hit()
        self.draw_paddle()
        self.draw_points()
        if self.gameon:
            self.recall=self.root.after(17, self.redraw_screen)
        else:
            self.root.after_cancel(self.recall)

        
    def draw_ball(self):
        #left or right boundary
        if self.area.coords(self.ballid)[0]<0 or self.area.coords(self.ballid)[2]>500:
            self.xspeed = -self.xspeed
        ##top and bottom boundary
        if self.area.coords(self.ballid)[1]<0:
            self.yspeed= -self.yspeed
        if self.area.coords(self.ballid)[3]>500:
            self.xspeed=0
            self.yspeed=0
            self.game_over()
        self.area.move(self.ballid,self.xspeed,self.yspeed)
        #ball location
        #print(self.area.coords(self.ballid))
        #canvas
        #print(self.area.winfo_height(), self.area.winfo_width())
        
    def draw_paddle(self):
        self.area.move(self.paddleid, self.pspeed,0)
        if self.area.coords(self.paddleid)[0]<=0 or self.area.coords(self.paddleid)[2]>=500:
            self.pspeed=0
        
    def paddle_hit(self):
        cb = self.area.coords(self.ballid)[0]+10
        cp = self.area.coords(self.paddleid)[0]+50
        ##to check if paddle is is paddle level
        if self.area.coords(self.ballid)[3] >= 400:
            ##if paddle is hit
            if cb > self.area.coords(self.paddleid)[0] and cb < self.area.coords(self.paddleid)[2] and self.area.coords(self.ballid)[3]<405:
                dis = cp-cb
                self.xspeed=-self.speed*sin(radians(dis*1.3))
                self.yspeed=-self.speed*cos(radians(dis*1.3))
    
    def turn_left(self, arg):
        self.pspeed=-5
        
    def turn_right(self, arg):
        self.pspeed=5

    def game_over(self):
        self.area.create_text(250,250, text="Game over!", font=("times", 30))
        #self.area.create_text(250,300, text="Press Ctrl+N for new game!", font=("times", 10))
        self.gameon=False

        
    
    
bounce =Game()
