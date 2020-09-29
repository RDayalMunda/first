from tkinter import*
import time
import random


root = Tk()
root.title("Bounce")
root.resizable(0,0)

##topmost window in the desktop
root.wm_attributes("-topmost",1)

canvas = Canvas(root, width = 510, height = 500, bd = 0, highlightthickness = 0)
canvas.pack()
root.update()

class gball:
    def __init__(self, canvas, color, paddle):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25, fill = color)##creates the oval and passes the ID
        self.canvas.move(self.id, 245,100)
        start = [-3,-2,2,3]
        self.paddle = paddle
        random.shuffle(start)
        self.x = start[0]
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()##to get the canvas height and width
        self.canvas_width = self.canvas.winfo_width()
        self.gameon= True

    def hit_paddle(self, pos):
        paddle_pos= self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3]>= paddle_pos[1] and pos[3]<= paddle_pos[3]:
                return True
        return False

            
    def draw(self):#refresh the canvas
        self.canvas.move(self.id,self.x, self.y) 
        pos = self.canvas.coords(self.id)##this return the current position of the ball
        if pos[1]<= 0:
            self.y = 2
        if pos[3] >= self.canvas_height:
            self.gameon = False
            self.y =0
         
        if pos[0]<= 0 :
            self.x = 2
        if pos[2]>= self.canvas_width:
            self.x = -2
        if self.hit_paddle(pos) == True:
            self.y = -3



class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10, fill=color)
        self.canvas.move(self.id,200,300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
    def draw(self):
        self.canvas.move(self.id, self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0
    def turn_left(self, evt):
        self.x = -2
        print('L')
    def turn_right(self, evt):
        print('R')
        self.x = 2


paddle = Paddle(canvas, 'blue')        
ball = gball(canvas, 'red', paddle)


while ball.gameon:
    ball.draw()
    paddle.draw()
    root.update_idletasks()##update background
    root.update()##update ball
    time.sleep(0.02)

    
root.mainloop()

#######################3
#bd is th e border
##using bind_all
#coords.id  -> return the cordinated of the object with that id
