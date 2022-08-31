"""
contacts application
contact: name,phone number
add contact
remove contact
search contact
"""
from genericpath import exists
import json

class contact:
    name=''
    pNum=''
    def __init__(self,name='',pNum='') -> None:
        self.name=name
        self.pNum=pNum
    def __str__(self) -> str:
        return json.dumps( {'name':self.name, 'phone':self.pNum})

    def return_contact_name(self,name):
        return self.name
    def return_contact_num(self,name):
        return self.pNum

class contacts:
    contacts=[]
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        res=''
        for contact in self.contacts:
            res+=contact.__str__()
        return res

    def addContact(self,name,pNum):
        self.contacts.append(contact(name,pNum))
    
    def rmvContact(self,name,data):
        with open(data,'r')as f:
            file=json.load(f)
            print(type(file))
            counter=0
            for i in (file):
                if i['name']==name:
                    del file[counter]
                counter+=1
        with open(data,'w')as f:
            json.dump(file,f,indent=4)
        # # for contact in self.contacts:
        #     if contact.return_contact_name(name)==name:
        #         self.contacts.remove(contact)
    def srcContact(self,name,data):
        with open(data,'r')as f:
            file=json.load(f)
            for i in file:
                if i['name']==name:
                    print(i)
        # for contact in self.contacts:
        #     if contact.return_contact_name(name)==name:
        #         print(contact)
    def jason(self,data):
        res=[]
        for contact in self.contacts:
            res.append( json.loads(contact.__str__()))
        with open(data,'r+')as f:
            json.dump(res,f,indent=4)
        
    
            
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
            pass

def main():
    data_file='contacts_cell.json'
    phonebook=contacts()
    selection=1
    chkJson(data_file)
    while selection != 'x':
        menu()
        selection = input('enter your selection')
        if selection == 'a': phonebook.addContact(input('enter contact name: '),input('enter contact phone number: '))
        if selection == 'r':phonebook.rmvContact(input('what name would you like to remove? '),data_file)
        if selection == 's':phonebook.srcContact(input('what name would you like to search? '),data_file)
        if selection == 'p':print(phonebook)
        if selection == 'j':phonebook.jason(data_file)
     



main()

