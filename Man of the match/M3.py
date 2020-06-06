#main prog
#values provided.
import MOM
dicts=[
{'name':'Virat Kohli', 'role':'bat', 'runs':112, '4':10, '6':0,
'balls':119, 'field':0, 'points' : 0},
{'name':'du Plessis', 'role':'bat', 'runs':120, '4':11, '6':2,
'balls':112, 'field':0, 'points' : 0},
{'name':'Bhuvneshwar Kumar', 'role':'bowl', 'wkts':1, 'overs':10,
'runs':71, 'field':1, 'points' : 0},
{'name':'Yuzvendra Chahal', 'role':'bowl', 'wkts':2, 'overs':10,
'runs':45, 'field':0, 'points' : 0},
{'name':'Kuldeep Yadav', 'role':'bowl', 'wkts':3, 'overs':10, 'runs':34,
'field':0, 'points' : 0}
]

for i in range(len(dicts)):

    #calling fielding points
    #'field' value is parameter
    dicts[i]['points']=dicts[i]['points']+MOM.fielding_points(dicts[i]['field'])

    #calling batting points
    #   runs    4's     6's balls        are parameters
    if dicts[i]['role'] == 'bat':
        dicts[i]['points']=dicts[i]['points']+MOM.batting_points(dicts[i]['runs'],dicts[i]['4'],dicts[i]['6'],dicts[i]['balls'])

    #calling bowling points
    #wickets   over    runs              are parameter
    else:
        dicts[i]['points']=dicts[i]['points']+MOM.bowling_points(dicts[i]['wkts'],dicts[i]['overs'], dicts[i]['runs'])
        
#Final Result Display
motm = dicts[0].copy()
for player in dicts:
    print('Name: %s\tPoints: %d '%(player['name'], player['points']))
    if player['points'] > motm['points']:
        motm = player.copy()
    
#man of the match
print('\nMan of the Match:\nName: %s\tPoints: %d '%(motm['name'], motm['points']))

##input for exit
input()
