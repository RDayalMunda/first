import sqlite3
import UIevaluate

def tryon(player):          #gets the name of player from the runninf function
    cono = sqlite3.connect('gamebase.db')
    curo = cono.cursor()
    sel = "SELECT * FROM match WHERE player = '"+player+"';"
    curo.execute(sel)
    record = curo.fetchone()
    pts = 0
    if record[2] > 0:           #if ever player a ball
        pts = pts + batting_points(record[1], record[3], record[4], record[2])
    if record[5] > 0:           #if ever delivered a ball
        pts = pts + bowling_points(record[8], record[5], record[7])
    #fielding is to be done by everyone
    pts = pts + fielding_points(record[9], record[10], record[11])
    return pts

##  only if faced > 0 he should be passed through batting points
##  only if bowled > 0 he should be passed through bowling_points
##  every one should be passed through fielding_points
    
def batting_points(a, b, c, d):
    "Points scored in Batting."
    runs =a
    fours=b
    sixes=c
    balls=d
    
    # 1 points for 2 runs
    pts=runs/2

    # half century
    if runs > 50:
        pts=pts+5
        
    # century
    if runs > 100:
        pts=pts+10
        
    # strike rate 80-100
    if runs/balls >=0.8 and runs/balls<=1:
        pts=pts+2
        
    # srike rate > 100
    if  runs/balls >1:
        pts=pts+4
        
    # fours
    pts = pts + fours
    
    #sixes
    pts = pts + sixes*2

    #return thr points scored by batsmen
    return pts
    
def bowling_points(a,b,c):
    "Points scored in Bowling."
    wkts=a
    overs=b/6
    runs=c
    
    # 10 for each wickets
    pts= wkts*10

    # 3 wickets
    if wkts >= 3:
        pts = pts + 5

    # 5 wickets
    if wkts >= 5:
        pts = pts + 10

    # economic rates
    if runs/overs < 2:
        pts = pts + 10
    elif runs/overs >= 2 and runs/overs < 3.5:
        pts = pts + 7
    elif runs/overs >= 3.5 and runs/overs <= 4.5:
        pts = pts + 4

    # return the points scored by bowlers
    return pts
    
def fielding_points(x , y, z):
    "points scored in fielding."
    pts = x*10 + y*10 + z*10
    return pts

def deleter(x):
    cono =sqlite3.connect('gamebase2.db')
    curo = cono.cursor()
    sel = "DELETE FROM teams WHERE name = '"+x+"';"
    curo.execute(sel)
    cono.commit()
    print('deleted')
    return

def namer(x):
    print(x)
    return
