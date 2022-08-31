import json
from genericpath import exists

def menu():
    print('- a - add contact')
    print('- r - remove contact')
    print('- p - print all contacts')
    print('- s - search a contact')
    print('- j - format as JSON and save file!')
    print('- x - exit')
    
def chkJson(data):
    if exists(data):
        pass
    else:
        with open(data,'w')as f:
            x=[]
            json.dump(x,f)