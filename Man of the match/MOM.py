def batting_points(a,b,c,d):
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
    overs=b
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
    elif runs/overs >=2 and runs/overs < 3.5:
        pts = pts + 7
    elif runs/overs >=3.5 and runs/overs <= 4.5:
        pts = pts + 4

    # return the points scored by bowlers
    return pts
    
def fielding_points(x):
    "points scored in fielding."
    pts = x*10
    return pts
